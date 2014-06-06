#define CosmicMuonAnalyzer_cxx
#include "CosmicMuonAnalyzer.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream>

inline double deltaPhi(double phi1, double phi2) { 
  double result = phi1 - phi2;
  while (result > TMath::Pi()) result -= 2*TMath::Pi();
  while (result <= -TMath::Pi()) result += 2*TMath::Pi();
  return result;
}

bool passTrackCut(const Track * track)
{
  // if( track->phi > 0 ) return false;


  // if( (fabs(track->eta) < 2.0) && (track->pt > 26) ) {
  if( (fabs(track->eta) < 2.0) ) {
  // if( (fabs(track->eta) < 2.0) && (track->pt > 26) && (track->dtStationsWithValidHits + track->cscStationsWithValidHits >= 3) ) {


  // Barrel
  // if( track->trackQuality && (fabs(track->eta) < 2.0) && (track->pt > 26) && (track->nValidHits > 6 ) && (fabs(track->eta) < 0.8) ) {
  // Endcaps
  // if( track->trackQuality && (fabs(track->eta) < 2.0) && (track->pt > 26) && (track->nValidHits > 6 ) && (fabs(track->eta) >= 0.8) ) {

    return true;
  }
  return false;
}

template <class T>
void fillEff(const double & value, TH1F * totalVsD0, const T & tracks, TH1F * passingVsD0)
{
  // Twice because we expect two tracks
  totalVsD0->Fill(value);
  totalVsD0->Fill(value);

  if( tracks->size() > 0 ) {
    bool firstPass = true;
    double firstPhi = 0.;
    std::vector<Track>::const_iterator it = tracks->begin();
    for( ; it != tracks->end(); ++it ) {
      // Always check that the second track (if any) is back to back. Discard tracks that are close by.
      // We are assuming the back-to-back topology of cosmic tracks.
      // PiOver2 just to check that they are not very close. The deltaPhi should be either ~0 or ~pi.
      if( firstPass || fabs(deltaPhi(firstPhi, it->phi)) > TMath::PiOver2() ) {
    	if( passTrackCut( &*it ) ) {
	  passingVsD0->Fill(value);
	  if( firstPass ) firstPhi = it->phi;
	  else break;
	  firstPass = false;
	}
      }
    }
  }
}

template <class T>
void fillDeltaR(double & muon_eta, double & muon_phi, TH1F * deltaR, const T & tracks)
{
  // Twice because we expect two tracks
  // double muonDxy = fabs((*muons)[0].dxy);
  // double muonDxy = fabs(returnValue->get((*muons)[0]));
  // totalVsD0->Fill(value);
  // totalVsD0->Fill(value);

  if( tracks->size() > 0 ) {
    bool firstPass = true;
    double firstPhi = 0.;
    std::vector<Track>::const_iterator it = tracks->begin();
    for( ; it != tracks->end(); ++it ) {
      // Always check that the second track (if any) is back to back. Discard tracks that are close by.
      // We are assuming the back-to-back topology of cosmic tracks.
      // PiOver2 just to check that they are not very close. The deltaPhi should be either ~0 or ~pi.
      if( firstPass || fabs(deltaPhi(firstPhi, it->phi)) > TMath::PiOver2() ) {
        if( passTrackCut( &*it ) ) {
          double DeltaR = sqrt( pow( (muon_eta - it->eta) , 2) + pow( (muon_phi - it->phi) , 2) );
          deltaR->Fill(DeltaR);
          if( firstPass ) firstPhi = it->phi;
          else break;
          firstPass = false;
        }
      }
    }
  }
}


double polynomial( const double & pt )
{
  return ( 0.1+1.91364 - 0.0211496*pt + 0.0000906055*pt*pt - 0.000000130650*pt*pt*pt );
}

/// Returns the maximum dxy error value allowed for the cuts
double dxyErrMax( const double & pt )
{
  double dxyErrMax = 1.;
  if(pt < 200 ) dxyErrMax = polynomial(pt);
  else dxyErrMax = polynomial(200);
  return std::min(dxyErrMax, 1.);
}


bool passMuonCut(const Track * muon)
{
  if( (fabs(muon->eta) < 2.)
      // (muon->nValidHits >= 0)
      && ( muon->dtStationsWithValidHits + muon->cscStationsWithValidHits > 3 )
      // && (fabs(muon->eta) >= 0.8) && (fabs(muon->eta) < 2.)
      // && (fabs(muon->eta) < 0.8)
      //&& fabs(muon->dxyError) < 1.
      //&& fabs(muon->dzError) < 1.
      // && (fabs(muon->dxyError) < dxyErrMax(muon->pt))
      // && (fabs(muon->dzError) < dxyErrMax(muon->pt)) // Note: the use of the same function is intentional.
      ) {

    // Use this for the efficiency vs z0
    // if( fabs(muon->dxy) < 4. && muon->pt > 35 ) {

    // Use this for the efficiency vs d0
    if( fabs(muon->dz) < 10. && muon->pt > 50 ) {

    // Use this for comparison plots with relaxed cut
    //  if( fabs(muon->dxy) < 50. && muon->pt > 35 ) {
      return true;
    }
  }
  return false;
}

