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

//  bool useMET = true;
  bool useMET = false;

  if (useMET){
  // Signal

  //  // mH = 1000 GeV

  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_analysis_20140627"] = 1;

  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF50_CTau4To400_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150_analysis_20140627"] = 1;

//  // mH = 400 GeV
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF150_CTau40To4000_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF50_CTau8To800_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF20_CTau4To400_analysis_20140627"] = 1;

//  // mH = 200 GeV
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH200_MFF20_CTau7To700_analysis_20140627"] = 1;

//  // mH = 125 GeV
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH125_MFF50_CTau50To5000_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_analysis_20140627"] = 1;

//  // Chi0
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark1500_MChi494_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark1000_MChi148_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark350_MChi148_analysis_20140627"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark120_MChi48_analysis_20140627"] = 1;
  // Vector bosons

  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/ZZ_analysis_20140627"] = 17.6;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/WZ_analysis_20140627"] = 33.2;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/WW_analysis_20140627"] = 54.8;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/WJetsToLNu_analysis_20140627"] = 36257.2;
  // TTbar

  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/TTJets_FullLept_analysis_20140627"] = 24.77;

  // DY JETS
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/DYJets10_analysis_20140627"] = 12471;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/DYJets50_analysis_20140627"] = 3503.7;
 }

  else {
// Signal

  //  // mH = 1000 GeV

//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF350_CTau350To35000_analysis_20140805"] = 1;

//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF150_CTau100To10000_analysis_20140805"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF50_CTau40To4000_analysis_20140805"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF20_CTau15To1500_analysis_20140805"] = 1;

//
//  // mH = 400 GeV
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF150_CTau400To40000_analysis_20140805"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF50_CTau80To8000_analysis_20140805"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF20_CTau40To4000_analysis_20140805"] = 1;
//
//  // mH = 200 GeV
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH200_MFF50_CTau200To20000_analysis_20140805"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH200_MFF20_CTau70To7000_analysis_20140805"] = 1;
//
//  // mH = 125 GeV
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH125_MFF50_CTau500To50000_analysis_20140819"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH125_MFF20_CTau130To13000_analysis_20140805"] = 1;

//
//  // Chi0

//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark1000_MChi148_analysis_20140717"] = 1;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark1500_MChi494_analysis_20140822"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark350_MChi148_analysis_20140717"] = 1;
//  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark120_MChi48_analysis_20140717"] = 1;



  // Vector bosons

  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/ZZ_analysis_20140601"] = 17.6;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/WZ_analysis_20140601"] = 33.2;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/WW_analysis_20140601"] = 54.8;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/WJetsToLNu_analysis_20140601"] = 36257.2;

// TTbar

  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/TTJets_FullLept_analysis_20140601"] = 24.77;

  // DY JETS
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/DYJets10_analysis_20140601"] = 12471;
  fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/DYJets50_analysis_20140601"] = 3503.7;
  
  }

  if (!electrons && useMET)
  {
    // QCD mu
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/QCDmu15_analysis_20140627"] = 2738580.0;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/QCDmu20_analysis_20140627"] = 134680.0;


    // Data
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012A22Jan_analysis_20140627"] = -1;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012B22Jan_analysis_20140627"] = -1;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012C22Jan_analysis_20140627"] = -1;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012D22Jan_analysis_20140627"] = -1;
   //Cosmics

//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsRunA_analysis_20140603"] = -1;
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsRunB_analysis_20140603"] = -1;
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsRunC_analysis_20140603"] = -1;

      
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsCRAFT_186785_186996_analysis_20140618"] = -1;
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsCRAFT_187461_187468_and_187469_189146_analysis_20140618"] = -1;

  }
  else if (!electrons && !useMET)
  {
      // QCD mu
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/QCDmu15_analysis_20140601"] = 2738580.0;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/QCDmu20_analysis_20140601"] = 134680.0;


    // Data
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012A22Jan_analysis_20140531"] = -1;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012B22Jan_analysis_20140531"] = -1;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012C22Jan_analysis_20140531"] = -1;
    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012D22Jan_analysis_20140531"] = -1;

   //Cosmics

//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsRunA_analysis_20140603"] = -1;
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsRunB_analysis_20140603"] = -1;
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsRunC_analysis_20140603"] = -1;


//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsCRAFT_186785_186996_analysis_20140602"] = -1;
//    fw["/uscms_data/d3/msolmaz/myworkingspace/phys_698_spring_2014/CMSSW_5_3_8/src/workdirs/cosmicsCRAFT_187461_187468_and_187469_189146_analysis_20140602"] = -1;
  }
  else{}
  return fw;
}

#endif
