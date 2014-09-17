import ROOT
from ROOT import TFile

cut = 3

backgroundL90 = 0.
backgroundG90 = 0.

print "running with cut value:", cut


fileNames = []

fileNames.append("CombinedFiles/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_combined_2saMu.root")
fileNames.append("CombinedFiles/QCDenriched_combined_2saMu.root")
fileNames.append("CombinedFiles/TTJets_combined_2saMu.root")
fileNames.append("CombinedFiles/WJets_combined_2saMu.root")
# fileNames.append("CombinedFiles/Tau_combined_2saMu.root")
fileNames.append("CombinedFiles/WW_combined_2saMu.root")
fileNames.append("CombinedFiles/WZ_combined_2saMu.root")
fileNames.append("CombinedFiles/ZZ_combined_2saMu.root")
fileNames.append("CombinedFiles/DYJets_combined_2saMu.root")


def getNumber(fileName):
    global backgroundG90
    global backgroundL90
    inputFile = TFile(fileName)
    factor = 20000.
    if fileName.find("HTo2") != -1:
        factor = 1.
    if fileName.find("Data") == -1:
        hD0L90 = inputFile.Get("minLeptonAbsD0Sig_bestCand_deltaPhiL90_removedLifetimeCollCuts")
        integralL90 = hD0L90.Integral(hD0L90.FindBin(cut), hD0L90.GetNbinsX()+1)*factor
        print "events passing the cut in the signal region =", integralL90
        if fileName.find("HTo2") == -1:
            backgroundL90 += integralL90
    hD0G90 = inputFile.Get("minLeptonAbsD0Sig_bestCand_deltaPhiG90_removedLifetimeCollCuts")
    integralG90 = hD0G90.Integral(hD0G90.FindBin(cut), hD0G90.GetNbinsX()+1)*factor
    print "events passing the cut in the control region =", integralG90
    if fileName.find("HTo2") == -1 and fileName.find("Data") == -1:
        backgroundG90 += integralG90

for fileName in fileNames:
    print fileName
    getNumber(fileName)

print "background in the signal region =", backgroundL90
print "background in the control region =", backgroundG90
