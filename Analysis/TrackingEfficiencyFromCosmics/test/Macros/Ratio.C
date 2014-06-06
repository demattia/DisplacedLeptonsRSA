{
	TFile *f1 = new TFile("eff_MC_dz10.root");
	TFile *f2 = new TFile("eff_data_dz10_new.root");
	TH1F *h1 = f1->Get("effVsD0");
	TH1F *h2 = f2->Get("effVsD0");
	h2->Divide(h1);
	h2->Draw();
	h2
}
