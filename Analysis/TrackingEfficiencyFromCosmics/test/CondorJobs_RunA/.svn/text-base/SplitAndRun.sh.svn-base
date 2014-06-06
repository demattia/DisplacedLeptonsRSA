#!/bin/bash

cmsswDir="/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/CMSDAS2013/CMSSW_5_3_6/src/"
inputFiles=""
dcacheDirIn="/pnfs/cms/WAX/11/store/user/yangf/Cosmics2012-RunC/"
#dcacheDirIn="/pnfs/cms/WAX/resilient/zhenhu/Cosmics2012/test/"

j=0
for files in `ls $dcacheDirIn | grep reco_RAW2DIGI_L1Reco_RECO`
do 
	inputFiles=$files;
	echo $inputFiles;
	jobNb=${j};
	let j=${j}+1;
	cmsCFG="CosmicMuonTreeWriter_cfg_${jobNb}.py"
	scriptName="Run_${jobNb}.csh";
	condorScriptName="runOnCondor_${jobNb}";
	cat CosmicMuonTreeWriter_cfg.py | sed "s-INPUTFILES-${inputFiles}-" | sed "s/NUMBER/${jobNb}/" > ${cmsCFG}
	cat Run.csh | sed "s-FILENAME-${cmsCFG}-" | sed "s-CMSSWDIR-${cmsswDir}-" > ${scriptName};
	chmod +x ${scriptName}
	cat runOnCondor | sed "s/SCRIPT/${scriptName}/" | sed "s/CFG/${cmsCFG}/"> ${condorScriptName}
	condor_submit ${condorScriptName}
done
