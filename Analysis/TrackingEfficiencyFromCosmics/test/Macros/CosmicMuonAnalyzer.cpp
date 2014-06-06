#include "CosmicMuonAnalyzer.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream>

CosmicMuonAnalyzer::CosmicMuonAnalyzer(const bool MC) :
  MC_(MC)
{
   Init();
   Loop();
}

CosmicMuonAnalyzer::~CosmicMuonAnalyzer()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t CosmicMuonAnalyzer::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t CosmicMuonAnalyzer::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (!fChain->InheritsFrom(TChain::Class()))  return centry;
   TChain *chain = (TChain*)fChain;
   if (chain->GetTreeNumber() != fCurrent) {
      fCurrent = chain->GetTreeNumber();
      Notify();
   }
   return centry;
}

// void CosmicMuonAnalyzer::Init(TTree *tree)
void CosmicMuonAnalyzer::Init()
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   tracks = 0;
   muons = 0;
   genParticles = 0;
   // Set branch addresses and branch pointers
   // if (!tree) return;
   // fChain = tree;

   // Read all the trees
   fChain = new TChain("T");
   if( MC_ ) {
     //For MC
     // fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/Cosmics/Trees_MC/cosmicMuons1Leg_MC_SA.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/cosmicMuons1Leg_MC.root");
     // fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Cosmics_PPReco_Tree/cosmicMuons1Leg.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/Delay25/cosmicMuons1Leg.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/Delay50/cosmicMuons1Leg.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/Delay50Sharp/cosmicMuons1Leg.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/Delay25Sharp/cosmicMuons1Leg.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_7/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC_PPReco_Timing/cosmicMuons1Leg.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_7/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC_PPReco_Timing/Anticipate25/cosmicMuons1Leg.root");
     // fChain->Add("/uscmst1b_scratch/lpc1/3DayLifetime/demattia/cosmicMuons1Leg.root");
     fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/Cosmics/PPrecoTiming_Anticipate25/cosmicMuons1Leg.root");
   }
   else {
     //For data
     // fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/Cosmics/Trees_SA/cosmicMuons1Leg_RunA.root");
     // fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/Cosmics/Trees_SA/cosmicMuons1Leg_RunB.root");
     // fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/Cosmics/Trees_SA/cosmicMuons1Leg_RunC.root");
     // fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/Cosmics/CRAFT_Trees_SA/CRAFT_Run1_Tree_SA/cosmicMuons1Leg.root");
     fChain->Add("/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Cosmics/CRAFT_Timing/cosmicMuons1Leg.root");
     // fChain->Add("/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/cosmicMuons1Leg_Data.root");
   }

   // For global muon trees
//  fChain->Add("/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/CMSDAS2013/CMSSW_5_3_6/src/MCTree/cosmicMuons1Leg_p10_globalMuons.root");
//  fChain->Add("/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/CMSDAS2013/CMSSW_5_3_6/src/DataTree/cosmicMuons1Leg_CRAFT_globalMuons.root");

   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("tracks", &tracks, &b_tracks);
   fChain->SetBranchAddress("muons", &muons, &b_muons);
   if( MC_ ) {
     fChain->SetBranchAddress("genParticles", &genParticles, &b_genParticles);
   }
   Notify();
}

Bool_t CosmicMuonAnalyzer::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void CosmicMuonAnalyzer::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
  if (!fChain) return;
  fChain->Show(entry);
}
// Int_t CosmicMuonAnalyzer::Cut(Long64_t entry)
// {
  // This function may be called from Loop.
  // returns  1 if entry is accepted.
  // returns -1 otherwise.
//   return 1;
// }

inline double deltaPhi(double phi1, double phi2) { 
  double result = phi1 - phi2;
  while (result > TMath::Pi()) result -= 2*TMath::Pi();
  while (result <= -TMath::Pi()) result += 2*TMath::Pi();
  return result;
}


bool passTrackCut(const Track * muon)
{
  // if( fabs(muon->eta) < 1. && muon->pt > 26 ) return true;
  if( fabs(muon->eta) < 1. && muon->pt > 26 && // muon->normalizedChi2 < 2 &&
      (muon->dtStationsWithValidHits+muon->cscStationsWithValidHits) > 2 ) return true;
  return false;
}


