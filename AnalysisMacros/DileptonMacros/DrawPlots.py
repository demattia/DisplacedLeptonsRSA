import ROOT
from ROOT import TFile, TDirectory, TH1F, TCanvas

inputFile = TFile.Open("WeightedFiles/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_analysis_20140414_weighted_2saMu.root")

gen_lxy_all = inputFile.Get("gen_lxy_all")
gen_lxy_all_DecayMode = inputFile.Get("gen_lxy_all_DecayMode")
gen_lxy_all_DecayMode_withinAcc = inputFile.Get("gen_lxy_all_DecayMode_withinAcc")
gen_lxy_all_DecayMode_withinAcc_trigFired = inputFile.Get("gen_lxy_all_DecayMode_withinAcc_trigFired")

gen_lxy_aftercuts = inputFile.Get("gen_lxy_aftercuts")


gen_lxy_afterReco_noGenMatch = inputFile.Get("gen_lxy_afterReco_noGenMatch")
gen_lxy_reco_genMatched = inputFile.Get("gen_lxy_reco_genMatched")
gen_lxy_reco_removeFakeComb = inputFile.Get("gen_lxy_reco_removeFakeComb")
gen_lxy_reco_triggerMatch = inputFile.Get("gen_lxy_reco_triggerMatch")
gen_lxy_reco_withinAcc = inputFile.Get("gen_lxy_reco_withinAcc")
gen_lxy_afterAllCutsLoose_noCosmicRejection = inputFile.Get("gen_lxy_afterAllCutsLoose_noCosmicRejection")
gen_lxy_afterAllCutsLoose = inputFile.Get("gen_lxy_afterAllCutsLoose")
gen_lxy_afterAllCutsLoose_complementary = inputFile.Get("gen_lxy_afterAllCutsLoose_complementary")
gen_lxy_final = inputFile.Get("gen_lxy_final")

canvas = TCanvas()
gen_lxy_all.Draw()
gen_lxy_final.Draw()
canvas.Draw()
# canvas.SaveAs("c.root")
