import os
import subprocess
from math import sqrt
from SignalSampleInfo_RSA import *
from SignalSampleInfo_Tk import *

# NOTE: the efficiency over acceptances can only be combined if the acceptance definition is the same
# It is not the case at this moment. The Tk files should be reproduced with the same acceptance definition
# as the RSA ones.

baseDirTk = "counting_job_Tk_Bayesian_neutralino"
baseDirRSA = "counting_job_RSA_Bayesian_neutralino"
baseDirCombined = "counting_job_Combined_Bayesian_neutralino"
from itertools import izip

samples_RSA = getSignalSampleInfoRSA()
samples_Tk = getSignalSampleInfoTk()
samples_Combined = getSignalSampleInfoTk()

output_file_name = "SignalSampleInfoEffi_Combined.py"
output_file = open(output_file_name, "w")
output_file_name_acc = "SignalSampleInfoEffiOverAcc_Combined.py"
output_file_acc = open(output_file_name_acc, "w")

for sIndexRSA, sRSA in enumerate(samples_RSA):
    print "MASSES AND ACCEPTANCE:", sRSA.MH, sRSA.MX, sRSA.acceptance
    for sIndexTk, sTk in enumerate(samples_Tk):
        if sRSA.MH == sTk.MH and sRSA.MX == sTk.MX:
            for ctauRSAIndex, ctauRSA in enumerate(sRSA.ctaus):
                if sRSA.acceptance != sTk.acceptance:
                    continue
                # print ctauRSA, sRSA.ctauScales[ctauRSAIndex]
                i = -1
                for ctauTkIndex, ctauTk in enumerate(sTk.ctaus):
                    if ctauTk == ctauRSA:
                        i = ctauTkIndex
                        break
                if i != -1:
                    # print ctauRSA, sTk.ctaus[i]
                    eff1 = sTk.effis['Muons'][i]
                    eff2 = sRSA.effis['Muons'][ctauRSAIndex]
                    # print "effs =", eff1, eff2
                    value1 = sTk.effi_relerrs['Muons'][i]
                    value2 = sRSA.effi_relerrs['Muons'][ctauRSAIndex]
                    samples_Combined[sIndexTk].effis['Muons'][i] = eff1 + eff2
                    samples_Combined[sIndexTk].effi_relerrs['Muons'][i] =\
                        sqrt((value1*eff1)**2+(value2*eff2)**2)/(eff1+eff2)
                    samples_Combined[sIndexTk].effis_control['Muons'][i] =\
                        sTk.effis_control['Muons'][i] + sRSA.effis_control['Muons'][ctauRSAIndex]
                else:
                    # print ctauRSA, sTk.ctaus
                    samples_Combined[sIndexTk].ctaus.append(ctauRSA)
                    samples_Combined[sIndexTk].ctauScales.append(sRSA.ctauScales[ctauRSAIndex]*10)
                    samples_Combined[sIndexTk].effis['Muons'].append(sRSA.effis['Muons'][ctauRSAIndex])
                    samples_Combined[sIndexTk].effi_relerrs['Muons'].append(sRSA.effi_relerrs['Muons'][ctauRSAIndex])
                    samples_Combined[sIndexTk].effis_control['Muons'].append(sRSA.effis_control['Muons'][ctauRSAIndex])
                    # print sRSA.ctauScales[ctauRSAIndex], samples_Combined[sIndexTk].effis

for sCombined in samples_Combined:
    of = output_file
    if sCombined.acceptance == 2:
        of = output_file_acc
    line = "s = SignalSampleInfo("+str(sCombined.MH)+","+str(sCombined.MX)+","+\
           str(sCombined.ctau0)+","+str(sCombined.acceptance)+")\n"
    of.write(line)
    line = "s.setCtauScales ( "+str(sCombined.ctauScales)+" )\n"
    of.write(line)
    line = "s.setWidths ( \"Muons\", [] )\n"
    of.write(line)
    line = "s.setEffis ( \"Muons\", "+str(sCombined.effis["Muons"])+" )\n"
    of.write(line)
    line = "s.setEffiRelErrs ( \"Muons\", "+str(sCombined.effi_relerrs["Muons"])+" )\n"
    of.write(line)
    line = "s.setEffisInControl ( \"Muons\", "+str(sCombined.effis_control["Muons"])+" )\n"
    of.write(line)
    line = "samples.append(s)\n"
    of.write(line)
    of.write("#\n")