template <class T>
void fillEff(const double & value, TH1F * totalVsD0, const T & tracks, TH1F * passingVsD0, const bool topBottom, const float & weight)
{
  totalVsD0->Fill(value, weight);
  if( tracks->size() > 1 ) {
    std::vector<Track>::const_iterator it = tracks->begin();
    for( ; it != tracks->end(); ++it ) {
      if( (!topBottom && (it->phi > 0 && it->phi < TMath::Pi())) ||
	  (topBottom && (it->phi < 0 && it->phi > -TMath::Pi())) ) {
//       if( (!topBottom && (it->phi > 1 && it->phi < 2)) ||
// 	  (topBottom && (it->phi < -1 && it->phi > -2)) ) {
	if( passTrackCut( &*it ) ) {
	  passingVsD0->Fill(value, weight);
	  break;
	}
      }
    }
  }
}


bool passMuonCut(const Track * muon)
{
  // if( muon->pt > 50 && fabs(muon->dz) < 10. && fabs(muon->dxyError) < 10. && fabs(muon->dzError) < 10. && fabs(muon->eta) < 1. &&
  // if( muon->pt > 26 && fabs(muon->eta) < 1. ) return true;
  // if( muon->pt > 26 && fabs(muon->eta) < 0.7 && // fabs(muon->dz) < 10. && muon->normalizedChi2 < 2 &&
  // if( muon->pt > 26 && fabs(muon->eta) < 0.7 && fabs(muon->dz) < 20. && fabs(muon->dxy) < 20. && muon->normalizedChi2 < 2 &&
  if( muon->pt > 30 && fabs(muon->eta) < 1. &&
      fabs(muon->dz) < 50. &&
      // fabs(muon->dxy) < 50. &&
      // muon->normalizedChi2 < 2 &&
      muon->timeAtIpInOut > -40 && muon->timeAtIpInOut < -20 &&
      fabs(muon->dxyError) < 10. && fabs(muon->dzError) < 10. &&
      (muon->dtStationsWithValidHits+muon->cscStationsWithValidHits) >= 2 ) return true;
  return false;
  // return passTrackCut(muon);
}


