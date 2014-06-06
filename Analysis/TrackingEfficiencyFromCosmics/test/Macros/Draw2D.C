#include "TLatex.h"

void Draw2D() {
	gStyle->SetOptStat(0);
	gStyle->SetOptTitle(0);
//	TFile *f = new TFile("eff_data_CRAFT.root","READ");
    TFile *f = new TFile("eff_Data_beforeMuonCut_forNote.root","READ");
    TH2F *histo = (TH2F*)f->FindObjectAny("totalD0errVsPt");
	TCanvas * canvas = new TCanvas();
	canvas->Draw();
  histo->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histo->GetXaxis()->SetTitleOffset(1.1);
//  histo->GetXaxis()->CenterTitle(1);
//  histo->GetXaxis()->SetRangeUser(xmin, xmax);
//  double binWidth = histo->GetXaxis()->GetBinWidth(1);
//  stringstream ss; 
//  ss << binWidth;
  histo->GetYaxis()->SetTitle("#sigma(d_{0}) [cm]");
  histo->GetYaxis()->SetTitleOffset(1.1);
  histo->GetYaxis()->SetLabelSize(0.04);
//  histo->GetYaxis()->SetRangeUser(0., 1.1);
  histo->SetMarkerSize(0.1);
  histo->Draw();
  TF1 f1("func1","0.1+1.91364-0.0211496*x+0.0000906055*x*x-0.000000130650*x*x*x",50,200);
  TF1 f2("func2","1",0,100);
  TF1 f3("func3","0.1+1.91364-0.0211496*200+0.0000906055*200*200-0.000000130650*200*200*200",200,300);
  f1.SetLineColor(kRed);
  f2.SetLineColor(kRed);
  f3.SetLineColor(kRed);
  f1.Draw("same");
  f2.Draw("same");
  f3.Draw("same");
  TLatex l;
  l.SetNDC();
  l.SetTextFont(42);
  l.SetTextAlign(31);
  l.SetTextSize(0.04);
  l.DrawLatex(0.9, 0.95,"CMS Preliminary");
  canvas->Update();
  canvas->SaveAs("plots/D0VsPt_cut_data.png");
  canvas->SaveAs("plots/D0VsPt_cut_data.pdf");

    TH2F *histo2 = (TH2F*)f->FindObjectAny("totalDzerrVsPt");
    TCanvas * canvas2 = new TCanvas();
    canvas2->Draw();
  histo2->GetXaxis()->SetTitle("p_{T} [GeV/c]");
  histo2->GetXaxis()->SetTitleOffset(1.1);
//  histo->GetXaxis()->CenterTitle(1);
//  histo->GetXaxis()->SetRangeUser(xmin, xmax);
//  double binWidth = histo->GetXaxis()->GetBinWidth(1);
//  stringstream ss; 
//  ss << binWidth;
  histo2->GetYaxis()->SetTitle("#sigma(d_{z}) [cm]");
  histo2->GetYaxis()->SetTitleOffset(1.1);
  histo2->GetYaxis()->SetLabelSize(0.04);
//  histo->GetYaxis()->SetRangeUser(0., 1.1);
  histo2->SetMarkerSize(0.1);
  histo2->Draw();
  f1.Draw("same");
  f2.Draw("same");
  f3.Draw("same");
  l.DrawLatex(0.9, 0.95,"CMS Preliminary");
  canvas2->Update();
  canvas2->SaveAs("plots/DzVsPt_cut_data.png");
  canvas2->SaveAs("plots/DzVsPt_cut_data.pdf");


	}
