#include <TFile.h>
#include <TH1F.h>
#include <TCanvas.h>
#include <TString.h>
#include <TStyle.h>
#include <TLegend.h>
#include <sstream>

void improveHisto(TFile * inputFile, TFile * inputFile2, TFile * outputFile, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  TH1F * histo = (TH1F*)inputFile->FindObjectAny(histoName);
  TH1F * histo2 = (TH1F*)inputFile2->FindObjectAny(histoName);
  outputFile->cd();
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

void improveHisto2(TFile * inputFile, TFile * inputFile2, TFile * outputFile, const TString & histoName_total, const TString & histoName_passing, const TString & xAxis, const TString & xUnit)
{
  outputFile->cd();
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

void normalizeHisto(TFile * inputFile, TFile * inputFile2, TFile * outputFile, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  outputFile->cd();
  TH1F * histo = (TH1F*)inputFile->FindObjectAny(histoName);
  TH1F * histo2 = (TH1F*)inputFile2->FindObjectAny(histoName);
  TCanvas * canvas = new TCanvas();
  canvas->Draw();
  if( histo->Integral() > 0 ) histo->Scale(1./histo->Integral());
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

void ratio(TFile * inputFile, TFile * inputFile2, TFile * outputFile, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  outputFile->cd();
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

void ratio2(TFile * inputFile, TFile * inputFile2, TFile * outputFile, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  outputFile->cd();
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

void twoPads(TFile * inputFile, TFile * inputFile2, TFile * outputFile, const TString & histoName, const TString & xAxis, const TString & xUnit)
{
  outputFile->cd();
  TH1F * histo = (TH1F*)inputFile->FindObjectAny(histoName);
  TH1F * histo2 = (TH1F*)inputFile2->FindObjectAny(histoName);
  TCanvas * canvas = new TCanvas();
  canvas->Draw();
  canvas->cd();
  TPad *p1 = new TPad("p1","p1",0.0,0.25,1.0,1.0);
  p1->Draw();
  p1->cd();
  histo->SetMarkerColor(kRed);
  histo->SetMarkerStyle(25);
  histo->SetLineColor(kRed);
  histo->Draw("P");
  histo->GetXaxis()->SetTitle(xAxis+xUnit);
  histo->GetXaxis()->SetTitleOffset(1.1);
  histo->GetXaxis()->SetRangeUser(0., 28);
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
  
  TLegend * legend = new TLegend(0.2, 0.25, 0.48, 0.45);
  legend->SetHeader("CMS");
  legend->AddEntry(histo, "Simulation");
  legend->AddEntry(histo2, "Data");
  //legend->AddEntry(histo, "MC, TKCosmics_p100");
  //legend->AddEntry(histo2, "MC, TKCosmics_p10");
  // TLegend * legend = canvas->BuildLegend();
  legend->Draw("same");
  legend->SetFillColor(kWhite);
  legend->SetBorderSize(0);
  p1->Update();


  canvas->cd();
  TPad *p2 = new TPad("p2","p2",0.0,0.0,1.0,0.25);
  p2->Draw();
  p2->cd();
  TH1F histo_ratio = *histo2;
  histo_ratio.Divide(histo);
  histo_ratio.GetXaxis()->SetTitle("");
  histo_ratio.GetYaxis()->SetTitle("");
//  histo_ratio->GetXaxis()->SetTitleOffset(1.1);
//  histo_ratio->GetXaxis()->CenterTitle(1);
//  histo_ratio->GetXaxis()->SetRangeUser(xmin, xmax);
  histo_ratio.SetMarkerColor(kBlack);
  histo_ratio.SetLineColor(kBlack);
  histo_ratio.SetMarkerStyle(20);
  histo_ratio.GetXaxis()->SetNdivisions(11);
  histo_ratio.GetYaxis()->SetNdivisions(5);
  histo_ratio.GetYaxis()->SetTitle("Data/MC");
  histo_ratio.GetYaxis()->SetTitleOffset(0.4);
  histo_ratio.GetYaxis()->SetTitleSize(0.12);
  histo_ratio.GetYaxis()->SetLabelSize(0.1);
  histo_ratio.GetXaxis()->SetLabelSize(0.1);
  histo_ratio.GetXaxis()->SetRangeUser(0, 28);
  histo_ratio.GetYaxis()->SetRangeUser(0.6, 1.4);  
  histo_ratio.Draw();

  p2->Update();

  canvas->SaveAs("NotePlots/EffAndRatio_"+histoName+".gif");
  canvas->SaveAs("NotePlots/EffAndRatio_"+histoName+".pdf");
  canvas->Write();
}

void fillNormalizeHisto(TFile * inputFile, TFile * inputFile2, TFile * outputFile)
{
  normalizeHisto(inputFile, inputFile2, outputFile, "totalVsD0", "|d_{0}|", " [cm]");
  normalizeHisto(inputFile, inputFile2, outputFile, "totalVsPhi", "#phi", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "totalVsEta", "#eta", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "totalVsPt", "p_{T}", " [GeV/c]");
  normalizeHisto(inputFile, inputFile2, outputFile, "totalVsValidHits", "# valid hits", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "totalVsDz", "|d_{z}|", " [cm]");
  normalizeHisto(inputFile, inputFile2, outputFile, "totalVsChi2", "#chi^{2}/ndof", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "passingVsD0", "|d_{0}|", " [cm]");
  normalizeHisto(inputFile, inputFile2, outputFile, "passingVsPhi", "#phi", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "passingVsEta", "#eta", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "passingVsPt", "p_{T}", " [GeV/c]");
  normalizeHisto(inputFile, inputFile2, outputFile, "passingVsValidHits", "# valid hits", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "passingVsDz", "|d_{z}|", " [cm]");
  normalizeHisto(inputFile, inputFile2, outputFile, "passingVsChi2", "#chi^{2}/ndof", "");
  normalizeHisto(inputFile, inputFile2, outputFile, "deltaR", "#Delta R", "");

  //  improveHisto2(inputFile, inputFile2, "totalVsD0", "passingVsD0", "|d_{0}|", " [cm]");
  //  ratio2(inputFile, inputFile2, "effVsD0", "|d_{0}|", " [cm]");
}

void Compare_new(const int select)
{
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0); 

  TFile * outputFile = new TFile("CompareEff.root", "RECREATE");

  TFile * inputFile = 0;
  TFile * inputFile2 = 0;

  if( select == 0 ) {
    // Using the next 6 lines to make d0 eff plot,
    inputFile = new TFile("eff_MC_dz10.root", "READ");
    inputFile2 = new TFile("eff_data_dz10.root", "READ");
    //improveHisto(inputFile, inputFile2, "effVsD0", "|d_{0}|", " [cm]");
    //ratio(inputFile, inputFile2, "effVsD0", "|d_{0}|", " [cm]"); 
    twoPads(inputFile, inputFile2, outputFile, "effVsD0", "|d_{0}|", " [cm]");
  }
  else if( select == 1 ) {
    // Or using the next 6 lines make dz eff plot
    inputFile = new TFile("eff_MC_dxy4.root", "READ");
    inputFile2 = new TFile("eff_data_dxy4.root", "READ");
    //improveHisto(inputFile, inputFile2, "effVsDz", "|z_{0}|", " [cm]");
    //ratio(inputFile, inputFile2, "effVsDz", "|d_{z}|", " [cm]"); 
    twoPads(inputFile, inputFile2, outputFile, "effVsDz", "|z_{0}|", " [cm]");
  }
  // Using the next lines to make comparison plots for all the vairables: 
  else if( select == 2 ) {
    // You should eigher make comparison plots before applying the muon cut,
    inputFile = new TFile("eff_MC_beforeMuonCut_forNote.root", "READ");
    inputFile2 = new TFile("eff_Data_beforeMuonCut_forNote.root", "READ");
    fillNormalizeHisto(inputFile, inputFile2, outputFile);
  }
  else if( select == 3 ) {
    // or make comparison plots after applying the muon cut 
    inputFile = new TFile("eff_MC_afterMuonCut_forNote.root", "READ");
    inputFile2 = new TFile("eff_Data_afterMuonCut_forNote.root", "READ");
    fillNormalizeHisto(inputFile, inputFile2, outputFile);
  }
  else {
    std::cout << "Error: input value can be 0,1,2,3" << std::endl;
    return 1;
  }

  outputFile->Write();
  outputFile->Close();
}

