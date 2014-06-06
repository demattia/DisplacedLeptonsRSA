void fitslicesy() {
//
// Illustrates how to use the TH1::FitSlicesY function
// To see the output of this macro, click begin_html <a href="gif/fitslicesy.gif" >here</a> end_html
//    It uses the TH2F histogram generated in macro hsimple.C
//    It invokes FitSlicesY and draw the fitted "mean" and "sigma"
//    in 2 sepate pads.
//    This macro shows also how to annotate a picture, change
//    some pad parameters.
//Author: Rene Brun
   
// Change some default parameters in the current style
   gStyle->SetLabelSize(0.06,"x");
   gStyle->SetLabelSize(0.06,"y");
   gStyle->SetTitleW(0.6);
   gStyle->SetTitleH(0.1);

   TFile *f = new TFile("eff_fitSlices1.root");
   if (!f) return;
   TH2F *hpxpy = (TH2F*)f->Get("totalD0VsPt");

   TFile *fout = new TFile("fitSlicesy.root","recreate");
// Create a canvas and divide it
   TCanvas *c1 = new TCanvas("c1","c1",800,800);
   c1->Divide(2,2);
   c1->cd(1);

   hpxpy->Draw();
   hpxpy->SetMarkerSize(0.1);

// Fit slices projected along Y fron bins in X [7,32] with more than 20 bins  in Y filled
//   TF1 *f2 = new TF1("f2","gaus",-1,9);
//   f2->SetRange(-1,9);
   hpxpy->FitSlicesY(0,2,-1,0,"QNRG2");
   hpxpy->Write();

// Show fitted "mean" for each slice
   c1->cd(2);
   totalD0VsPt_0->Draw();

   c1->cd(3);
   totalD0VsPt_1->Draw();

// Show fitted "sigma" for each slice
   c1->cd(4);
   totalD0VsPt_2->Draw();

//attributes
   totalD0VsPt_0->SetMarkerSize(0.8);
   totalD0VsPt_1->SetMarkerSize(0.8);
   totalD0VsPt_2->SetMarkerSize(0.8);

   fout->Write();
}