void CosmicMuonAnalyzer::Loop()
{
  if (fChain == 0) return;

  Long64_t nentries = fChain->GetEntriesFast();

  int nBins = 50;
  int nBinsD0 = 100;
  int nBinsZ0 = 25;

  TString outFileName = "eff_data_dz10.root";
  if( MC_ ) outFileName = "eff_MC_dz10.root";
  TFile * outputFile = new TFile(outFileName, "RECREATE");
  outputFile->cd();

  // Float_t manualBins[] = { 0,4,8,12,16,20,24,28,32,36,44,52 };
  // Int_t  binnum = sizeof(manualBins)/sizeof(Float_t) - 1;

  // Vs D0
  TH1F * passingVsD0 = new TH1F("passingVsD0", "tracks found vs |d_{0}|", nBinsD0, 0., 500);
  TH1F * totalVsD0 = new TH1F("totalVsD0", "cosmics found vs |d_{0}| (filled twice)", nBinsD0, 0., 500.);
  TH1F * effVsD0 = (TH1F*)passingVsD0->Clone("effVsD0");

  TH1F * passingVsPhi = new TH1F("passingVsPhi", "tracks found vs #phi", 60, -3.14, 3.14);
  TH1F * totalVsPhi = new TH1F("totalVsPhi", "cosmics found vs #phi (filled twice)", 60, -3.14, 3.14);
  TH1F * effVsPhi = (TH1F*)passingVsPhi->Clone("effVsPhi");

  TH1F * passingVsEta = new TH1F("passingVsEta", "tracks found vs #eta", nBins, -2.5, 2.5);
  TH1F * totalVsEta = new TH1F("totalVsEta", "cosmics found vs #eta (filled twice)", nBins, -2.5, 2.5);
  TH1F * effVsEta = (TH1F*)passingVsEta->Clone("effVsEta");

  TH1F * passingVsPt = new TH1F("passingVsPt", "tracks found vs p_{T}", nBins, 0., 300.);
  TH1F * totalVsPt = new TH1F("totalVsPt", "cosmics found vs p_{T} (filled twice)", nBins, 0., 300.);
  TH1F * effVsPt = (TH1F*)passingVsPt->Clone("effVsPt");

  TH1F * passingVsValidHits = new TH1F("passingVsValidHits", "tracks found vs valid hits", 6, 0., 6.);
  TH1F * totalVsValidHits = new TH1F("totalVsValidHits", "cosmics found vs valid hits (filled twice)", 6, 0., 6.);
  // TH1F * effVsValidHits = (TH1F*)passingVsValidHits->Clone("effVsValidHits");

  TH1F * passingVsDz = new TH1F("passingVsDz", "tracks found vs |d_{z}|", nBinsZ0, 0., 100.);
  //  TH1F * passingVsDz = new TH1F("passingVsDz", "tracks found vs |d_{z}|", binnum, manualBins);
  TH1F * totalVsDz = new TH1F("totalVsDz", "cosmics found vs |d_{z}| (filled twice)", nBinsZ0, 0., 100.);
  //  TH1F * totalVsDz = new TH1F("totalVsDz", "cosmics found vs |d_{z}| (filled twice)", binnum, manualBins);
  TH1F * effVsDz = (TH1F*)passingVsDz->Clone("effVsDz");

  TH1F * passingVsChi2 = new TH1F("passingVsChi2", "tracks found vs #chi^{2}/ndof", 250, 0., 50.);
  TH1F * totalVsChi2 = new TH1F("totalVsChi2", "cosmics found vs #chi^{2}/ndof (filled twice)", 250, 0., 50.);
  // TH1F * effVsChi2 = (TH1F*)passingVsChi2->Clone("effVsChi2");

  TH1F * deltaR = new TH1F("deltaR", "deltaR", 12, 0, 0.12);

  TH2F * totalD0errVsPt = new TH2F("totalD0errVsPt", "totalD0errVsPt", nBins, 0., 300., nBins, 0., 2.);
  TH2F * totalDzerrVsPt = new TH2F("totalDzerrVsPt", "totalDzerrVsPt", nBins, 0., 300., nBins, 0., 2.);
  TH2F * totalD0VsDz = new TH2F("totalD0VsDz", "totalD0VsDz", nBins, 0., 100., nBins, 0., 50.);
  // TH2F * totalD0VsPt = new TH2F("totalD0VsPt", "totalD0VsPt", nBins, 0., 300., nBins, -10., 10.);
  //  TH2F * totalD0relVsPt = new TH2F("totalD0relVsPt", "totalD0relVsPt", nBins, 0., 300., nBins, 0., 100.);

  TH1F * passingVsGenD0 = 0;
  TH1F * totalVsGenD0 = 0;
  TH1F * effVsGenD0 = 0;

  TH1F * passingVsGenPhi = 0;
  TH1F * totalVsGenPhi = 0;
  TH1F * effVsGenPhi = 0;

  TH1F * passingVsGenEta = 0;
  TH1F * totalVsGenEta = 0;
  TH1F * effVsGenEta = 0;

  TH1F * passingVsGenPt = 0;
  TH1F * totalVsGenPt = 0;
  TH1F * effVsGenPt = 0;

  TH1F * passingVsGenDz = 0;
  TH1F * totalVsGenDz = 0;
  TH1F * effVsGenDz = 0;



  if( MC_ ) {
    passingVsGenD0 = new TH1F("passingVsGenD0", "tracks found vs |gen d_{0}|", nBinsD0, 0., 500.);
    totalVsGenD0 = new TH1F("totalVsGenD0", "genParticles found vs |gen d_{0}| (filled twice)", nBinsD0, 0., 500.);
    effVsGenD0 = (TH1F*)passingVsGenD0->Clone("effVsGenD0");

    passingVsGenPhi = new TH1F("passingVsGenPhi", "tracks found vs gen #phi", 60, -3.14, 3.14);
    totalVsGenPhi = new TH1F("totalVsGenPhi", "genParticles found vs gen #phi (filled twice)", 60, -3.14, 3.14);
    effVsGenPhi = (TH1F*)passingVsGenPhi->Clone("effVsGenPhi");

    passingVsGenEta = new TH1F("passingVsGenEta", "tracks found vs gen #eta", nBins, -2.5, 2.5);
    totalVsGenEta = new TH1F("totalVsGenEta", "genParticles found vs gen #eta (filled twice)", nBins, -2.5, 2.5);
    effVsGenEta = (TH1F*)passingVsGenEta->Clone("effVsGenEta");

    passingVsGenPt = new TH1F("passingVsGenPt", "tracks found vs gen p_{T}", nBins, 0., 300.);
    totalVsGenPt = new TH1F("totalVsGenPt", "genParticles found vs gen p_{T} (filled twice)", nBins, 0., 300.);
    effVsGenPt = (TH1F*)passingVsGenPt->Clone("effVsGenPt");

    passingVsGenDz = new TH1F("passingVsGenDz", "tracks found vs gen |d_{z}|", nBinsZ0, 0., 100.);
    totalVsGenDz = new TH1F("totalVsGenDz", "genParticles found vs gen |d_{z}| (filled twice)", nBinsZ0, 0., 100.);
    effVsGenDz = (TH1F*)passingVsGenDz->Clone("effVsGenDz");
  }

  TH1F * etaRelError = new TH1F("etaRelError", "relative error on #eta", nBins, 0., 1.5);
  TH1F * dxyRelError = new TH1F("dxyRelError", "relative error on d_{0}", nBins, 0., 1.5);
  TH1F * dzRelError = new TH1F("dzRelError", "relative error on z_{0}", nBins, 0., 1.5);

  Long64_t nbytes = 0, nb = 0;
  for (Long64_t jentry=0; jentry<nentries;jentry++) {
    Long64_t ientry = LoadTree(jentry);
    if (ientry < 0) break;
    nb = fChain->GetEntry(jentry);   nbytes += nb;

    if( jentry % 1000 == 0 ) {
      std::cout << "Analyzed " << jentry << " events" << std::endl;
    }

    // Compute efficiency by counting how many tracks are reconstructed when two (opposite) are expected
    // Check this efficiency for tracks passing the analysis cuts.
    // Use only events in which exactly one cosmic1LegMuon has been reconstructed.
    if( muons->size() != 1 ) continue;

    if( !passMuonCut(&((*muons)[0])) ) continue;
    //	if( genParticles->size() != 1 ) continue;
    //	if( run > 187460 && run < 189147 && fabs((*muons)[0].dxy) < 11) continue; 

    //    if( muons->size() == 0 ) continue; 
    // Efficiency vs d0
    fillEff(fabs((*muons)[0].dxy), totalVsD0, tracks, passingVsD0);
    fillEff((*muons)[0].phi, totalVsPhi, tracks, passingVsPhi);
    fillEff((*muons)[0].eta, totalVsEta, tracks, passingVsEta);
    fillEff((*muons)[0].pt, totalVsPt, tracks, passingVsPt);
    fillEff((*muons)[0].dtStationsWithValidHits+(*muons)[0].cscStationsWithValidHits, totalVsValidHits, tracks, passingVsValidHits);
    fillEff(fabs((*muons)[0].dz), totalVsDz, tracks, passingVsDz);
    fillEff((*muons)[0].normalizedChi2, totalVsChi2, tracks, passingVsChi2);
    fillDeltaR((*muons)[0].eta, (*muons)[0].phi, deltaR, tracks);
    
    totalD0errVsPt->Fill((*muons)[0].pt,(*muons)[0].dxyError);
    totalDzerrVsPt->Fill((*muons)[0].pt,(*muons)[0].dzError);
    totalD0VsDz->Fill(fabs((*muons)[0].dz),fabs((*muons)[0].dxy));
    //	totalD0VsPt->Fill((*muons)[0].pt,(fabs((*muons)[0].dxy)-fabs((*genParticles)[0].dxy))/fabs((*genParticles)[0].dxy) );
    //	totalD0VsPt->Fill((*muons)[0].pt,fabs((*muons)[0].dxy));

    etaRelError->Fill((*muons)[0].etaError/fabs((*muons)[0].eta));
    dxyRelError->Fill((*muons)[0].dxyError/fabs((*muons)[0].dxy));
    dzRelError->Fill((*muons)[0].dzError/fabs((*muons)[0].dz));

    if( MC_ ) {

      fillEff(fabs((*genParticles)[0].dxy), totalVsGenD0, tracks, passingVsGenD0);
      fillEff((*genParticles)[0].phi, totalVsGenPhi, tracks, passingVsGenPhi);
      fillEff((*genParticles)[0].eta, totalVsGenEta, tracks, passingVsGenEta);
      fillEff((*genParticles)[0].pt, totalVsGenPt, tracks, passingVsGenPt);
      fillEff(fabs((*genParticles)[0].dz), totalVsGenDz, tracks, passingVsGenDz);
    }
/*
    // Apply also a dxy cut for the efficiency vs eta
    if( (*muons)[0].dxy > 5. ) continue;
    // Efficiency vs eta
    fillEff((*muons)[0].eta, totalVsEta, tracks, passingVsEta);
    if( MC_ ) {
      fillEff((*genParticles)[0].eta, totalVsGenEta, tracks, passingVsGenEta);
    }
*/
  }

  // Efficiency vs d0
  passingVsD0->Sumw2();
  totalVsD0->Sumw2();
  effVsD0->Divide(passingVsD0, totalVsD0, 1., 1., "B");
  if( MC_ ) {
    passingVsGenD0->Sumw2();
    totalVsGenD0->Sumw2();
    effVsGenD0->Divide(passingVsGenD0, totalVsGenD0, 1., 1., "B");
  }
  // Efficiency vs Phi
  passingVsPhi->Sumw2();
  totalVsPhi->Sumw2();
  effVsPhi->Divide(passingVsPhi, totalVsPhi, 1., 1., "B");
  if( MC_ ) { 
    passingVsGenPhi->Sumw2();
    totalVsGenPhi->Sumw2();
    effVsGenPhi->Divide(passingVsGenPhi, totalVsGenPhi, 1., 1., "B");
  }
  // Efficiency vs dz
  passingVsDz->Sumw2();
  totalVsDz->Sumw2();
  effVsDz->Divide(passingVsDz, totalVsDz, 1., 1., "B");
  if( MC_ ) {
    passingVsGenDz->Sumw2();
    totalVsGenDz->Sumw2();
    effVsGenDz->Divide(passingVsGenDz, totalVsGenDz, 1., 1., "B");
  }   
  // Efficiency vs pt
  passingVsPt->Sumw2();
  totalVsPt->Sumw2();
  effVsPt->Divide(passingVsPt, totalVsPt, 1., 1., "B");
  if( MC_ ) { 
    passingVsGenPt->Sumw2();
    totalVsGenPt->Sumw2();
    effVsGenPt->Divide(passingVsGenPt, totalVsGenPt, 1., 1., "B");
  }   
  // Efficiency vs eta
  passingVsEta->Sumw2();
  totalVsEta->Sumw2();
  effVsEta->Divide(passingVsEta, totalVsEta, 1., 1., "B");
  if( MC_ ) {
    passingVsGenEta->Sumw2();
    totalVsGenEta->Sumw2();
    effVsGenEta->Divide(passingVsGenEta, totalVsGenEta, 1., 1., "B");
  }

  outputFile->Write();
  outputFile->Close();
}
