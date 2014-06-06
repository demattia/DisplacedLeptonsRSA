#include <TFile.h>
#include <TH1F.h>
#include <TCanvas.h>
#include <TString.h>
#include <TStyle.h>
#include <TLegend.h>
#include <sstream>

void improveHisto(TFile * inputFile, TFile * inputFile2, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  TH1F * histo = (TH1F*)inputFile->FindObjectAny(histoName);
  TH1F * histo2 = (TH1F*)inputFile2->FindObjectAny(histoName);
  TCanvas * canvas = new TCanvas();
  canvas->Draw();
  histo->SetMarkerColor(kRed);
  histo->SetMarkerStyle(25);
  histo->SetLineColor(kRed);
  histo->Draw("P");
  histo->GetXaxis()->SetTitle(xAxis+xUnit);
  histo->GetXaxis()->SetTitleOffset(1.1);
  histo->GetXaxis()->SetRangeUser(0., 50.);
  double binWidth = histo->GetXaxis()->GetBinWidth(1);
  stringstream ss;
  ss << binWidth;
  //histo->GetYaxis()->SetTitle("Tracking efficiency / ("+TString(ss.str())+xUnit+")");
  histo->GetYaxis()->SetTitle("Tracking efficiency");
  histo->GetYaxis()->SetTitleOffset(1.1);
  histo->GetYaxis()->SetRangeUser(0., 1.1);

  histo2->SetMarkerStyle(20);
  histo2->SetLineColor(kBlack);
  histo2->Draw("sameP");
  
  TLegend * legend = new TLegend(0.6, 0.65, 0.88, 0.85);
  legend->SetHeader("CMS");
  legend->AddEntry(histo, "Simulation");
  legend->AddEntry(histo2, "Data");
  //legend->AddEntry(histo, "MC, TKCosmics_p100");
  //legend->AddEntry(histo2, "MC, TKCosmics_p10");
  // TLegend * legend = canvas->BuildLegend();
  legend->Draw("same");
  legend->SetFillColor(kWhite);
  legend->SetBorderSize(0);
  canvas->SaveAs("NotePlots/styled_"+histoName+".gif");
  canvas->SaveAs("NotePlots/styled_"+histoName+".pdf");
  canvas->Write();
}

void improveHisto2(TFile * inputFile, TFile * inputFile2, const TString & histoName_total, const TString & histoName_passing, const TString & xAxis, const TString & xUnit)
{
  TH1F * histo = (TH1F*)inputFile->FindObjectAny(histoName_total);
  TH1F * histo2 = (TH1F*)inputFile->FindObjectAny(histoName_passing);
  TH1F * histo3 = (TH1F*)inputFile2->FindObjectAny(histoName_total);
  TH1F * histo4 = (TH1F*)inputFile2->FindObjectAny(histoName_passing);
  TCanvas * canvas = new TCanvas();
  canvas->Draw();
  histo->SetMarkerColor(kBlue);
  histo->SetMarkerStyle(25);
  histo->Draw("P");
  histo->GetXaxis()->SetTitle(xAxis+xUnit);
  histo->GetXaxis()->SetTitleOffset(1.1);
  histo->GetXaxis()->SetRangeUser(0., 50.);
  double binWidth = histo->GetXaxis()->GetBinWidth(1);
  stringstream ss; 
  ss << binWidth;
  histo->GetYaxis()->SetTitle("Entries / ("+TString(ss.str())+xUnit+")");
  histo->GetYaxis()->SetTitleOffset(1.1);
//  histo->GetYaxis()->SetRangeUser(0., 1.1);

  histo2->SetMarkerStyle(20);
  histo2->SetMarkerColor(kMagenta);
  histo2->Draw("sameP");
  
  TLegend * legend = new TLegend(0.5, 0.5, 0.88, 0.7);
  legend->SetHeader("CMS Preliminary");
  legend->AddEntry(histo, "muons");
  legend->AddEntry(histo2, "tracks");
  //legend->AddEntry(histo, "MC, TKCosmics_p100");
  //legend->AddEntry(histo2, "MC, TKCosmics_p10");
  // TLegend * legend = canvas->BuildLegend();
  legend->Draw("same");
  legend->SetFillColor(kWhite);
  legend->SetBorderSize(0);
  canvas->SaveAs("plots/Compare_total_passing_MC.gif");
  canvas->SaveAs("plots/Compare_total_passing_MC.pdf");

  TCanvas * canvas1 = new TCanvas();
  canvas1->Draw();

  histo3->SetMarkerColor(kBlue);
  histo3->SetMarkerStyle(25);
  histo3->Draw("P");
  histo3->GetXaxis()->SetTitle(xAxis+xUnit);
  histo3->GetXaxis()->SetTitleOffset(1.1);
  histo3->GetXaxis()->SetRangeUser(0., 50.);
  double binWidth = histo->GetXaxis()->GetBinWidth(1);
  stringstream ss;
  ss << binWidth;
  histo3->GetYaxis()->SetTitle("Entries / ("+TString(ss.str())+xUnit+")");
  histo3->GetYaxis()->SetTitleOffset(1.1);
//  histo3->GetYaxis()->SetRangeUser(0., 1.1);

  histo4->SetMarkerStyle(20);
  histo4->SetMarkerColor(kMagenta);
  histo4->Draw("sameP");

  TLegend * legend = new TLegend(0.5, 0.5, 0.88, 0.7);
  legend->SetHeader("CMS Preliminary");
  legend->AddEntry(histo3, "muons");
  legend->AddEntry(histo4, "tracks");
  //legend->AddEntry(histo, "MC, TKCosmics_p100");
  //legend->AddEntry(histo2, "MC, TKCosmics_p10");
  // TLegend * legend = canvas->BuildLegend();
  legend->Draw("same");
  legend->SetFillColor(kWhite);
  legend->SetBorderSize(0);
  canvas1->SaveAs("plots/Compare_total_passing_data.gif");
  canvas1->SaveAs("plots/Compare_total_passing_data.pdf");

}


