{
   c1 = new TCanvas("c1","c1",600,600);

   Int_t n = 31;
   double ctauBase = 35.00;
   double ctauScale[n] = {
   0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   ,   
   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   ,   
   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   ,   
   80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000
   };
   double ctau[n] = {0};
   double ctauErr[n] = {0};

   double eff[n] = { 
   0.593400 ,  0.577300 ,  0.575500 ,  0.578900 ,  0.581900 ,  0.584500 ,  0.593000 ,  0.599000 , 
   0.599800 ,  0.599400 ,  0.599200 ,  0.581600 ,  0.573300 ,  0.556700 ,  0.537000 ,  0.515900 , 
   0.415500 ,  0.294800 ,  0.226500 ,  0.183600 ,  0.154200 ,  0.085867 ,  0.045473 ,  0.030918 , 
   0.023420 ,  0.018849 ,  0.009539 ,  0.004798 ,  0.003205 ,  0.002406 ,  0.001926
   };
   double effRelErr[n] = {
   0.123752 ,  0.114151 ,  0.108322 ,  0.106256 ,  0.105215 ,  0.104588 ,  0.103348 ,  0.102762 , 
   0.102582 ,  0.102509 ,  0.102487 ,  0.103493 ,  0.102901 ,  0.102738 ,  0.102688 ,  0.102707 , 
   0.105069 ,  0.105331 ,  0.105655 ,  0.105885 ,  0.106057 ,  0.106894 ,  0.108679 ,  0.109886 , 
   0.110663 ,  0.111196 ,  0.112406 ,  0.113135 ,  0.113429 ,  0.113460 ,  0.113591
   };
   double effErr[n] = {0}; 

   for (int i=0; i<n; i++) {
     ctau[i] = ctauBase*ctauScale[i];
     effErr[i] = eff[i]*effRelErr[i];
     cout<<ctau[i]<<" "<<eff[i]<<" "<<effErr[i]<<endl;
   }

   gr = new TGraphErrors(n,ctau,eff,ctauErr,effErr);
   gr->SetTitle("HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5");
   gr->GetXaxis()->SetTitle("c#tau [cm]");
   gr->GetXaxis()->SetTitleOffset(1.2);
   gr->GetYaxis()->SetRangeUser(0,1);
   gr->GetYaxis()->SetTitle("Trigger efficiency");
   gr->GetYaxis()->SetTitleOffset(1.2);
   gPad->SetLogx();
   //gPad->SetLogy();
   //gr->SetMarkerColor(4);
   gr->SetMarkerStyle(20);
   gr->Draw("AP");
   TLatex t1;
   t1.SetNDC();
   t1.SetTextSize(0.04);
   t1.DrawLatex(0.2,0.25,"m_{H} = 1000 GeV/c^{2}");
   t1.DrawLatex(0.2,0.2,"m_{X} = 350 GeV/c^{2}");
   return c1;
}