output_file.close()


# This creates the combined files for the limit jobs
# --------------------------------------------------
dirs_RSA = set(os.listdir(baseDirRSA))
dirs_Tk = set(os.listdir(baseDirTk))

# Take the union of the dir list for both
all_dirs = dirs_RSA.union(dirs_Tk)

multicrab_file = open(baseDirCombined+"/multicrab.cfg", "w")

multicrab_file.write("""
[MULTICRAB]
cfg=counting_job_Combined_Bayesian/Muons_125_20_1000.0/TestGrid.cfg

[COMMON]
USER.ui_working_dir = counting_job_output_Combined_Bayesian 

""")


def modifyCard(inputFilePathAndName, outputFilePathAndName):
    combine_mod = open(outputFilePathAndName, "w")
    for line in open(inputFilePathAndName):
        if line.find("rate") != -1:
            combine_mod.write(line.replace("1", "0.5"))
        else:
            combine_mod.write(line)


for subDirName in all_dirs:
    if subDirName.find("multicrab") != -1:
        continue

    print subDirName

    multicrab_file.write("""
["""+subDirName+"""] 
USER.script_exe = counting_job_Combined_Bayesian/"""+subDirName+"""/TestGrid.sh 
USER.additional_input_files = combine, counting_job_Combined_Bayesian/"""+subDirName+"""/combine.root 
CMSSW.output_file = higgsCombineTest.MarkovChainMC.mH0.root, higgsCombineTest.MarkovChainMC.mH0.123456.root, combine.root 

""")

    os.system("mkdir -p "+baseDirCombined+"/"+subDirName)
 
    dir_Tk_exists = os.path.isdir(baseDirTk+"/"+subDirName)
    dir_RSA_exists = os.path.isdir(baseDirRSA+"/"+subDirName)
 
    dir_to_use = baseDirTk+"/"+subDirName
    if not dir_Tk_exists:
        dir_to_use = baseDirRSA+"/"+subDirName
        os.system("cat "+dir_to_use+"/TestGrid.cfg | sed s@_RSA@_Combined@g > "+baseDirCombined+"/"+subDirName+"/TestGrid.cfg")
    else:
        os.system("cat "+dir_to_use+"/TestGrid.cfg | sed s@_Tk@_Combined@g > "+baseDirCombined+"/"+subDirName+"/TestGrid.cfg")
 
    # print "cat "+baseDirTk+"/"+subDirName+"/TestGrid.cfg"
    os.system("cp "+dir_to_use+"/TestGrid.sh "+baseDirCombined+"/"+subDirName+"/TestGrid.sh")
 
    if dir_Tk_exists and dir_RSA_exists:
        modifyCard(baseDirTk+"/"+subDirName+"/combine.txt", baseDirTk+"/"+subDirName+"/combine_mod.txt")
        modifyCard(baseDirRSA+"/"+subDirName+"/combine.txt", baseDirRSA+"/"+subDirName+"/combine_mod.txt")
        print "combineCards.py "+baseDirTk+"/"+subDirName+"/combine.txt "+baseDirRSA+"/"+subDirName+"/combine.txt > "+baseDirCombined+"/"+subDirName+"/combine.txt"
        os.system("combineCards.py "+baseDirTk+"/"+subDirName+"/combine_mod.txt "+baseDirRSA+"/"+subDirName+"/combine_mod.txt > "+baseDirCombined+"/"+subDirName+"/combine.txt")
    else:
        os.system("cp "+dir_to_use+"/combine.txt "+baseDirCombined+"/"+subDirName+"/")
 
    cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/scripts/text2workspace.py "+baseDirCombined+"/"+subDirName+"/combine.txt -b -o "+baseDirCombined+"/"+subDirName+"/combine.root"
    istat = subprocess.call(cmd, shell=True)
    if istat != 0:
        sys.exit("ERROR: whilst executing %s" %cmd)

