import ROOT
from ROOT import TFile
ROOT.gROOT.SetBatch(True)
gen_all = 13724



fileNames = []

fileNames.append("CombinedFiles_minstation_3/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/QCDenriched_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/TTJets_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/WJets_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/Tau_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/WW_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/WZ_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/ZZ_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/DYJets_combined_2saMu.root")
fileNames.append("CombinedFiles_minstation_3/Data22Jan_combined_2saMu.root")

def getNumber(fileName, x, y, z):
    global backgroundG90 
    global backgroundL90
    global signal_eff 
    global dataG90 
#    global dataL90 
    global signalL90 
    global signalG90 

    inputFile = TFile(fileName)
    hD0L90 = inputFile.Get("nMinus3_3D_finalCollCuts")
    binglobal = hD0L90.FindBin(x,y,z)
    binx,biny,binz = ROOT.Long(), ROOT.Long(), ROOT.Long()
    hD0L90.GetBinXYZ(binglobal,binx,biny,binz)
    integralL90 = hD0L90.Integral(binx, hD0L90.GetNbinsX()+1, biny, hD0L90.GetNbinsY()+1, binz, hD0L90.GetNbinsZ()+1)
    hD0G90 = inputFile.Get("nMinus3_3D_controlCollCuts")
    integralG90 = hD0G90.Integral(binx, hD0G90.GetNbinsX()+1, biny, hD0G90.GetNbinsY()+1, binz, hD0G90.GetNbinsZ()+1)

    factor = 20531.99
    if fileName.find("HTo2") != -1:
        factor = 2

    if fileName.find("Data") == -1:
        integralL90 = integralL90 * factor
        integralG90 = integralG90 * factor
        if fileName.find("HTo2") == -1:
            backgroundL90 += integralL90
            backgroundG90 += integralG90
        else :
            signalL90 = integralL90
            signalG90 = integralG90
            signal_eff = integralL90/gen_all
    else :         
        dataG90 = integralG90
#        dataL90 = integralL90

data_G90_2D={}
background_G90_2D={}
signal_eff_2D ={}

outputfile = ROOT.TFile("cut_optimization_minstation_3.root","RECREATE")
canvas1 = ROOT.TCanvas("c1","c1",500,1000)
canvas1.Divide(5,10)
canvas2 = ROOT.TCanvas("c2","c2",500,1000)
canvas2.Divide(5,10)
canvas3 = ROOT.TCanvas("c3","c3",500,1000)
canvas3.Divide(5,10)

for x in range(0,50):
    cut_cos = -1.0 + x*0.01
    data_G90_2D[x] = ROOT.TH2F("data_G90_2D_"+str(x), "data_G90_2D"+str(x), 20, 0, 20, 40, 0, 40)
    background_G90_2D[x] = ROOT.TH2F("background_G90_2D_"+str(x), "background_G90_2D"+str(x), 20, 0, 20, 40, 0, 40)
    signal_eff_2D[x] = ROOT.TH2F("signal_eff_2D_"+str(x), "signal_eff_2D"+str(x), 20, 0, 20, 40, 0, 40)
    for y in range(0,20):
        for z in range(0,40):
            print "************************************************************************************************************"
            print "For cosine >= ", cut_cos, ", for d0 Significance >=  ", y, ", for Lxy Significance >= ", z, ": "
            backgroundL90 = 0.
            backgroundG90 = 0.
            signal_eff = 0
            dataG90 = 0
#           dataL90 = 0
            signalL90 = 0
            signalG90 = 0
            for fileName in fileNames:
                getNumber(fileName, cut_cos, y, z)
            print "background events passing the cut in the signal region =", backgroundL90
            print "background events passing the cut in the control region =", backgroundG90
#            print "data events passing the cut in the signal region =", dataL90
            print "data events passing the cut in the control region =", dataG90
            print "signal events passing the cut in the signal region =", signalL90
            print "signal events passing the cut in the control region =", signalG90
            print "signal efficiency =", signal_eff
            data_G90_2D[x].SetBinContent(data_G90_2D[x].FindBin(y,z), dataG90)
            background_G90_2D[x].SetBinContent(background_G90_2D[x].FindBin(y,z), backgroundG90)
            signal_eff_2D[x].SetBinContent(signal_eff_2D[x].FindBin(y,z), signal_eff) 
    outputfile.cd()
    data_G90_2D[x].Write()
    background_G90_2D[x].Write()
    signal_eff_2D[x].Write()
    canvas1.cd(x+1)
    data_G90_2D[x].Draw("colz")
    canvas2.cd(x+1)
    background_G90_2D[x].Draw("colz")
    canvas3.cd(x+1)
    signal_eff_2D[x].Draw("colz")
canvas1.Write()
canvas2.Write()
canvas3.Write()
#outputfile.Write()

