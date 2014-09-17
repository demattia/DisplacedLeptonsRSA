#ifndef FILESANDWEIGHTS_H
#define FILESANDWEIGHTS_H

#include <map>
#include <TString.h>

std::map<TString, double> filesAndWeightsMap( bool electrons )
{
  // The weights are the cross sections in pb. The number of processed events is read from a histograms in the tree root file.
  // Give data a weight of -1, so we know it is data

  // Files and weights map
  std::map<TString, double> fw;

  // Signal

  //  // mH = 1000 GeV
  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_analysis_20140403"] = 0.5;

//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_analysis_20140403"] = 0.5;
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150_analysis_20140403"] = 0.5;
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH1000_MFF50_CTau4To400_analysis_20140403"] = 0.5;

//  // mH = 400 GeV
//
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH400_MFF150_CTau40To4000_analysis_20140403"] = 0.1;
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH400_MFF50_CTau8To800_analysis_20140403"] = 0.1;
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH400_MFF20_CTau4To400_analysis_20140403"] = 0.1;
//  // mH = 200 GeV
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000_analysis_20140403"] = 0.1;
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH200_MFF20_CTau7To700_analysis_20140403"] = 0.1;
//
//  // mH = 125 GeV
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH125_MFF50_CTau50To5000_analysis_20140403"] = 0.1;
//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_analysis_20140403"] = 0.1;
//
//  // Chi0
  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Chi0ToNuLL_MSquark350_MChi148_analysis_20140403"] = 0.1;

//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Chi0ToNuLL_MSquark1500_MChi494_analysis_20140403"] = 0.1;

  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Chi0ToNuLL_MSquark120_MChi48_analysis_20140403"] = 0.1;

//  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Chi0ToNuLL_MSquark1000_MChi148_analysis_20140403"] = 0.1;

    // H
//  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/Displaced_new4/CMSSW_5_3_8/src/workdirs/LongLivedTo2F_M_1000_CTau350_analysis_20140122"] = 0.1;
//  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/Displaced_new4/CMSSW_5_3_8/src/workdirs/LongLivedTo2F_M_500_CTau350_analysis_20140122"] = 0.1;
//  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/Displaced_new4/CMSSW_5_3_8/src/workdirs/LongLivedTo2F_M_350_CTau350_analysis_20140122"] = 0.1;
//  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/Displaced_new4/CMSSW_5_3_8/src/workdirs/LongLivedTo2F_M_200_CTau350_analysis_20140122"] = 0.1;
//  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/Displaced_new4/CMSSW_5_3_8/src/workdirs/LongLivedTo2F_M_100_CTau350_analysis_20140122"] = 0.1;
//  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/Displaced_new4/CMSSW_5_3_8/src/workdirs/LongLivedTo2F_M_50_CTau350_analysis_20140122"] = 0.1;


  // Vector bosons


  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/WW_analysis_20140403"] = 54.8;
  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/WZ_analysis_20140403"] = 33.2;
  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/ZZ_analysis_20140403"] = 17.6;
  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/WJetsToLNu_analysis_20140403"] = 36257.2;

  // TTbar

  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/TTJets_FullLept_analysis_20140403"] = 24.77;

  // DY JETS
  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/DYJets10_analysis_20140403"] = 12471;
  fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/DYJets50_analysis_20140403"] = 3503.7;


  if (!electrons)
  {
    // QCD mu
    // fw["/uscmst1b_scratch/lpc1/3DayLifetime/demattia/CMSSW_5_3_8/src/workdirs/QCDmu15_analysis_20140331"] = 2738580.0;
    // fw["/uscmst1b_scratch/lpc1/3DayLifetime/demattia/CMSSW_5_3_8/src/workdirs/QCDmu20_analysis_20140331"] = 134680.0;
    fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/QCDmu15_analysis_20140403"] = 2738580.0;
    fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/QCDmu20_analysis_20140403"] = 134680.0;


    // Data
    fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Data_Mu_Run2012A22Jan_analysis_20140331"] = -1;
    fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Data_Mu_Run2012B22Jan_analysis_20140402_0"] = -1;
    fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Data_Mu_Run2012C22Jan_analysis_20140402_0"] = -1;
    fw["/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Trees/Data_Mu_Run2012D22Jan_analysis_20140402_0"] = -1;
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/PickEvents/Data22Jan_Mu_Run2012D"] = -1;
  }
  else
  {
  }
  return fw;
}

#endif
