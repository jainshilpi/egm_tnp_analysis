#include "CMS_lumi.C"
#include <cstdlib>

void xAxisname(string histname, string& xname, string& xunit, string& reg);

void setTCanvasNicev1(TCanvas *can0){
  can0->SetFillColor(0);
  can0->SetBorderMode(0);
  can0->SetBorderSize(2);
  can0->SetTickx(1);
  can0->SetTicky(1);
  /*can0->SetLeftMargin(0.15);
  can0->SetRightMargin(0.05);
  can0->SetTopMargin(0.05);
  can0->SetBottomMargin(0.13);
  */
  can0->SetFrameFillStyle(0);
  can0->SetFrameBorderMode(0);
  can0->SetFrameFillStyle(0);
  can0->SetFrameBorderMode(0);
  return;
}


void plot_onlyMC(){

  bool plotLog = false;
  //bool plotLog = true;

   string dirName = "plotsLinear";
   if(plotLog)
     dirName = "plotsLog";
   
   const int dir_err = system( Form(" mkdir %s",dirName.c_str() ) );
   if(dir_err == -1){
     std::cout<<"ERRR!!!! directory "<<dirName<<" could not be created!!! Please check! Plots wont be saved"<<std::endl;
   }

  TFile *f;

  const int nfiles = 3;
  string fmcnames[nfiles] = {"histoMC_mc1.root", "histoMC_mc2.root", "histoMC_mc3.root"};
  //string mcTitle[nfiles] = {"2017UL", "2018re-reco", "2021", "2023"};
  string mcTitle[nfiles] = {"2017UL", "2018re-reco", "2021"};

  vector<string> varnames;
  
  TFile *fmc[nfiles];
  for(int ifile=0; ifile<nfiles; ifile++){
    
    fmc[ifile] = TFile::Open(fmcnames[ifile].c_str());

    if(ifile==0){
      TIter next(fmc[ifile]->GetListOfKeys());
      TKey *key;
      while ((key = (TKey*)next())) {
	
	TClass *cl = gROOT->GetClass(key->GetClassName());
	if (cl->InheritsFrom("TDirectory")) {
	  continue;
	}
	
	
	if (!cl->InheritsFrom("TH1F")) continue;
	
	TH1 *htmp = (TH1*)key->ReadObj();

	string var = htmp->GetName();
	varnames.push_back(var);
      }//while ((key = (TKey*)next()))
    }//if(ifile==0)
  }//for(int ifile=0; ifile<nfiles; ifile++)

  

  TH1F *hmc[nfiles];
  //int col[nfiles] = {1,8,9,46};
  int col[nfiles] = {1,8,9};
  double tmpMax[nfiles];
  
  for(int ivar=0; ivar<varnames.size(); ivar++){
    
    string var = varnames[ivar];
        
    for(int ifile=0; ifile<nfiles; ifile++){
      
      hmc[ifile] = (TH1F*) fmc[ifile]->Get(var.c_str());
      hmc[ifile]->SetLineColor(col[ifile]);
      hmc[ifile]->SetLineWidth(2);
      hmc[ifile]->Scale(1./hmc[ifile]->Integral());
      tmpMax[ifile] = hmc[ifile]->GetMaximum();
  
    }//for(int ifile=0; ifile<nfiles; ifile++)

    double maxBinC = TMath::MaxElement(nfiles,tmpMax);
    
    
    int W = 800;
    int H = 600;
    
    int H_ref = 600; 
    int W_ref = 800; 
    
    // references for T, B, L, R
    float T = 0.08*H_ref;
    float B = 0.12*H_ref; 
    float L = 0.12*W_ref;
    float R = 0.04*W_ref;


    
    TCanvas* c = new TCanvas("c","c",50,50,W,H);
    
    c->SetLeftMargin( L/W );
    c->SetRightMargin( R/W );
    c->SetTopMargin( T/H );
    c->SetBottomMargin( B/H );
    
    gStyle->SetOptStat(0);
    
    
    gStyle->SetTitleFont(62);
    gStyle->SetLabelFont(62);
    
    setTCanvasNicev1(c);

    TLegend *leg = new TLegend(0.6080402,0.7125436,0.8994975,0.8954704,NULL,"brNDC");
    leg->SetBorderSize(0);
    leg->SetTextFont(42);
    leg->SetLineColor(1);
    leg->SetLineStyle(1);
    leg->SetLineWidth(1);
    leg->SetFillColor(0);
    leg->SetFillStyle(1001);
    
    char *binw = new char[100];
  
    string fname = var;

    ///get the xaxis name and the y axis unit
    string xname = "";
    string xunit = "";
    string reg = "";
    xAxisname(var,xname, xunit, reg);

    cout<<"REG is "<<reg<<endl;

    cout<<"Var is , unit is "<<var<<" "<<xunit<<endl;
    //bin widths
    sprintf(binw,"Events / %2.1f %s", float(hmc[0]->GetBinWidth(1)), xunit.c_str());

    if(float(hmc[0]->GetBinWidth(1)) < 10e-2)
    sprintf(binw,"Events / %2.2f %s", float(hmc[0]->GetBinWidth(1)), xunit.c_str());

    if(float(hmc[0]->GetBinWidth(1)) < 10e-3)
      sprintf(binw,"Events / %2.3f %s", float(hmc[0]->GetBinWidth(1)), xunit.c_str());

    if(float(hmc[0]->GetBinWidth(1)) < 10e-4)
      sprintf(binw,"Events / %2.4f %s", float(hmc[0]->GetBinWidth(1)), xunit.c_str());

    if(float(hmc[0]->GetBinWidth(1)) < 10e-5)
      sprintf(binw,"Events / %2.5f %s", float(hmc[0]->GetBinWidth(1)), xunit.c_str());

    string xtitle = xname;

    double dmax = 1.5;
    double dmin = 0.1;

    if(plotLog) dmax = 70.0;

    for(int ifile=0; ifile<nfiles; ifile++){     
      
      hmc[ifile]->SetMaximum(maxBinC*dmax);
      hmc[ifile]->SetMinimum(dmin);
      hmc[ifile]->GetXaxis()->SetTitleSize(0.05);  
      hmc[ifile]->GetYaxis()->SetTitleSize(0.05);  


      
      //hmc[ifile]->GetXaxis()->SetLabelOffset(999);
      hmc[ifile]->GetXaxis()->SetLabelSize(0);

      
      
      
      hmc[ifile]->GetXaxis()->SetLabelFont(42);
      hmc[ifile]->GetXaxis()->SetLabelSize(0.035);
      hmc[ifile]->GetXaxis()->SetTitleSize(0.035);
      //hmc[ifile]->GetXaxis()->SetTitleSize(0.05);
      hmc[ifile]->GetXaxis()->SetTitleFont(42);
      hmc[ifile]->GetYaxis()->SetLabelFont(42);
      hmc[ifile]->GetYaxis()->SetLabelSize(0.035);
      //hmc[ifile]->GetYaxis()->SetTitleSize(0.035);
      hmc[ifile]->GetYaxis()->SetTitleSize(0.05);
      hmc[ifile]->GetYaxis()->SetTitleOffset(1);
      hmc[ifile]->GetYaxis()->SetTitleFont(42);
      hmc[ifile]->SetTitle("");

      hmc[ifile]->GetYaxis()->SetTitle(binw);
      hmc[ifile]->GetXaxis()->SetTitle(xtitle.c_str());  


      if(ifile==0 )hmc[ifile]->Draw("HIST");
      else hmc[ifile]->Draw("HISTsame");

      leg->AddEntry(hmc[ifile], mcTitle[ifile].c_str(),"l");

    }

    leg->Draw();
    c->Update();

    char *filename = new char[100];   
   sprintf(filename,"%s/%s.png",dirName.c_str(),var.c_str());
   c->Print(filename);
   sprintf(filename,"%s/%s.C",dirName.c_str(),var.c_str());
   c->Print(filename);
   

  }//for(int ivar=0; ivar<varnames.size(); ivar++)
}// void plot_onlyMC()
 


