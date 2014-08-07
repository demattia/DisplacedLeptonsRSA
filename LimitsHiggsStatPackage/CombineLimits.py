import os
import subprocess
from math import sqrt

baseDirTk = "counting_job_Tk_Bayesian"
baseDirRSA = "counting_job_RSA_Bayesian"
baseDirCombined = "counting_job_Combined_Bayesian"
from itertools import izip

def combine_efficiencies(file_RSA, file_Tk):
    output_file_name = file_RSA.split("_RSA.py")[0]+"_Combined.py"
    output_file = open(output_file_name, "w")

    relLineCounter = 0
    found = False
    foundControl = False
    foundRel = False
    eff1 = []
    eff2 = []
    for line1, line2 in izip(open(file_RSA), open(file_Tk)):
    
        output_line = line1

        if line1.find("s.setEffiRelErrs") != -1:
            foundRel = True
        if line1.find("s.setEffisInControl") != -1:
            relLineCounter = 0
            foundControl = True
            print eff1
            print eff2
            eff1 = []
            eff2 = []
            foundRel = False
        if line1.find("s.setEffis ") != -1:
            foundControl = False
    
        if line1.find("s.setEffiRelErrs") != -1 or line1.find("samples.append(s)") != -1:
            found = False
    
        # Replace the efficiencies with the sum
        if found == True and line1.find("s.setEffis ") == -1:
            # print line1
            # print line2
            new_string = ""
            for value_string1, value_string2 in izip(line1.split(','), line2.split(',')):
                if value_string1.strip() != "":
                    # print value_string1.strip().strip(' ] )')
                    # print value_string2.strip().strip(' ] )')
                    value1 = float(value_string1.strip().strip(' ] )'))
                    value2 = float(value_string2.strip().strip(' ] )'))
                    if not foundControl:
                        eff1.append(value1)
                        eff2.append(value2)
                    value = value1+value2
                    # print '%.6f' % value1, '%.6f' % value2, '%.6f' % value
                    new_string += " "+'%.6f' % value
                    if value_string1.find(' ] )') != -1:
                        new_string += " ] )"
                    else:
                        new_string += " , "
            output_line = new_string+"\n"

        # Replace the relative errors on the efficiencies with the weighted average
        if foundRel == True and line1.find("s.setEffiRelErrs") == -1:
            new_string = ""
            for value_string1, value_string2 in izip(line1.split(','), line2.split(',')):
                if value_string1.strip() != "":
                    value1 = float(value_string1.strip().strip(' ] )'))
                    value2 = float(value_string2.strip().strip(' ] )'))
                    value = value1
                    if eff1[relLineCounter] != 0 or eff2[relLineCounter] != 0:
                        # print value1, eff1[relLineCounter], value2, eff2[relLineCounter]
                        value = sqrt((value1*eff1[relLineCounter])**2+(value2*eff2[relLineCounter])**2)/(eff1[relLineCounter]+eff2[relLineCounter])
                        # print "value =", value
                    new_string += " "+'%.6f' % value
                    if value_string1.find(' ] )') != -1:
                        new_string += " ] )"
                    else:
                        new_string += " , "
                    relLineCounter += 1
            output_line = new_string+"\n"

    
        if line1.find("s = SignalSampleInfo") != -1:
            masses1 = line1.split('(')[1].split(',')
            masses2 = line2.split('(')[1].split(',')
            if masses1[0] != masses2[0] or masses1[1] != masses2[1]:
                print "Efficiency files for RSA and Tk are inconsistent. Exiting"
                sys.exit(1)
        if line1.find("s.setEffis") != -1:
            found = True
    
        output_file.write(output_line)


# Combine the efficiencies and efficiencies over acceptance
combine_efficiencies("SignalSampleInfoEffi_RSA.py", "SignalSampleInfoEffi_Tk.py")
# NOTE: the efficiency over acceptances can only be combined if the acceptance definition is the same
# It is not the case at this moment. The Tk files should be reproduced with the same acceptance definition
# as the RSA ones.
combine_efficiencies("SignalSampleInfoEffiOverAcc_RSA.py", "SignalSampleInfoEffiOverAcc_Tk.py")


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
        # print "combineCards.py "+baseDirTk+"/"+subDirName+"/combine.txt "+baseDirRSA+"/"+subDirName+"/combine.txt > "+baseDirCombined+"/"+subDirName+"/combine.txt"
        os.system("combineCards.py "+baseDirTk+"/"+subDirName+"/combine_mod.txt "+baseDirRSA+"/"+subDirName+"/combine_mod.txt > "+baseDirCombined+"/"+subDirName+"/combine.txt")
    else:
        os.system("cp "+dir_to_use+"/combine.txt "+baseDirCombined+"/"+subDirName+"/")
 
    cmd = "$CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/scripts/text2workspace.py "+baseDirCombined+"/"+subDirName+"/combine.txt -b -o "+baseDirCombined+"/"+subDirName+"/combine.root"
    istat = subprocess.call(cmd, shell=True)
    if istat != 0:
        sys.exit("ERROR: whilst executing %s" %cmd)
