//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Mar 30 14:32:13 2012 by ROOT version 5.27/06b
// from TTree T/MuonsTree
// found on file: cosmicMuons1Leg.root
//////////////////////////////////////////////////////////

#ifndef CosmicMuonAnalyzer_h
#define CosmicMuonAnalyzer_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <vector>

#include "../../../../RootTreeProducers/interface/Track.h"
#include "../../../../RootTreeProducers/interface/GenParticle.h"
#ifdef __CINT__
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;
#pragma link C++ class Track+;
#pragma link C++ class std::vector<Track>+;
#pragma link C++ class GenParticle+;
#pragma link C++ class std::vector<GenParticle>+;
#endif

class CosmicMuonAnalyzer {
public :
  // TTree          *fChain;   //!pointer to the analyzed TTree or TChain
  TChain          *fChain;   //!pointer to the analyzed TTree or TChain
  Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   UInt_t          event;
   UInt_t          run;
   std::vector<Track>   *tracks;
   std::vector<Track>   *muons;
   std::vector<GenParticle> *genParticles;

   // List of branches
   TBranch        *b_event;   //!
   TBranch        *b_run;   //!
   TBranch        *b_tracks;   //!
   TBranch        *b_muons;   //!
   TBranch        *b_genParticles;   //!

   bool MC_;

   CosmicMuonAnalyzer(const bool MC = false);
   virtual ~CosmicMuonAnalyzer();
   // virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init();
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

// #ifdef CosmicMuonAnalyzer_cxx
// #endif // #ifdef CosmicMuonAnalyzer_cxx