void normalizeHisto(TFile * inputFile, TFile * inputFile2, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  TH1F * histo = (TH1F*)inputFile->FindObjectAny(histoName);
  TH1F * histo2 = (TH1F*)inputFile2->FindObjectAny(histoName);
  TCanvas * canvas = new TCanvas();
  canvas->Draw();
  histo->Scale(1./histo->Integral());
  histo->SetMarkerColor(kRed);
  histo->SetMarkerStyle(25);
  histo->Draw("P");
  histo->GetXaxis()->SetTitle(xAxis+xUnit);
  histo->GetXaxis()->SetTitleOffset(1.1);
  histo->GetXaxis()->CenterTitle(1);
//  histo->GetXaxis()->SetRangeUser(xmin, xmax);
  double binWidth = histo->GetXaxis()->GetBinWidth(1);
  stringstream ss; 
  ss << binWidth;
  histo->GetYaxis()->SetTitle("Entries / ("+TString(ss.str())+xUnit+")");
  histo->GetYaxis()->SetTitleOffset(1.2);
  histo->GetYaxis()->SetLabelSize(0.03);
//  histo->GetYaxis()->SetRangeUser(0., 1.1);
  
  histo2->Scale(1./histo2->Integral());
  histo2->SetMarkerStyle(20);
  histo2->Draw("sameP");
  
  TLegend * legend = new TLegend(0.5, 0.6, 0.88, 0.8);
  legend->SetHeader("CMS Preliminary");
  legend->AddEntry(histo, "MC simulation");
  legend->AddEntry(histo2, "cosmic data");
  //legend->AddEntry(histo, "MC, TKCosmics_p100");
  //legend->AddEntry(histo2, "MC, TKCosmics_p10");
  // TLegend * legend = canvas->BuildLegend();
  legend->Draw("same");
  legend->SetFillColor(kWhite);
  legend->SetBorderSize(0);
  canvas->SaveAs("NotePlots/styled_generalTracks_"+histoName+".gif");
  canvas->SaveAs("NotePlots/styled_generalTracks_"+histoName+".pdf");
  canvas->Write();
}

void ratio(TFile * inputFile, TFile * inputFile2, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  TH1F * histo_data = (TH1F*)inputFile2->FindObjectAny(histoName);
  TH1F * histo_MC = (TH1F*)inputFile->FindObjectAny(histoName);
  new histo = histo_data;
  histo->Divide(histo_MC);

  TCanvas * canvas = new TCanvas();
  canvas->Draw();
  histo->GetXaxis()->SetTitle(xAxis+xUnit);
  histo->GetXaxis()->SetTitleOffset(1.1);
  histo->GetXaxis()->CenterTitle(1);
//  histo.GetXaxis()->SetRangeUser(xmin, xmax);
  double binWidth = histo->GetXaxis()->GetBinWidth(1);
  stringstream ss; 
  ss << binWidth;
  histo->GetYaxis()->SetTitle("Eff(data)/Eff(sim) / ("+TString(ss.str())+xUnit+")");
  histo->GetYaxis()->SetTitleOffset(1.2);
  histo->GetYaxis()->SetLabelSize(0.03);
  histo->GetXaxis()->SetRangeUser(0, 50);
  histo->Draw();
  histo->Write();
  canvas->SaveAs("plots/Ratio_"+histoName+".gif");
  canvas->SaveAs("plots/Ratio_"+histoName+".pdf");
  canvas->Write();

}