void xAxisname(string histname, string& xname, string& xunit, string& reg){

  ////variable naming
  int fstr = histname.find("chIso",0);
  if(fstr!=string::npos)
    {
      xname = "PF Charged Isolation [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("neuIso",0);
  if(fstr!=string::npos)
    {
      xname = "PF Neutral Hadron Isolation [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("phoIso",0);
  if(fstr!=string::npos)
    {
      xname = "PF Photon Isolation [GeV]";
      xunit = "GeV";
    }



  fstr = histname.find("ecalIso",0);
  if(fstr!=string::npos)
    {
      xname = "ECAL Isolation [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("hcalIso",0);
  if(fstr!=string::npos)
    {
      xname = "HCAL Isolation [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("hcalIso1",0);
  if(fstr!=string::npos)
    {
      xname = "HCAL depth1 Isolation [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("hcalIso2",0);
  if(fstr!=string::npos)
    {
      xname = "HCAL depth2 Isolation [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("trkIso",0);
  if(fstr!=string::npos)
    {
      xname = "Tracker Isolation [GeV]";
      xunit = "GeV";
    }




  fstr = histname.find("e1x3",0);
  if(fstr!=string::npos)
    {
      xname = "E_{1x3}/E_{5x5}";
      xunit = "";
    }



  fstr = histname.find("e1x3raw",0);
  if(fstr!=string::npos)
    {
      xname = "E_{1x3}";
      xunit = "GeV";
    }

  
  fstr = histname.find("e1x3raw",0);
  if(fstr!=string::npos)
    {
      xname = "E_{1x3}";
      xunit = "GeV";
    }

  fstr = histname.find("e2x2",0);
  if(fstr!=string::npos)
    {
      xname = "E_{2x2}/E_{5x5}";
      xunit = "";
    }


  fstr = histname.find("e2x2raw",0);
  if(fstr!=string::npos)
    {
      xname = "E_{2x2}";
      xunit = "GeV";
    }


  fstr = histname.find("e2x5",0);
  if(fstr!=string::npos)
    {
      xname = "E_{2x5}/E_{5x5}";
      xunit = "";
    }


  fstr = histname.find("e2x5raw",0);
  if(fstr!=string::npos)
    {
      xname = "E_{2x5}";
      xunit = "GeV";
    }


  fstr = histname.find("e5x5raw",0);
  if(fstr!=string::npos)
    {
      xname = "E_{5x5}";
      xunit = "GeV";
    }

  fstr = histname.find("eleVeto",0);
  if(fstr!=string::npos)
    {
      xname = "CSV";
      xunit = "";
    }

  fstr = histname.find("esE",0);
  if(fstr!=string::npos)
    {
      xname = "E_{ES} [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("esEnTorawEn",0);
  if(fstr!=string::npos)
    {
      xname = "E_{ES}/E_{SC}^{Raw}";
      xunit = "";
    }


  fstr = histname.find("esSRR",0);
  if(fstr!=string::npos)
    {
      xname = "#sigma_{E}^{ES}";
      xunit = "GeV";
    }


  fstr = histname.find("hoe",0);
  if(fstr!=string::npos)
    {
      xname = "H/E";
      xunit = "";
    }

  fstr = histname.find("muu",0);
  if(fstr!=string::npos)
    {
      xname = "M_{#mu#mu} [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("muug",0);
  if(fstr!=string::npos)
    {
      xname = "M_{#mu#mu#gamma} [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("muuPlusmuug",0);
  if(fstr!=string::npos)
    {
      xname = "(M_{#mu#mu#gamma} + M_{#mu#mu})[GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("mva",0);
  if(fstr!=string::npos)
    {
      xname = "MVA";
      xunit = "";
    }


  fstr = histname.find("nvtx",0);
  if(fstr!=string::npos)
    {
      xname = "Nvtx";
      xunit = "";
    }

  fstr = histname.find("et",0);
  if(fstr!=string::npos)
    {
      xname = "P_{T} [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("r9",0);
  if(fstr!=string::npos)
    {
      xname = "R_{9}";
      xunit = "";
    }


  fstr = histname.find("scBrem",0);
  if(fstr!=string::npos)
    {
      xname = "SC brem";
      xunit = "";
    }

  fstr = histname.find("scEn",0);
  if(fstr!=string::npos)
    {
      xname = "SC Energy [GeV]";
      xunit = "[GeV]";
    }




  fstr = histname.find("scRawEn",0);
  if(fstr!=string::npos)
    {
      xname = "E_{SC}^{Raw} [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("sie",0);
  if(fstr!=string::npos)
    {
      //xname = "#sigma_{i#etai#eta}";
      xname = "#sigma_{#eta#eta}";
      xunit = "";
    }

  fstr = histname.find("sietaiphi",0);
  if(fstr!=string::npos)
    {
      xname = "#sigma_{i#etai#phi}";
      xunit = "";
    }

  fstr = histname.find("siphi",0);
  if(fstr!=string::npos)
    {
      xname = "#sigma_{i#phii#phi}";
      xunit = "";
    }
  ////////////////////////////////////////////

  fstr = histname.find("el_dEtaIn",0);
  if(fstr!=string::npos)
    {
      xname = "#Delta#eta_{in}";
      //xunit = "GeV";
    }

  fstr = histname.find("el_dPhiIn",0);
  if(fstr!=string::npos)
    {
      xname = "#Delta#phi_{in} [rad]";
      xunit = "rad";
    }


  fstr = histname.find("el_dz",0);
  if(fstr!=string::npos)
    {
      xname = "dz [mm]";
      //xunit = "GeV";
    }

  fstr = histname.find("el_chisq",0);
  if(fstr!=string::npos)
    {
      xname = "#chi^{2}";
      //xunit = "GeV";
    }

  fstr = histname.find("el_eoverp",0);
  if(fstr!=string::npos)
    {
      xname = "E/p";
      //xunit = "GeV";
    }

  fstr = histname.find("el_fbrem",0);
  if(fstr!=string::npos)
    {
      xname = "f_{brem}";
      //xunit = "GeV";
    }

  fstr = histname.find("el_neuIso",0);
  if(fstr!=string::npos)
    {
      xname = "Neutral Hadron Isolation [GeV]";
      xunit = "GeV";
    }

  fstr = histname.find("el_phoIso",0);
  if(fstr!=string::npos)
    {
      xname = "Photon Isolation [GeV]";
      xunit = "GeV";
    }


  fstr = histname.find("el_relneuIso",0);
  if(fstr!=string::npos)
    {
      xname = "Rel. Neutral Hadron Isolation";
      //xunit = "GeV";
    }

  fstr = histname.find("el_relphoIso",0);
  if(fstr!=string::npos)
    {
      xname = "Rel. Photon Isolation";
      //xunit = "GeV";
    }

  fstr = histname.find("el_relchIso",0);
  if(fstr!=string::npos)
    {
      xname = "Rel. Charged Hadron Isolation";
      //xunit = "GeV";
    }


  fstr = histname.find("eta",0);
  if(fstr!=string::npos)
    {
      xname = "#eta";
      xunit = "";
    }

  fstr = histname.find("el_mHits",0);
  if(fstr!=string::npos)
    {
      xname = "# missing hits";
      xunit = "";
    }

  fstr = histname.find("sc_eta",0);
  if(fstr!=string::npos)
    {
      xname = "#eta^{SC}";
      xunit = "";
    }

  fstr = histname.find("sc_phi",0);
  if(fstr!=string::npos)
    {
      xname = "#phi^{SC} [rad]";
      xunit = "rad";
    }


  fstr = histname.find("etaW",0);
  if(fstr!=string::npos)
    {
      xname = "#eta^{SC} width";
      xunit = "";
    }

  fstr = histname.find("phiW",0);
  if(fstr!=string::npos)
    {
      xname = "#phi^{SC} width [rad]";
      xunit = "rad";
    }


  fstr = histname.find("relchIso",0);
  if(fstr!=string::npos)
    {
      xname = "PF Charged Isolation";
      xunit = "";
    }

  fstr = histname.find("relneuIso",0);
  if(fstr!=string::npos)
    {
      xname = "PF Neutral Hadron Isolation";
      xunit = "";
    }

  fstr = histname.find("relphoIso",0);
  if(fstr!=string::npos)
    {
      xname = "PF Photon Isolation";
      xunit = "";
    }

  ////////////////////////////////////////////

  fstr = histname.find("EB",0);
  if(fstr!=string::npos)
    {
      reg = "Barrel";
    }

  fstr = histname.find("EE",0);
  if(fstr!=string::npos)
    {
      reg = "Endcap";
    }

  /*
  fstr = histname.find("2012",0);
  if(fstr!=string::npos)
    {
      xname += "[5x5]";
      xunit = "";
    }
  */

  fstr = histname.find("EB",0);
  if(fstr!=string::npos)
    {
      //xname += " [EB]";
      //xunit = "";
    }


  fstr = histname.find("EE",0);
  if(fstr!=string::npos)
    {
      //xname += " [EE]";
      //xunit = "";
    }
  

}
