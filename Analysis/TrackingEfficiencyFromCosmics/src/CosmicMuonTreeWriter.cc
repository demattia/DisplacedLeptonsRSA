// -*- C++ -*-
//
// Package:    CosmicMuonTreeWriter
// Class:      CosmicMuonTreeWriter
//
/**\class CosmicMuonTreeWriter CosmicMuonTreeWriter.cc Analysis/CosmicMuonTreeWriter/src/CosmicMuonTreeWriter.cc

 Description: Can be used to save the information in a tree. The tracks can then be accessed with the macros under test/Macros.

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Marco De Mattia,40 1-A11,
//         Created:  Thu Mar 29 13:29:00 CEST 2012
// $Id: CosmicMuonTreeWriter.cc,v 1.4 2012/04/02 15:07:33 demattia Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"

#include "SimDataFormats/Track/interface/SimTrackContainer.h"

#include "DataFormats/GeometryCommonDetAlgo/interface/Measurement1D.h"
#include "DataFormats/Math/interface/Error.h"
#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "TrackingTools/GeomPropagators/interface/AnalyticalImpactPointExtrapolator.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/PatternTools/interface/TransverseImpactPointExtrapolator.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include <TVector3.h>

#include "Analysis/SmartPropagatorWithIP/interface/SmartPropagatorWithIP.h"
#include "Analysis/Records/interface/SmartPropagatorWithIPComponentsRecord.h"
#include "Analysis/RootTreeProducers/interface/RootTreeHandler.h"
#include "Analysis/RootTreeProducers/interface/Track.h"
#include "Analysis/RootTreeProducers/interface/GenParticle.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonTime.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtra.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtraMap.h"

#include <boost/foreach.hpp>

//
// class declaration
//

class CosmicMuonTreeWriter : public edm::EDAnalyzer {
public:
  explicit CosmicMuonTreeWriter(const edm::ParameterSet&);
  ~CosmicMuonTreeWriter();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob();

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  // Helpers to fill the Track and GenParticle objects.
  void fillTrackToTreeTrack( Track & treeTrack, const reco::Track & track );
  void fillTrackToTreeTrack( Track & treeTrack, const reco::Track & track, const SmartPropagatorWithIP::IP & ip );
  // For the tree
  template <class T>
  void fillTreeTracks( const T & collection, const edm::Handle<reco::MuonCollection> & recoMuons,
		       const reco::MuonTimeExtraMap & timeMap1,
		       const GlobalPoint & vertex, std::vector<Track> & tracks, const bool readTiming );
  template <class T>
  GenParticle fillGenParticle(const T & it, const SmartPropagatorWithIP::IP & ip);

  // ----------member data ---------------------------
  bool useMCtruth_;

  AlgebraicSymMatrix55 nullCovariance_;
  bool recomputeIP_;
  edm::InputTag outputName_;
  edm::InputTag muonCollection_;
  edm::InputTag trackCollection_;
  edm::InputTag recoMuonTag_;
  edm::InputTag timeTags_;
  edm::ESHandle<TransientTrackBuilder> theB_;
  const SmartPropagatorWithIP * smartPropIP_;
  boost::shared_ptr<RootTreeHandler> treeHandler_;
  std::vector<Track> tracks_;
  std::vector<Track> muons_;
  std::vector<GenParticle> genParticles_;
};

CosmicMuonTreeWriter::CosmicMuonTreeWriter(const edm::ParameterSet& iConfig) :
  useMCtruth_(iConfig.getParameter<bool>("UseMCtruth")),
  recomputeIP_(iConfig.getParameter<bool>("RecomputeIP")),
  outputName_(iConfig.getParameter<edm::InputTag>("OutPutName")),
  muonCollection_(iConfig.getParameter<edm::InputTag>("MuonCollection")),
  trackCollection_(iConfig.getParameter<edm::InputTag>("TrackCollection")),
  recoMuonTag_(iConfig.getParameter<edm::InputTag>("RecoMuonCollection")),
  timeTags_(iConfig.getParameter<edm::InputTag>("timeExtraSrc"))
{
  // Initialize the nullCovariance matrix
  for( unsigned int i=0; i<5; ++i ) {
    for( unsigned int j=0; j<5; ++j ) {
      nullCovariance_(i,j) = 0;
    }
  }
  smartPropIP_ = 0;

  //treeHandler_.reset(new RootTreeHandler(muonCollection_.label()+".root", "MuonsTree"));
  treeHandler_.reset(new RootTreeHandler(outputName_.label()+".root", "MuonsTree"));
  treeHandler_->addBranch("tracks", "std::vector<Track>", &tracks_);
  treeHandler_->addBranch("muons", "std::vector<Track>", &muons_);
  //treeHandler_->addBranch("muons", "std::vector<Muon>", &muons_);
  treeHandler_->addBranch("genParticles", "std::vector<GenParticle>", &genParticles_);
}

CosmicMuonTreeWriter::~CosmicMuonTreeWriter()
{
  std::cout << "Saving trees" << std::endl;
  treeHandler_->writeTree();
}

void CosmicMuonTreeWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // Vertex with respect to which do all the propagations
  GlobalPoint vertex(0,0,0);

  // Load the transient track builder
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB_);

  // Load the propagator and IP calculator
  edm::ESHandle<Propagator> smartPropIPHandle;
  iSetup.get<SmartPropagatorWithIPComponentsRecord>().get("SmartPropagatorWithIP", smartPropIPHandle);
  smartPropIP_ = dynamic_cast<const SmartPropagatorWithIP*>(&*smartPropIPHandle);

  edm::Handle<reco::MuonCollection> recoMuons;
  // Fill the trees
  try {
    edm::Handle<reco::TrackCollection> allTracks;
    iEvent.getByLabel(trackCollection_, allTracks);

    if( recoMuonTag_.label() != "" ) {
      edm::Handle<reco::MuonTimeExtraMap> timeMap1;
      iEvent.getByLabel(recoMuonTag_, recoMuons);
      iEvent.getByLabel(timeTags_.label(), "combined", timeMap1);
      // std::cout << "RSA size = " << allTracks->size() << std::endl;
      fillTreeTracks(*(allTracks.product()), recoMuons, *(timeMap1.product()), vertex, tracks_, true);
    }
    else {
      fillTreeTracks(*(allTracks.product()), recoMuons, reco::MuonTimeExtraMap(), vertex, tracks_, false);
    }
  }
  catch (cms::Exception & ex) {
    std::cerr << ex;
  }

  try {
    edm::Handle<reco::TrackCollection> staMuons;
    iEvent.getByLabel(muonCollection_, staMuons);
    fillTreeTracks(*(staMuons.product()), recoMuons, reco::MuonTimeExtraMap(), vertex, muons_, false);
  }
  catch (cms::Exception & ex) {
    std::cerr << ex;
  }


  // Gen Particles. Note: selecting stable muons only
  edm::Handle<reco::GenParticleCollection> genParticles;
  if( useMCtruth_ ) {
    iEvent.getByLabel("genParticles", genParticles);
    for( reco::GenParticleCollection::const_iterator it = genParticles->begin(); it != genParticles->end(); ++it ) {
      if( it->status() == 1 && fabs(it->pdgId()) == 13 ) {
        // Compute impact parameters for generator particle
        SmartPropagatorWithIP::IP ip;
        if( sqrt(pow(it->vertex().x(),2) + pow(it->vertex().y(),2)) < 110. && fabs(it->vertex().z()) < 280. ) {
          ip = smartPropIP_->computeGenImpactParametersInsideTkVol( *it, it->vertex(), it->charge(), GlobalPoint(0,0,0) );
        }
        else {
          ip = smartPropIP_->computeGenImpactParametersOutsideTkVol( *it, it->vertex(), it->charge(), GlobalPoint(0,0,0) );
        }
        genParticles_.push_back(fillGenParticle(it, ip));
      }
    }
  }

  // Fill the trees
  treeHandler_->saveToTree(iEvent.id().event(), iEvent.run());
  tracks_.clear();
  muons_.clear();
  genParticles_.clear();


#ifdef THIS_IS_AN_EVENT_EXAMPLE
  Handle<ExampleData> pIn;
  iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
  ESHandle<SetupData> pSetup;
  iSetup.get<SetupRecord>().get(pSetup);
#endif
}

// ------------ method called once each job just before starting event loop  ------------
void CosmicMuonTreeWriter::beginJob()
{
  // edm::Service<TFileService> fileService;
}

// ------------ method called once each job just after ending the event loop  ------------
void CosmicMuonTreeWriter::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void CosmicMuonTreeWriter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void CosmicMuonTreeWriter::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void CosmicMuonTreeWriter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void CosmicMuonTreeWriter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void CosmicMuonTreeWriter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

template <class T>
void CosmicMuonTreeWriter::fillTreeTracks( const T & collection, const edm::Handle<reco::MuonCollection> & recoMuons,
					   const reco::MuonTimeExtraMap & timeMap1,
					   const GlobalPoint & vertex, std::vector<Track> & tracks,
					   const bool readTiming )
{
  typename T::const_iterator it = collection.begin();
  for( ; it != collection.end(); ++it ) {
    SmartPropagatorWithIP::IP ip(it->pt(), it->ptError(), it->eta(), it->etaError(), it->phi(), it->phiError(),
                                 it->dxy(), it->dxyError(), it->dz(), it->dzError());
    Track treeTrack;

    if( readTiming ) {
      // Match the RSA to the SA. This is needed because RSA are not in the reco::Muon and we need
      // to access timing information from the reco::Muon. The RSA is a refit of the SA, the timing
      // of the hits is the same (but do not use anything with IP or beamspot constraint).
      // Analyze the short info stored directly in reco::Muon
      const math::XYZPoint & rsaInnerPoint(it->innerPosition());
      const math::XYZPoint & rsaOuterPoint(it->outerPosition());

      float minDxIn = 1000.;
      float minDyIn = 1000.;
      float minDzIn = 1000.;
      float minDxOut = 1000.;
      float minDyOut = 1000.;
      float minDzOut = 1000.;
      int imucount = 0;

      // Loop over the standAloneMuons and take the one with the closest inner and outer position.
      // Only save the timing if the matching is close enough (<5cm in x,y and <50cm in z).
      const reco::Muon * matchedSA = 0;
      int imucountMatch = -1;
      // std::cout << "muons size = " << recoMuons->size() << std::endl;
      for (reco::MuonCollection::const_iterator sa=recoMuons->begin(); sa!=recoMuons->end(); ++sa, ++imucount) {
	if( sa->isStandAloneMuon() ) {

	  const math::XYZPoint & saInnerPoint(sa->standAloneMuon()->innerPosition());
	  const math::XYZPoint & saOuterPoint(sa->standAloneMuon()->outerPosition());
	  // std::cout << "minDIn = " << minDxIn << ", " << minDyIn << ", " << minDzIn << std::endl;
	  // std::cout << "minDOut = " << minDxOut << ", " << minDyOut << ", " << minDzOut << std::endl;
	  if( fabs(saInnerPoint.x() - rsaInnerPoint.x()) < minDxIn &&
	      fabs(saInnerPoint.y() - rsaInnerPoint.y()) < minDyIn &&
	      fabs(saOuterPoint.x() - rsaOuterPoint.x()) < minDxOut &&
	      fabs(saOuterPoint.y() - rsaOuterPoint.y()) < minDyOut ) {
	    minDxIn = fabs(saInnerPoint.x() - rsaInnerPoint.x());
	    minDyIn = fabs(saInnerPoint.y() - rsaInnerPoint.y());
	    minDzIn = fabs(saInnerPoint.z() - rsaInnerPoint.z());
	    minDxOut = fabs(saOuterPoint.x() - rsaOuterPoint.x());
	    minDyOut = fabs(saOuterPoint.y() - rsaOuterPoint.y());
	    minDzOut = fabs(saOuterPoint.z() - rsaOuterPoint.z());

	    // std::cout << "better minDIn = " << minDxIn << ", " << minDyIn << ", " << minDzIn << std::endl;
	    // std::cout << "better minDOut = " << minDxOut << ", " << minDyOut << ", " << minDzOut << std::endl;


	    // Check for good matching and fill timing information
	    if( minDxIn > 5 || minDyIn > 5 || minDxOut > 5 || minDyOut > 5 || minDzIn > 50 || minDzOut > 50 ) continue;


	    matchedSA = &*sa;
	    imucountMatch = imucount;
	  }
	}
      }

      // Save the closest match
      treeTrack.minDxIn = minDxIn;
      treeTrack.minDyIn = minDyIn;
      treeTrack.minDzIn = minDzIn;
      treeTrack.minDxOut = minDxOut;
      treeTrack.minDyOut = minDyOut;
      treeTrack.minDzOut = minDzOut;

      if( matchedSA != 0 && imucountMatch != -1 ) {
	if (matchedSA->isTimeValid()) {
	  // number of muon stations used
	  treeTrack.nDof = matchedSA->time().nDof;

	  // time of arrival at the IP for the Beta=1 hypothesis
	  //  a) particle is moving from inside out
	  treeTrack.timeAtIpInOut = matchedSA->time().timeAtIpInOut;
	  treeTrack.timeAtIpInOutErr = matchedSA->time().timeAtIpInOutErr;
	  //  b) particle is moving from outside in
	  treeTrack.timeAtIpOutIn = matchedSA->time().timeAtIpOutIn;
	  treeTrack.timeAtIpOutInErr = matchedSA->time().timeAtIpOutInErr;
	}
	// Save the MuonTimeExtra information
	reco::MuonRef muonR(recoMuons,imucountMatch);
	const reco::MuonTimeExtra & timeMapCmb = timeMap1[muonR];
	treeTrack.timeAtIpInOutC = timeMapCmb.timeAtIpInOut();
	treeTrack.timeAtIpInOutErrC = timeMapCmb.timeAtIpInOutErr();
	treeTrack.timeAtIpOutInC = timeMapCmb.timeAtIpOutIn();
	treeTrack.timeAtIpOutInErrC = timeMapCmb.timeAtIpOutInErr();
	// 1/beta for prompt particle hypothesis
	treeTrack.inverseBeta = timeMapCmb.inverseBeta();
	treeTrack.inverseBetaErr = timeMapCmb.inverseBetaErr();
	// unconstrained 1/beta (time is free)
	treeTrack.freeInverseBeta = timeMapCmb.freeInverseBeta();
	treeTrack.freeInverseBetaErr = timeMapCmb.freeInverseBetaErr();
      }
    }

    // Store the Track
    if( recomputeIP_ ) {
      ip = smartPropIP_->computeImpactParameters(*it, vertex);
      fillTrackToTreeTrack(treeTrack, *it, ip);
      tracks.push_back(treeTrack);
    }
    else {
      fillTrackToTreeTrack(treeTrack, *it);
      tracks.push_back(treeTrack);
    }
  }
}

template <class T>
GenParticle CosmicMuonTreeWriter::fillGenParticle(const T & it, const SmartPropagatorWithIP::IP & ip)
{
  GenParticle p;
  p.pt = it->pt();
  p.eta = it->eta();
  p.phi = it->phi();
  p.charge = it->charge();
  p.dxy = ip.dxyValue;
  p.dz = ip.dzValue;
  p.referencePointRadius = 0.;
  p.referencePointZ = 0.;
  p.vx = it->vertex().x();
  p.vy = it->vertex().y();
  p.vz = it->vertex().z();
  p.pid = it->pdgId();
  return p;
}

void CosmicMuonTreeWriter::fillTrackToTreeTrack( Track & treeTrack, const reco::Track & track )
{
  treeTrack.pt = track.pt();
  treeTrack.ptError = track.ptError();
  treeTrack.eta = track.eta();
  treeTrack.etaError = track.etaError();
  treeTrack.phi = track.phi();
  treeTrack.phiError = track.phiError();
  treeTrack.charge = track.charge();
  // treeTrack.vx = track.vx();
  // treeTrack.vy = track.vy();
  // treeTrack.vz = track.vz();
  treeTrack.chi2 = track.chi2();
  treeTrack.normalizedChi2 = track.normalizedChi2();
  treeTrack.referencePointRadius = std::sqrt(std::pow(track.referencePoint().x(),2)+std::pow(track.referencePoint().y(),2));
  treeTrack.referencePointZ = track.referencePoint().z();
  treeTrack.nHits = track.recHitsSize();
  treeTrack.nValidHits = track.found();
  treeTrack.nValidPlusInvalidHits = track.found()+track.lost();
  treeTrack.trackAlgorithm = track.algo();
  reco::TrackBase::TrackQuality trackQualityHighPurity = reco::TrackBase::qualityByName("highPurity");
  treeTrack.trackQuality = track.quality(trackQualityHighPurity);
  try {
    treeTrack.innermostHitRadius = track.innerPosition().r();
    treeTrack.innermostHitZ = track.innerPosition().z();
    treeTrack.muonStationsWithAnyHits = track.hitPattern().muonStationsWithAnyHits();
    // treeTrack.dtStationsWithAnyHits = track.hitPattern().dtStationsWithAnyHits();
    // treeTrack.cscStationsWithAnyHits = track.hitPattern().cscStationsWithAnyHits();
    treeTrack.dtStationsWithValidHits = track.hitPattern().dtStationsWithValidHits();
    treeTrack.cscStationsWithValidHits = track.hitPattern().cscStationsWithValidHits();
  }
  catch (cms::Exception & ex) {
    // Not present in AOD
    // std::cerr << ex;
  }
  treeTrack.dxy = track.dxy();
  treeTrack.dxyError = track.dxyError();
  treeTrack.dz = track.dz();
  treeTrack.dzError = track.dzError();
}

void CosmicMuonTreeWriter::fillTrackToTreeTrack(Track & treeTrack, const reco::Track & track, const SmartPropagatorWithIP::IP & ip)
{
  fillTrackToTreeTrack(treeTrack, track);
  treeTrack.pt = ip.pt;
  treeTrack.ptError = ip.ptError;
  treeTrack.eta = ip.eta;
  treeTrack.etaError = ip.etaError;
  treeTrack.phi = ip.phi;
  treeTrack.phiError = ip.phiError;
  treeTrack.dxy = ip.dxyValue;
  treeTrack.dxyError = ip.dxyError;
  treeTrack.dz = ip.dzValue;
  treeTrack.dzError = ip.dzError;
}

//define this as a plug-in
DEFINE_FWK_MODULE(CosmicMuonTreeWriter);