void CosmicMuonAnalyzer::Loop()
{
  if (fChain == 0) return;

  Long64_t nentries = fChain->GetEntriesFast();

  bool topBottom = true;

  int nBins = 100;
  int nBinsD0 = 50;
  int nBinsZ0 = 50;

  // Load the weights
  TFile * weightFile = new TFile("weight.root", "READ");
  TH1F * weightHisto = (TH1F*)weightFile->Get("TrackChi2Weight");
  TFile * weightFileEtaPhi = new TFile("weightEtaPhi.root", "READ");
  TH2F * weightHistoEtaPhi = (TH2F*)weightFileEtaPhi->Get("EtaPhiWeight");

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

  TH1F * hPhiAll = new TH1F("PhiAll", "muon #phi", 60, -3.14, 3.14);
  TH1F * hPhiAfterSel = new TH1F("PhiAfterSel", "muon #phi", 60, -3.14, 3.14);
  TH1F * hPhi1 = new TH1F("TotalPhi", "muon 1 #phi", 60, -3.14, 3.14);
  TH1F * hPhi2 = new TH1F("PassingPhi", "muon 2 #phi", 60, -3.14, 3.14);
  TH1F * hEta1 = new TH1F("TotalEta", "muon 1 #eta", 60, -2.4, 2.4);
  TH1F * hEta2 = new TH1F("PassingEta", "muon 2 #eta", 60, -2.4, 2.4);
  TH1F * hPt1 = new TH1F("TotalPt", "muon 1 pt", 100, 0., 1000);
  TH1F * hPt2 = new TH1F("PassingPt", "muon 2 pt", 100, 0., 1000);

  TH1F * passingVsPhi = new TH1F("passingVsPhi", "tracks found vs #phi", 60, -3.14, 3.14);
  TH1F * totalVsPhi = new TH1F("totalVsPhi", "cosmics found vs #phi (filled twice)", 60, -3.14, 3.14);
  TH1F * effVsPhi = (TH1F*)passingVsPhi->Clone("effVsPhi");

  TH1F * passingVsEta = new TH1F("passingVsEta", "tracks found vs #eta", nBins, -2.5, 2.5);
  TH1F * totalVsEta = new TH1F("totalVsEta", "cosmics found vs #eta (filled twice)", nBins, -2.5, 2.5);
  TH1F * effVsEta = (TH1F*)passingVsEta->Clone("effVsEta");

  TH1F * passingVsPt = new TH1F("passingVsPt", "tracks found vs p_{T}", nBins, 0., 300.);
  TH1F * totalVsPt = new TH1F("totalVsPt", "cosmics found vs p_{T} (filled twice)", nBins, 0., 300.);
  TH1F * effVsPt = (TH1F*)passingVsPt->Clone("effVsPt");


  // Timing
  TH1F * nDof = new TH1F("nDof", "nDof", 100, 0., 100.);
  TH1F * timeAtIpInOut = new TH1F("timeAtIpInOut", "timeAtIpInOut", 200, -100., 100.);
  TH2F * timeAtIpInOutVsPhi = new TH2F("timeAtIpInOutVsPhi", "timeAtIpInOutVsPhi", 200, -100., 100., 60, -3.14, 3.14);


  TH1F * passingVsValidHits = new TH1F("passingVsValidHits", "tracks found vs valid hits", 6, 0., 6.);
  TH1F * totalVsValidHits = new TH1F("totalVsValidHits", "cosmics found vs valid hits (filled twice)", 6, 0., 6.);
  // TH1F * effVsValidHits = (TH1F*)passingVsValidHits->Clone("effVsValidHits");

  TH1F * passingVsDz = new TH1F("passingVsDz", "tracks found vs |d_{z}|", nBinsZ0, 0., 500.);
  //  TH1F * passingVsDz = new TH1F("passingVsDz", "tracks found vs |d_{z}|", binnum, manualBins);
  TH1F * totalVsDz = new TH1F("totalVsDz", "cosmics found vs |d_{z}| (filled twice)", nBinsZ0, 0., 500.);
  //  TH1F * totalVsDz = new TH1F("totalVsDz", "cosmics found vs |d_{z}| (filled twice)", binnum, manualBins);
  TH1F * effVsDz = (TH1F*)passingVsDz->Clone("effVsDz");

  TH1F * passingVsChi2 = new TH1F("passingVsChi2", "tracks found vs #chi^{2}/ndof", 250, 0., 50.);
  TH1F * totalVsChi2 = new TH1F("totalVsChi2", "cosmics found vs #chi^{2}/ndof (filled twice)", 250, 0., 50.);
  TH1F * passingVsChi2_noWeight = new TH1F("passingVsChi2_noWeight", "tracks found vs #chi^{2}/ndof", 250, 0., 50.);
  TH1F * totalVsChi2_noWeight = new TH1F("totalVsChi2_noWeight", "cosmics found vs #chi^{2}/ndof (filled twice)", 250, 0., 50.);
  // TH1F * effVsChi2 = (TH1F*)passingVsChi2->Clone("effVsChi2");

  TH2F * hEtaPhi_noWeight = new TH2F("hEtaPhi_noWeight", "etaPhi_noWeight", 100, -1., 1., 63, -3.15, 3.15);
  TH2F * hEtaPhi = new TH2F("hEtaPhi", "etaPhi", 100, -1., 1., 63, -3.15, 3.15);

  TH2F * hEtaD0_noWeight = new TH2F("hEtaD0_noWeight", "etaD0_noWeight", 100, -1., 1., 100, 0, 500);
  TH2F * hEtaD0 = new TH2F("hEtaD0", "etaD0", 100, -1., 1., 100, 0, 500);
  TH2F * hEtaDz_noWeight = new TH2F("hEtaDz_noWeight", "etaDz_noWeight", 100, -1., 1., 100, 0, 500);
  TH2F * hEtaDz = new TH2F("hEtaDz", "etaDz", 100, -1., 1., 100, 0, 500);

  TH2F * hPhiD0_noWeight = new TH2F("hPhiD0_noWeight", "phiD0_noWeight", 63, -3.15, 3.15, 100, 0, 500);
  TH2F * hPhiD0 = new TH2F("hPhiD0", "phiD0", 63, -3.15, 3.15, 100, 0, 500);
  TH2F * hPhiDz_noWeight = new TH2F("hPhiDz_noWeight", "phiDz_noWeight", 63, -3.15, 3.15, 100, 0, 500);
  TH2F * hPhiDz = new TH2F("hPhiDz", "phiDz", 63, -3.15, 3.15, 100, 0, 500);

  TH2F * hEtaPhiHalf_noWeight = new TH2F("hEtaPhiHalf_noWeight", "etaPhi half", 100, -1., 1., 63, -3.15, 3.15);
  TH2F * hEtaPhiHalf = new TH2F("hEtaPhiHalf", "etaPhi half", 100, -1., 1., 63, -3.15, 3.15);

  TH2F * validHitsVsEtaAll = new TH2F("validHitsVsEtaAll", "validHitsVsEtaAll", 5, 0., 5., 20, -2., 2.);
  TH2F * validHitsVsEtaAfterSel = new TH2F("validHitsVsEtaAfterSel", "validHitsVsEtaAfterSel", 5, 0., 5., 20, -2., 2.);

  TH2F * totalD0errVsPt = new TH2F("totalD0errVsPt", "totalD0errVsPt", nBins, 0., 300., nBins, 0., 100.);
  TH2F * totalDzerrVsPt = new TH2F("totalDzerrVsPt", "totalDzerrVsPt", nBins, 0., 300., nBins, 0., 100.);
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

  // --------- //
  // Main loop //
  // --------- //
  Long64_t nbytes = 0, nb = 0;
  for (Long64_t jentry=0; jentry<nentries;jentry++) {
    Long64_t ientry = LoadTree(jentry);
    if (ientry < 0) break;
    nb = fChain->GetEntry(jentry);   nbytes += nb;

    if( jentry % 10000 == 0 ) {
      std::cout << "Analyzed " << jentry << " events" << std::endl;
    }


    // if( jentry > 1000000 ) break;


    if( tracks->size() == 0 ) continue;
    if( tracks->size() > 2 ) continue;

    std::vector<Track>::const_iterator it = tracks->begin();
    for( ; it != tracks->end(); ++it ) {

      float weight = 1.;
      // if( MC_ ) weight = weightHisto->GetBinContent(weightHisto->FindBin(it->normalizedChi2));
      // if( MC_ ) weight = weightHistoEtaPhi->GetBinContent(weightHisto->FindBin(it->eta, it->phi));

//       // Timing
//       nDof->Fill(it->nDof);
//       timeAtIpInOut->Fill(it->timeAtIpInOut, weight);
//       timeAtIpInOutVsPhi->Fill(it->timeAtIpInOut, it->phi, weight);


      hPhiAll->Fill(it->phi, weight);
      validHitsVsEtaAll->Fill(it->dtStationsWithValidHits+it->cscStationsWithValidHits, it->eta, weight);

      // if( it->pt > 50 || fabs(it->dz) < 10. || fabs(it->dxyError) < 10. || fabs(it->dzError) < 10.) {
      if( it->pt > 26 || fabs(it->dz) < 10. ) {
	hPhiAfterSel->Fill(it->phi, weight);
	validHitsVsEtaAfterSel->Fill(it->dtStationsWithValidHits+it->cscStationsWithValidHits, it->eta, weight);
      }

      if( !passMuonCut(&*it) ) continue;


      // No weight applied. This is used to compute the weight
      hEtaPhi_noWeight->Fill(it->eta, it->phi);
      hEtaPhi->Fill(it->eta, it->phi, weight);
      hEtaD0_noWeight->Fill(it->eta, it->dxy);
      hEtaD0->Fill(it->eta, it->dxy, weight);
      hEtaDz_noWeight->Fill(it->eta, it->dz);
      hEtaDz->Fill(it->eta, it->dz, weight);
      hPhiD0_noWeight->Fill(it->phi, it->dxy);
      hPhiD0->Fill(it->phi, it->dxy, weight);
      hPhiDz_noWeight->Fill(it->phi, it->dz);
      hPhiDz->Fill(it->phi, it->dz, weight);

      if( (!topBottom && (it->phi < 0 && it->phi > -TMath::Pi())) ||
  	  (topBottom && (it->phi > 0 && it->phi < TMath::Pi())) ) {


	// Timing
	nDof->Fill(it->nDof);
	timeAtIpInOut->Fill(it->timeAtIpInOut, weight);
	timeAtIpInOutVsPhi->Fill(it->timeAtIpInOut, it->phi, weight);


//       if( (!topBottom && (it->phi < -1 && it->phi > -2)) ||
// 	  (topBottom && (it->phi > 1 && it->phi < 2)) ) {
	// if( it->phi < 0 && it->phi > -TMath::Pi() ) {

	hEtaPhiHalf_noWeight->Fill(it->eta, it->phi);
	hEtaPhiHalf->Fill(it->eta, it->phi, weight);

	hPhi1->Fill(it->phi, weight);
	hEta1->Fill(it->eta, weight);
	hPt1->Fill(it->pt, weight);
	if( tracks->size() > 1 ) {
	  std::vector<Track>::const_iterator jt = tracks->begin();
	  for( ; jt != tracks->end(); ++jt ) {
	    if( jt->phi != it->phi ) {
	      if( (!topBottom && (jt->phi > 0 && jt->phi < TMath::Pi())) ||
		  (topBottom && (jt->phi < 0 && jt->phi > -TMath::Pi())) ) {
		if( passTrackCut( &*jt ) ) {
		  hPhi2->Fill(jt->phi, weight);
		  hEta2->Fill(jt->eta, weight);
		  hPt2->Fill(jt->pt, weight);
		  break;
		}
	      }
	    }
	  }
	}

	// Efficiency vs d0
	fillEff(fabs(it->dxy), totalVsD0, tracks, passingVsD0, topBottom, weight);
	fillEff(it->phi, totalVsPhi, tracks, passingVsPhi, topBottom, weight);
	fillEff(it->eta, totalVsEta, tracks, passingVsEta, topBottom, weight);
	fillEff(it->pt, totalVsPt, tracks, passingVsPt, topBottom, weight);
	fillEff(it->dtStationsWithValidHits+it->cscStationsWithValidHits, totalVsValidHits, tracks, passingVsValidHits, topBottom, weight);
	fillEff(fabs(it->dz), totalVsDz, tracks, passingVsDz, topBottom, weight);
	fillEff(it->normalizedChi2, totalVsChi2_noWeight, tracks, passingVsChi2_noWeight, topBottom, 1.);
	fillEff(it->normalizedChi2, totalVsChi2, tracks, passingVsChi2, topBottom, weight);
    
	totalD0errVsPt->Fill(it->pt,it->dxyError, weight);
	totalDzerrVsPt->Fill(it->pt,it->dzError, weight);
	totalD0VsDz->Fill(fabs(it->dz),fabs(it->dxy), weight);
	// totalD0VsPt->Fill((*muons)[0].pt,(fabs((*muons)[0].dxy)-fabs((*genParticles)[0].dxy))/fabs((*genParticles)[0].dxy) );
	// totalD0VsPt->Fill((*muons)[0].pt,fabs((*muons)[0].dxy));

	etaRelError->Fill(it->etaError/fabs(it->eta), weight);
	dxyRelError->Fill(it->dxyError/fabs(it->dxy), weight);
	dzRelError->Fill(it->dzError/fabs(it->dz), weight);

	if( MC_ ) {

	  fillEff(fabs((*genParticles)[0].dxy), totalVsGenD0, tracks, passingVsGenD0, topBottom, weight);
	  fillEff((*genParticles)[0].phi, totalVsGenPhi, tracks, passingVsGenPhi, topBottom, weight);
	  fillEff((*genParticles)[0].eta, totalVsGenEta, tracks, passingVsGenEta, topBottom, weight);
	  fillEff((*genParticles)[0].pt, totalVsGenPt, tracks, passingVsGenPt, topBottom, weight);
	  fillEff(fabs((*genParticles)[0].dz), totalVsGenDz, tracks, passingVsGenDz, topBottom, weight);
	}
	/*
	// Apply also a dxy cut for the efficiency vs eta
	if( (*muons)[0].dxy > 5. ) continue;
	// Efficiency vs eta
	fillEff((*muons)[0].eta, totalVsEta, tracks, passingVsEta, weight);
	if( MC_ ) {
	fillEff((*genParticles)[0].eta, totalVsGenEta, tracks, passingVsGenEta, weight);
	}
	*/
	break;
      }
    }
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

// #ifndef __CINT__
// int main()
// {
//   CosmicMuonAnalyzer c;
//   return 0;
// }
// #endif