void ratio2(TFile * inputFile, TFile * inputFile2, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  TH1F * histo = (TH1F*)inputFile2->FindObjectAny(histoName);
  TH1F * histo_data = (TH1F*)inputFile2->FindObjectAny(histoName);
  TH1F * histo_MC = (TH1F*)inputFile->FindObjectAny(histoName);
  histo->Add(histo_MC,histo_data,1,-1);
  histo->Divide(histo_MC);

  TCanvas * canvas = new TCanvas();
  canvas->Draw();
  histo->GetXaxis()->SetTitle(xAxis+xUnit);
  histo->GetXaxis()->SetTitleOffset(1.1);
  histo->GetXaxis()->CenterTitle(1);
//  histo->GetXaxis()->SetRangeUser(xmin, xmax);
  double binWidth = histo->GetXaxis()->GetBinWidth(1);
  stringstream ss; 
  ss << binWidth;
  histo->GetYaxis()->SetTitle("[Eff(sim)-Eff(data)]/Eff(sim) / ("+TString(ss.str())+xUnit+")");
  histo->GetYaxis()->SetTitleOffset(1.2);
  histo->GetYaxis()->SetLabelSize(0.03);
  histo->GetXaxis()->SetRangeUser(0, 50);
  histo->Draw();
  histo->Write();
  canvas->SaveAs("plots/Ratio2_"+histoName+".gif");
  canvas->SaveAs("plots/Ratio2_"+histoName+".pdf");
  canvas->Write();

}


void Compare()
{
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0); 

  TFile * outputFile = new TFile("CompareEff.root", "RECREATE");


// make d0 eff plot
  TFile * inputFile = new TFile("eff_MC_dz10.root", "READ");
  TFile * inputFile2 = new TFile("eff_data_dz10_new.root", "READ");
  TFile * outputFile = new TFile("CompareEff.root", "RECREATE");
  improveHisto(inputFile, inputFile2, "effVsD0", "|d_{0}|", " [cm]");
  ratio(inputFile, inputFile2, "effVsD0", "|d_{0}|", " [cm]"); 


// make dz eff plot
//  TFile * inputFile = new TFile("eff_MC_dxy4.root", "READ");
//  TFile * inputFile2 = new TFile("eff_data_dxy4_new.root", "READ");
//  TFile * outputFile = new TFile("CompareEff.root", "RECREATE");
//  improveHisto(inputFile, inputFile2, "effVsDz", "|z_{0}|", " [cm]");
//  ratio(inputFile, inputFile2, "effVsDz", "|d_{z}|", " [cm]"); 


// make comparison plots before applying the muon cut
//  TFile * inputFile = new TFile("eff_MC_beforeMuonCut_forNote.root", "READ");
//  TFile * inputFile2 = new TFile("eff_Data_beforeMuonCut_forNote.root", "READ");

// make comparison plots after applying the muon cut 
//  TFile * inputFile = new TFile("eff_MC_afterMuonCut_forNote.root", "READ");
//  TFile * inputFile2 = new TFile("eff_Data_afterMuonCut_forNote.root", "READ");

//  normalizeHisto(inputFile, inputFile2, "totalVsD0", "|d_{0}|", " [cm]");
//  normalizeHisto(inputFile, inputFile2, "totalVsPhi", "#phi", "");
//  normalizeHisto(inputFile, inputFile2, "totalVsEta", "#eta", "");
//  normalizeHisto(inputFile, inputFile2, "totalVsPt", "p_{T}", " [GeV/c]");
//  normalizeHisto(inputFile, inputFile2, "totalVsValidHits", "# valid hits", "");
//  normalizeHisto(inputFile, inputFile2, "totalVsDz", "|d_{z}|", " [cm]");
//  normalizeHisto(inputFile, inputFile2, "totalVsChi2", "#chi^{2}/ndof", "");
//  normalizeHisto(inputFile, inputFile2, "passingVsD0", "|d_{0}|", " [cm]");
//  normalizeHisto(inputFile, inputFile2, "passingVsPhi", "#phi", "");
//  normalizeHisto(inputFile, inputFile2, "passingVsEta", "#eta", "");
//  normalizeHisto(inputFile, inputFile2, "passingVsPt", "p_{T}", " [GeV/c]");
//  normalizeHisto(inputFile, inputFile2, "passingVsValidHits", "# valid hits", "");
//  normalizeHisto(inputFile, inputFile2, "passingVsDz", "|d_{z}|", " [cm]");
//  normalizeHisto(inputFile, inputFile2, "passingVsChi2", "#chi^{2}/ndof", "");
//  normalizeHisto(inputFile, inputFile2, "deltaR", "#Delta R", "");

//  improveHisto2(inputFile, inputFile2, "totalVsD0", "passingVsD0", "|d_{0}|", " [cm]");
//  ratio2(inputFile, inputFile2, "effVsD0", "|d_{0}|", " [cm]");

  outputFile->Write();
  outputFile->Close();
}

