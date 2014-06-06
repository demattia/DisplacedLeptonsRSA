float doweight(TString filename, TCanvas *c, int n) {
	cout<<"****** Weight with "<<filename<<endl;
	TFile *input = new TFile("CompareEff.root");
	TFile *weight = new TFile("/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/Displaced_new2/CMSSW_5_3_6/src/AnalysisMacros/DileptonMacros/WeightedFiles/"+filename+"_weighted_2muTrack.root");
	TH1F *h = (TH1F*)input->Get("effVsD0");
	//h->Draw();
	TH1F *w = (TH1F*)weight->Get("d0_finalCuts");
	float weightedMean=0;
	float diff=0;
	for (int i=1; i<15; i++) {
		cout<<"bin "<<i<<endl;
		cout<<h->GetBinContent(i)<<endl;
		//cout<<w->GetBinContent(i)<<endl;
		diff = 1.0 - h->GetBinContent(i);
		weightedMean += ( fabs(diff) * w->GetBinContent(i) / w->Integral(1,14) );
		//cout<<diff<<endl;
	}
	TCanvas *c1 = new TCanvas;
	c1->cd();
	c1->SetLogy(1);
	w->GetXaxis()->SetTitle("|d_{0}|");
	w->Draw("p");
	c1->SaveAs("weight/"+filename+".gif");
	c1->SaveAs("weight/"+filename+".pdf");
	c->cd(n);
	gPad->SetLogy(1);
	w->Draw("p");
	cout<<"Weighted mean is "<<weightedMean<<endl;
	return weightedMean;
}

void Weight() {
	TCanvas *c = new TCanvas("c","c",1200,1200);
	c->Divide(4,4);
	c->SetLogy(1);
	float mean[11];
	mean[0] = 1 - doweight("HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_analysis_20130320",c,3);
	mean[1] = 1 - doweight("HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150_analysis_20130320",c,1);
	mean[2] = 1 - doweight("HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_analysis_20130320",c,4);
	mean[3] = 1 - doweight("HTo2LongLivedTo4F_MH1000_MFF50_CTau4To400_analysis_20130320",c,2);
	mean[4] = 1 - doweight("HTo2LongLivedTo4F_MH120_MFF20_CTau13To1300_analysis_20130320",c,13);
	//mean[5] = 1 - doweight("HTo2LongLivedTo4F_MH125_MFF50_CTau50To5000_analysis_20130320",c,);
	mean[6] = 1 - doweight("HTo2LongLivedTo4F_MH200_MFF20_CTau7To700_analysis_20130320",c,9);
	mean[7] = 1 - doweight("HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000_analysis_20130320",c,10);
	mean[8] = 1 - doweight("HTo2LongLivedTo4F_MH400_MFF150_CTau40To4000_analysis_20130320",c,7);
	mean[9] = 1 - doweight("HTo2LongLivedTo4F_MH400_MFF20_CTau4To400_analysis_20130320",c,5);
	mean[10] = 1 - doweight("HTo2LongLivedTo4F_MH400_MFF50_CTau8To800_analysis_20130320",c,6);
	c->SaveAs("weight/SignalMC_d0.gif");
	c->SaveAs("weight/SignalMC_d0.pdf");
	float sample[11] = {1,2,3,4,5,6,7,8,9,10,11};
	TCanvas *c2 = new TCanvas;
	c2->cd();
	TGraph *gr = new TGraph(11, sample, mean);
	gr->GetYaxis()->SetRangeUser(0.9,1);
	gr->GetYaxis()->SetTitle("Weighted efficiency ratio");
	gr->GetXaxis()->SetTitle("Different MC signal samples");
	gr->Draw("A*");
	c2->SaveAs("weight/d0_systemtic.gif");
	c2->SaveAs("weight/d0_systemtic.pdf");
}
