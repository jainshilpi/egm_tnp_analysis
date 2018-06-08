import sys
#sys.path.append("..")
import etc.inputs.tnpSampleDef as tnpSamples
import libPython.tnpClassUtils as tnpClasses
import ROOT as rt
from ROOT import gStyle
from ROOT import gROOT
import math
import os
import libPython.CMS_lumi as CMS_lumi
import libPython.tdrstyle as tdrstyle


usephoid = False
#usephoid = True

#treename = 'GsfElectronToSC/fitter_tree'
#treename = 'GsfElectronToPhoID/fitter_tree'
#treename = 'GsfElectronToEleID/fitter_tree'
treename = 'tnpEleIDs/fitter_tree'

if usephoid:
    treename = 'tnpPhoIDs/fitter_tree'


tdrstyle.setTDRStyle()

#gROOT.ProcessLine('.L CMS_lumi.C+')


CMS_lumi.extraText = "Preliminary"
#CMS_lumi.lumi_sqrtS = "1 fb^{-1} (13 TeV)" 
#CMS_lumi.lumi_sqrtS = "35.9 fb^{-1} (13 TeV)" 
#CMS_lumi.lumi_sqrtS = "48 pb^{-1} (13 TeV)" 
CMS_lumi.lumi_sqrtS = "(13 TeV)" 
iPos = 11
iPeriod = 4

def loopTree(sample, isMC):
    

    tree = rt.TChain(treename)
    for p in sample.path:
        print ' adding rootfile: ', p
        tree.Add(p)
    #friendTreeName='weights_2016_runBCD'
#    friendTreeName='weights_2016_runAll'
#    friendTreeName='weights_2017_runBCDEF'
    friendTreeName='weights_2017_runC'
    
    #if not sample.puTree is None:
       # print ' - Adding weight tree: %s from file %s ' % (sample.weight.split('.')[0], sample.puTree)
       # friendTreeName = sample.weight.split('.')[0]
       # tree.AddFriend(sample.weight.split('.')[0],sample.puTree)
#    tree.AddFriend(friendTreeName,"/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_04162018-Legacy2016/Legacy16_V1/PU/mc/DY_madgraph_Moriond17_ele.pu.puTree.root")
    tree.AddFriend(friendTreeName,"/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01162018/Moriond18_V1/PU/mc-V2-wRUNC/DY_madgraph_ele.pu.puTree.root")
    print "friendTreeName is ", friendTreeName

    histList = {}
    xTitle   = {}

#    region = ['EB','EE','all']
    region = ['EB','EE']

#    histList['el_sc_eta'] = rt.TH1F('el_sc_eta','SC #eta',100,-2.5,2.5)
    histList['el_sc_eta'] = rt.TH1F('el_sc_eta','SC #eta',50,-2.5,2.5)
    histList['el_sc_eta'].Sumw2()

    histList['el_sc_phi'] = rt.TH1F('el_sc_phi' ,'SC #phi',70,-3.5,3.5)
    histList['el_sc_phi'].Sumw2()

    histList['el_eta'] = rt.TH1F('el_eta','#eta',50,-2.5,2.5)
    histList['el_eta'].Sumw2()

    histList['el_phi'] = rt.TH1F('el_phi' ,'#phi',70,-3.5,3.5)
    histList['el_phi'].Sumw2()	

    histList['tag_sc_phi'] = rt.TH1F('tag_sc_phi' ,'Tag SC #phi',70,-3.5,3.5)
    histList['tag_sc_phi'].Sumw2()

    histList['event_nPV'] = rt.TH1F('event_nPV' ,'#vertices',70,0,70)
    histList['event_nPV'].Sumw2()

    histList['event_nPV_wei'] = rt.TH1F('event_nPV_wei' ,'#vertices',70,0,70)
    histList['event_nPV_wei'].Sumw2()

    histList['event_rho'] = rt.TH1F('event_rho' ,'#rho',100,0,50)
    histList['event_rho'].Sumw2()
    
    #b="this is %sand%s" %(a,c) 
    for reg in region:
        
        histList['el_chIso_%s' %(reg)] = rt.TH1F('el_chIso_%s' %(reg),'Charged isolation',20,0,5)
        histList['el_chIso_%s' %(reg)].Sumw2()

        histList['el_chIso_puSub_%s' %(reg)] = rt.TH1F('el_chIso_puSub_%s' %(reg),'PU subtracted Charged isolation',20,0,5)
        histList['el_chIso_puSub_%s' %(reg)].Sumw2()
        
        histList['el_relchIso_%s' %(reg)] = rt.TH1F('el_relchIso_%s' %(reg),'rel. Charged Isolation',60,0,0.6)
        histList['el_relchIso_%s' %(reg)].Sumw2()

        #nbins=100
        #xmin=0.005
        #xmax=0.015

        nbins=35
        xmin=0.005
        xmax=0.012

        if reg=='EE':
            #nbins=100
            #xmin=0.015
            #xmax=0.035

            nbins=40
            xmin=0.015
            xmax=0.035
                    
        histList['el_sieie_%s' %(reg)] = rt.TH1F('el_sieie_%s' %(reg),'#sigma(i#etai#eta)',nbins,xmin,xmax)
        histList['el_sieie_%s' %(reg)].Sumw2()
		
        histList['el_r9_%s' %(reg)] = rt.TH1F('el_r9_%s' %(reg),'#r9',60,0.4,1)
        histList['el_r9_%s' %(reg)].Sumw2()

        histList['el_ecalIso_%s' %(reg)] = rt.TH1F('el_ecalIso_%s' %(reg),'ECAL Isolation',20,0,5)
        histList['el_ecalIso_%s' %(reg)].Sumw2()
        		

        histList['el_5x5_sieie_%s' %(reg)] = rt.TH1F('el_5x5_sieie_%s' %(reg),'5x5 #sigma(i#etai#eta)',nbins,xmin,xmax)
        histList['el_5x5_sieie_%s' %(reg)].Sumw2()
        
        histList['el_neuIso_%s' %(reg)] = rt.TH1F('el_neuIso_%s' %(reg),'Neutral hadron isolation',20,0,5)
        histList['el_neuIso_%s' %(reg)].Sumw2()
        
        histList['el_phoIso_%s' %(reg)] = rt.TH1F('el_phoIso_%s' %(reg),'Photon isolation',20,0,5)
        histList['el_phoIso_%s' %(reg)].Sumw2()
        
        histList['el_neuIso_puSub_%s' %(reg)] = rt.TH1F('el_neuIso_puSub_%s' %(reg),'PU subtracted Neutral hadron isolation',20,0,5)
        histList['el_neuIso_puSub_%s' %(reg)].Sumw2()
        
        histList['el_phoIso_puSub_%s' %(reg)] = rt.TH1F('el_phoIso_puSub_%s' %(reg),'PU subtracted Photon isolation',20,0,5)
        histList['el_phoIso_puSub_%s' %(reg)].Sumw2()

        histList['el_relneuIso_%s' %(reg)] = rt.TH1F('el_relneuIso_%s' %(reg),'Rel Neutral hadron isolation',60,0,0.6)
        histList['el_relneuIso_%s' %(reg)].Sumw2()

        histList['el_relphoIso_%s' %(reg)] = rt.TH1F('el_relphoIso_%s' %(reg),'Rel Photon isolation',60,0,.6)
        histList['el_relphoIso_%s' %(reg)].Sumw2()

        histList['el_sc_phi_%s' %(reg)] = rt.TH1F('el_sc_phi_%s' %(reg),'SC #phi',70,-3.5,3.5)
        histList['el_sc_phi_%s' %(reg)].Sumw2()

        histList['tag_sc_phi_%s' %(reg)] = rt.TH1F('tag_sc_phi_%s' %(reg),'tag SC #phi',70,-3.5,3.5)
        histList['tag_sc_phi_%s' %(reg)].Sumw2()
        
        histList['el_dEtaIn_%s' %(reg)] = rt.TH1F('el_dEtaIn_%s' %(reg),'#Delta#eta_{in}',50,-0.04,0.04)
        histList['el_dEtaIn_%s' %(reg)].Sumw2()
        
        histList['el_dPhiIn_%s' %(reg)] = rt.TH1F('el_dPhiIn_%s' %(reg),'#Delta#eta_{in}',50,-0.2,0.2)
        histList['el_dPhiIn_%s' %(reg)].Sumw2()
        
        #histList['el_et_%s' %(reg)] = rt.TH1F('el_et_%s' %(reg),'E_{T}',50,0,100)
        histList['el_et_%s' %(reg)] = rt.TH1F('el_et_%s' %(reg),'E_{T}',50,20,100)
        histList['el_et_%s' %(reg)].Sumw2()

#        histList['pair_mass_%s' %(reg)] = rt.TH1F('pair_mass_%s' %(reg),'Di-lepton invariant mass',40,80,100)
        histList['pair_mass_%s' %(reg)] = rt.TH1F('pair_mass_%s' %(reg),'Di-lepton invariant mass',60,60,120)
        histList['pair_mass_%s' %(reg)].Sumw2()


        histList['mass_sc_%s' %(reg)] = rt.TH1F('mass_sc_%s' %(reg),'Di-lepton invariant mass using SC energy',60,60,120)
        histList['mass_sc_%s' %(reg)].Sumw2()




        histList['el_hoe_%s' %(reg)] = rt.TH1F('el_hoe_%s' %(reg),'H/E',20,0.,0.2)
        histList['el_hoe_%s' %(reg)].Sumw2()

        histList['el_mHits_%s' %(reg)] = rt.TH1F('el_mHits_%s' %(reg),'missing hits',4,0.,4)
        histList['el_mHits_%s' %(reg)].Sumw2()
        
        histList['el_5x5_r9_%s' %(reg)] = rt.TH1F('el_5x5_r9_%s' %(reg),'r9 (5x5)',60,0.4,1)
        histList['el_5x5_r9_%s' %(reg)].Sumw2()

        histList['el_etaW_%s' %(reg)] = rt.TH1F('el_etaW_%s' %(reg),'#eta width',50,0.,0.05)
        histList['el_etaW_%s' %(reg)].Sumw2()

        histList['el_phiW_%s' %(reg)] = rt.TH1F('el_phiW_%s' %(reg),'#phi width',50,0.,0.5)
        histList['el_phiW_%s' %(reg)].Sumw2()

        histList['el_fbrem_%s' %(reg)] = rt.TH1F('el_fbrem_%s' %(reg),'#fBrem',25,0.,1)
        histList['el_fbrem_%s' %(reg)].Sumw2()

        histList['el_sc_esE_%s' %(reg)] = rt.TH1F('el_sc_esE_%s' %(reg),'preshower Energy',40,0.,40)
        histList['el_sc_esE_%s' %(reg)].Sumw2()

        histList['el_chisq_%s' %(reg)] = rt.TH1F('el_chisq_%s' %(reg),'#chi^{2}',50,0.,200)
        histList['el_chisq_%s' %(reg)].Sumw2()

        histList['el_dxy_%s' %(reg)] = rt.TH1F('el_dxy_%s' %(reg),'dxy',40,-0.1,0.1)
        histList['el_dxy_%s' %(reg)].Sumw2()

        histList['el_dz_%s' %(reg)] = rt.TH1F('el_dz_%s' %(reg),'dz',40,-0.1,0.1)
        histList['el_dz_%s' %(reg)].Sumw2()


        histList['el_nonTrigMVA80X_%s' %(reg)] = rt.TH1F('el_nonTrigMVA80X_%s' %(reg),'nonTrigMVA80X',50,-1,1)
        histList['el_nonTrigMVA80X_%s' %(reg)].Sumw2()

      
        histList['el_eoverp_wES_%s' %(reg)] = rt.TH1F('el_eoverp_wES_%s' %(reg),'el_eoverp_wES',20,0.,1.6)
        histList['el_eoverp_wES_%s' %(reg)].Sumw2()
       
        histList['el_relchIso_puSub_%s' %(reg)] = rt.TH1F('el_relchIso_puSub_%s' %(reg),'Rel. PU subtracted Neutral hadron isolation',20,0,5)
        histList['el_relchIso_puSub_%s' %(reg)].Sumw2()
       
        histList['el_relneuIso_puSub_%s' %(reg)] = rt.TH1F('el_relneuIso_puSub_%s' %(reg),'Rel. PU subtracted Neutral hadron isolation',20,0,5)
        histList['el_relneuIso_puSub_%s' %(reg)].Sumw2()
        
        histList['el_relphoIso_puSub_%s' %(reg)] = rt.TH1F('el_relphoIso_puSub_%s' %(reg),'Rel. PU subtracted Photon isolation',20,0,5)
        histList['el_relphoIso_puSub_%s' %(reg)].Sumw2()



        ######xTitles
        xTitle['el_chIso_%s' %(reg)] = 'Charged Hadron Isolation [GeV] (%s)' %(reg)
        xTitle['el_chIso_puSub_%s' %(reg)] = 'Charged Hadron Isolation [GeV] (%s)' %(reg)
        xTitle['el_relchIso_%s' %(reg)] = 'Rel. Charged Hadron Isolation (%s)' %(reg)

        xTitle['el_sieie_%s' %(reg)] = '#sigma_{i#eta i#eta} (%s)' %(reg)
        xTitle['el_r9_%s' %(reg)] = 'r9 (%s)' %(reg)		
        xTitle['el_ecalIso_%s' %(reg)] = 'ECAL Isolation [GeV] (%s)' %(reg)
        xTitle['el_5x5_sieie_%s' %(reg)] = '#sigma_{i#eta i#eta} (5x5) (%s)' %(reg)
        xTitle['el_neuIso_%s' %(reg)] = 'Neutral Hadron Isolation [GeV] (%s)' %(reg)
        xTitle['el_phoIso_%s' %(reg)] = 'Photon Isolation [GeV] (%s)' %(reg)

        xTitle['el_neuIso_puSub_%s' %(reg)] = 'Neutral Hadron Isolation [GeV] (%s)' %(reg)
        xTitle['el_phoIso_puSub_%s' %(reg)] = 'Photon Isolation [GeV] (%s)' %(reg)
        xTitle['el_relneuIso_%s' %(reg)] = 'Rel. Neutral Hadron Isolation (%s)' %(reg)
        xTitle['el_relphoIso_%s' %(reg)] = 'Rel. Photon Isolation (%s)' %(reg)

        xTitle['el_dEtaIn_%s' %(reg)] = '#Delta#eta_{in} (%s)' %(reg)
        xTitle['el_dPhiIn_%s' %(reg)] = '#Delta#phi_{in} (%s)' %(reg)
        xTitle['el_et_%s' %(reg)] = 'Probe E_{T} [GeV] (%s)' %(reg)
        xTitle['pair_mass_%s' %(reg)] = 'M_{ee} [GeV] (%s)' %(reg)
        xTitle['mass_sc_%s' %(reg)] = 'M_{ee} {SC energy} [GeV] (%s)' %(reg)
        xTitle['el_eoverp_wES_%s' %(reg)] = 'el_eoverp_wES (%s)' %(reg)      
        
       

        xTitle['el_hoe_%s' %(reg)] = 'H/E (%s)' %(reg)
        xTitle['el_mHits_%s' %(reg)] = 'Missing hits (%s)' %(reg)
        xTitle['el_5x5_r9_%s' %(reg)] = 'r9 (5x5) (%s)' %(reg)
        xTitle['el_etaW_%s' %(reg)] = '#eta SC width (%s)' %(reg)
        xTitle['el_phiW_%s' %(reg)] = '#phi SC width (%s)' %(reg)
        xTitle['el_fbrem_%s' %(reg)] = 'fBrem (%s)' %(reg)
        xTitle['el_sc_esE_%s' %(reg)] = 'Preshower Energy [GeV] (%s)' %(reg)
        xTitle['el_chisq_%s' %(reg)] = '#chi^{2} (%s)' %(reg)
        xTitle['el_dxy_%s' %(reg)] = 'dxy [mm] (%s)' %(reg)
        xTitle['el_dz_%s' %(reg)] = 'dz [mm] (%s)' %(reg)
        xTitle['el_nonTrigMVA80X_%s' %(reg)] = 'Non-triggering MVA (80X) (%s)' %(reg)
        xTitle['el_sc_phi_%s' %(reg)] = 'Probe #phi_{sc} (%s)' %(reg) 
        xTitle['tag_sc_phi_%s' %(reg)] = 'Tag #phi_{sc} (%s)' %(reg) 

        xTitle['el_relchIso_puSub_%s' %(reg)] = 'Rel. Charged Hadron Isolation [GeV] (%s)' %(reg)
        xTitle['el_relphoIso_puSub_%s' %(reg)] = 'Rel. Photon Isolation [GeV] (%s)' %(reg)
        xTitle['el_relneuIso_puSub_%s' %(reg)] = 'Rel. Neutral Hadron Isolation [GeV] (%s)' %(reg)

        
    histList['pair_mass_EB_EB'] = rt.TH1F('pair_mass_EB_EB','Di-lepton invariant mass',60,60,120)
    histList['pair_mass_EB_EB'].Sumw2()

    histList['pair_mass_EB_EE'] = rt.TH1F('pair_mass_EB_EE','Di-lepton invariant mass',60,60,120)
    histList['pair_mass_EB_EE'].Sumw2()

    histList['pair_mass_EE_EE'] = rt.TH1F('pair_mass_EE_EE','Di-lepton invariant mass',60,60,120)
    histList['pair_mass_EE_EE'].Sumw2()


    xTitle['pair_mass_EB_EB'] = 'M_{ee} [GeV] (EB-EB)' 
    xTitle['pair_mass_EB_EE'] = 'M_{ee} [GeV] (EB-EE)' 
    xTitle['pair_mass_EE_EE'] = 'M_{ee} [GeV] (EE-EE)' 


    xTitle['el_sc_eta'] = 'Probe #eta_{sc}' 
    xTitle['el_sc_phi'] = 'Probe #phi_{sc}' 
    xTitle['el_eta'] = '#eta' 
    xTitle['el_phi'] = '#phi' 	
    xTitle['tag_sc_phi'] = 'Tag #phi_{sc}' 
    xTitle['event_nPV'] = '#vertices' 
    xTitle['event_nPV_wei'] = '#vertices' 
    xTitle['event_rho'] = '#rho' 
	
    if(isMC):
        friendTree = tree.GetFriend(friendTreeName)

    #fnvtx = rt.TFile("histo_nvtxratio_runB.root","READ");
    #fnvtx = rt.TFile("histo_nvtxratio_runC.root","READ");
    #hnvtx = fnvtx.Get("hratio");

    for ev in range(tree.GetEntries()):
#    for ev in range(100):
        if (ev % 100000 ==0):
            print 'Processing event: ',ev
        #if (ev >= 100000):
         #   break
        #if (isMC):
          #  if (ev >= 2000):
            #    break
#    for ev in range(1,100):
        if (tree.GetEntry(ev) <= 0):
            raise Exception('TTree::GetEntry() failed')

        run                = tree.run

#        if not isMC:
#            if not run==296174:
#                continue

        #if not isMC:
        #    if (run<298615 and run > 299381):
        #        continue
            
            
####initialize to 0
        el_ecalIso   = -99
        el_eoverp_wES = -99
        el_r9   = -99
        el_neuIso    = -99
        el_phoIso    = -99
        el_chIso     = -99
        el_pt        = -99
        el_sieie     = -99
        el_dEtaIn    = -99
        el_dPhiIn    = -99
        el_et        = -99
        el_sc_eta        = -99
        el_sc_phi        = -99
        
        el_sc_abseta     = -99
        passingLoose80X  = -99
        
        el_eta         = -99
        el_phi         = -99
        
        el_5x5_sieie   = -99
        
        el_hoe         = -99
        el_mHits       = -99
        el_5x5_r9      = -99
        el_5x5_sieip   = -99
        el_etaW        = -99
        el_fbrem       = -99
        el_phiW        = -99
        el_sc_esE      = -99
        el_chisq       = -99
        el_dxy         = -99
        el_dz          = -99
        el_nonTrigMVA80X = -99
        passingConvVeto = -99        
        el_1overEminus1overP = -99        
       
        
        
        el_sc_e      = -99
        el_sc_rawE   = -99
        el_seed_e    = -99
        sc_pt_p      = -99
        scraw_pt_p      = -99
        seed_pt_p      = -99

        
        
        tag_Ele_pt          = tree.tag_Ele_pt
        tag_Ele_eta         = tree.tag_Ele_eta
        tag_Ele_phi         = tree.tag_Ele_phi

#        tag_Ele_sc_phi         = tree.tag_Ele_sc_phi
#        tag_Ele_sc_phi         = -999
        tag_Ele_sc_phi         = tree.tag_Ele_phi
        tag_sc_abseta       = tree.tag_sc_abseta
        tag_sc_eta       = tree.tag_sc_eta
        pair_mass           = tree.pair_mass


        if not usephoid:
            el_ecalIso   = tree.el_ecalIso
#            el_eoverp_wES = tree.el_eoverp_wES
            el_eoverp_wES = tree.el_eoverp
#            passingConvVeto = tree.passingConvVeto        
#            el_1overEminus1overP = tree.el_1overEminus1overP   			
            el_r9   = tree.el_r9			
            el_neuIso    = tree.el_neuIso
            el_phoIso    = tree.el_phoIso
            el_chIso     = tree.el_chIso
            el_pt        = tree.el_pt
            el_sieie     = tree.el_sieie
            el_dEtaIn    = tree.el_dEtaIn
            el_dPhiIn    = tree.el_dPhiIn
            el_et        = tree.el_et
            el_sc_eta        = tree.el_sc_eta
            el_sc_phi        = tree.el_sc_phi
            
            el_sc_abseta     = tree.el_sc_abseta
            passingLoose80X     = tree.passingLoose80X
            
            el_eta         = tree.el_eta
            el_phi         = tree.el_phi
            
            el_5x5_sieie   = tree.el_5x5_sieie
           
            el_hoe         = tree.el_hoe
            el_mHits       = tree.el_mHits
            el_5x5_r9      = tree.el_5x5_r9
            el_5x5_sieip   = tree.el_5x5_sieip
            el_etaW        = tree.el_etaW
            el_fbrem       = tree.el_fbrem
            el_phiW        = tree.el_phiW
            el_sc_esE      = tree.el_sc_esE
            el_chisq       = tree.el_chisq
            el_dxy         = tree.el_dxy
            el_dz          = tree.el_dz
            el_nonTrigMVA80X = tree.el_nonTrigMVA80X
            
            
          
           
            
            el_sc_e      = tree.el_sc_e
            el_sc_rawE   = tree.el_sc_rawE
            el_seed_e    = tree.el_seed_e
            sc_pt_p      = el_sc_e/math.cosh(el_sc_eta)
            scraw_pt_p      = el_sc_rawE/math.cosh(el_sc_eta)
            seed_pt_p      = el_seed_e/math.cosh(el_sc_eta)


        ###phoID
        if usephoid:
            el_ecalIso   = tree.el_ecalIso
            el_r9   = tree.el_r9
            el_neuIso    = tree.ph_neuIso
            el_phoIso    = tree.ph_phoIso
            el_chIso     = tree.ph_chIso
            el_pt        = tree.ph_et
            el_sieie     = tree.ph_sieie
            el_et        = tree.ph_et
            el_sc_eta        = tree.ph_sc_eta
            el_sc_phi        = tree.ph_sc_phi
            
            el_sc_abseta     = tree.ph_sc_eta
            passingLoose80X     = tree.passingLoose
            
            el_eta         = tree.ph_eta
            el_phi         = tree.ph_phi
            
            el_5x5_sieie   = tree.ph_sieie
            el_hoe         = tree.ph_hoe
            el_5x5_r9      = tree.ph_full5x5x_r9
            el_5x5_sieip   = tree.ph_sieip
            el_etaW        = tree.ph_etaW
            el_phiW        = tree.ph_phiW
            el_sc_esE      = tree.ph_sc_esE

            
            el_sc_e      = tree.ph_sc_energy
            el_sc_rawE   = tree.ph_sc_rawE
            el_seed_e    = tree.ph_seed_e
            sc_pt_p      = el_sc_e/math.cosh(el_sc_eta)
            scraw_pt_p      = el_sc_rawE/math.cosh(el_sc_eta)
            seed_pt_p      = el_seed_e/math.cosh(el_sc_eta)


        ###tag variables
        
		
        
        tag_sc_e     = tree.tag_sc_e
        

        sc_pt_t         = tag_sc_e/math.cosh(tag_sc_eta)
        
       


        event_nPV = tree.event_nPV
        event_rho = tree.event_rho



        ##########################PROBE#########################
        ###SC energy
        tlv_sc_p = rt.TLorentzVector()
        tlv_sc_p.SetPtEtaPhiM(sc_pt_p, el_eta,el_phi, 0.511*0.001)

        ###SCraw energy
        tlv_scraw_p = rt.TLorentzVector()
        tlv_scraw_p.SetPtEtaPhiM(scraw_pt_p, el_eta,el_phi, 0.511*0.001)

        ###Seed energy
        tlv_seed_p = rt.TLorentzVector()
        tlv_seed_p.SetPtEtaPhiM(seed_pt_p, el_eta,el_phi, 0.511*0.001)


        ##########################TAG#########################
        ###SC energy
        tlv_sc_t = rt.TLorentzVector()
        tlv_sc_t.SetPtEtaPhiM(sc_pt_t, tag_Ele_eta,tag_Ele_phi, 0.511*0.001)

        ###SCraw energy
       

        ###Seed energy
        


        #######Construct 3 TLorentzVector
        z_sc    = tlv_sc_p    + tlv_sc_t
        
        

        mass_sc    = z_sc.M()
        
        
        
        ###PUweight:totWeight
        totWeight = 1


        if isMC==1:
            totWeight        = friendTree.totWeight
            #totWeight        = tree.totWeight
            ######################################
            #maxbins =  hnvtx.GetNbinsX()
            #nvtxbin = hnvtx.FindBin(event_nPV)
            #weight = hnvtx.GetBinContent(nvtxbin)
            #if(maxbins<nvtxbin):
                #weight = hnvtx.GetBinContent(maxbins)

            #totWeight  = weight
			
            #########################################
#        print 'totweight is ',totWeight


        
        ###get the Eff A
        neu_A, pho_A, cha_A, com_A = EffArea(el_sc_abseta)
            

        
        neuphoIso  = max(el_neuIso+el_phoIso - com_A * event_rho,0)
#        combinedProbeIso   = (el_neuIso+el_phoIso+el_chIso)/el_pt
        combinedProbeIso   = (neuphoIso+el_chIso)/el_pt

#        print "tag pt : mass : combinedIso ", tag_Ele_pt, " ",pair_mass, " ", combinedTagIso
        
#        if not (tag_Ele_pt > 30 and tag_sc_abseta<2.1 and pair_mass>80 and pair_mass<100 and el_sc_abseta<2.5 and el_et>20):
#        if not (tag_Ele_pt > 30 and tag_sc_abseta<2.1 and pair_mass>60 and pair_mass<120 and el_sc_abseta<2.5 and el_et>20):
        #if not (tag_Ele_pt > 30 and tag_sc_abseta<2.5 and pair_mass>60 and pair_mass<120 and el_sc_abseta<2.5 and el_et>20):
		#applying a tighter cut
        if not (tag_Ele_pt > 40 and tag_sc_abseta<1.4442 and pair_mass>80 and pair_mass<100 and el_sc_abseta<2.5 and el_et>20):
            continue

        forIso   = 0
        forIDetc = 0

        
        
        if (el_sc_abseta <= 1.479):                                                    
            #if (el_5x5_sieie<0.011100 and math.fabs(el_dEtaIn) < 0.016315 and math.fabs(el_dPhiIn) < 0.252044 and el_hoe < 0.345843  and (math.fabs(el_dxy))< 0.060279 and math.fabs(el_dz) < 0.800538):
            if (el_5x5_sieie<0.0105 and math.fabs(el_dEtaIn) < 0.00387 and math.fabs(el_dPhiIn) < 0.0716 and el_hoe < 0.05  and (math.fabs(el_dxy))< 0.060279 and math.fabs(el_dz) < 0.800538):
                forIso = 1
                
            forIDetc = combinedProbeIso<0.1
#            forIDetc = combinedProbeIso<0.06
			
        elif (el_sc_abseta > 1.479 and el_sc_abseta < 2.5):
            #if (el_5x5_sieie < 0.033987 and math.fabs(el_dEtaIn) < 0.010671 and math.fabs(el_dPhiIn) < 0.245263 and el_hoe  < 0.134691  and math.fabs(el_dxy) < 0.273097 and math.fabs(el_dz) < 0.885860):
            if (el_5x5_sieie < 0.0356 and math.fabs(el_dEtaIn) < 0.0072 and math.fabs(el_dPhiIn) < 0.147 and el_hoe  < 0.0414  and math.fabs(el_dxy) < 0.273 and math.fabs(el_dz) < 0.885860):
                forIso = 1

            forIDetc = combinedProbeIso<0.1

        #else :
            #forIDetc = combinedProbeIso<0.1				
          


        reg = 'EB'

        if(el_sc_abseta > 1.479):
            reg = 'EE'

        

        combreg = 'EB_EB'

        if(tag_sc_abseta < 1.479):
            combreg = 'EB_EB'
            if(el_sc_abseta > 1.479): 
                combreg = 'EB_EE'

        if(tag_sc_abseta > 1.479):
            combreg = 'EB_EE'   ##### i dont write EE_EB since this combination should go in one hist
            if(el_sc_abseta > 1.479): 
                combreg = 'EE_EE'
            


        if(forIDetc):    
            histList['el_sc_eta'].Fill(el_sc_eta,totWeight)
            histList['el_sc_phi'].Fill(el_sc_phi,totWeight)
			
            histList['el_eta'].Fill(el_eta,totWeight)
            histList['el_phi'].Fill(el_phi,totWeight)			

            histList['event_nPV'].Fill(event_nPV)

            histList['event_nPV_wei'].Fill(event_nPV,totWeight)

            histList['event_rho'].Fill(event_rho,totWeight)
            
            histList['el_sc_phi_%s' %(reg)].Fill(el_sc_phi,totWeight)

            histList['tag_sc_phi'].Fill(tag_Ele_sc_phi,totWeight)

            histList['tag_sc_phi_%s' %(reg)].Fill(tag_Ele_sc_phi,totWeight)

            histList['el_et_%s' %(reg)].Fill(el_et,totWeight)
            histList['el_sieie_%s' %(reg)].Fill(el_sieie,totWeight)
            histList['el_r9_%s' %(reg)].Fill(el_r9,totWeight)			
            histList['el_dEtaIn_%s' %(reg)].Fill(el_dEtaIn,totWeight)
            histList['el_dPhiIn_%s' %(reg)].Fill(el_dPhiIn,totWeight)
            histList['pair_mass_%s' %(reg)].Fill(pair_mass,totWeight)


            histList['pair_mass_%s' %(combreg)].Fill(pair_mass,totWeight)

            histList['mass_sc_%s' %(reg)].Fill(mass_sc,totWeight)
           

            histList['el_hoe_%s' %(reg)].Fill(el_hoe,totWeight)
            histList['el_eoverp_wES_%s' %(reg)].Fill(el_eoverp_wES,totWeight)
            histList['el_mHits_%s' %(reg)].Fill(el_mHits,totWeight)
            histList['el_5x5_r9_%s' %(reg)].Fill(el_5x5_r9,totWeight)
            histList['el_etaW_%s' %(reg)].Fill(el_etaW,totWeight)
            histList['el_phiW_%s' %(reg)].Fill(el_phiW,totWeight)
            histList['el_fbrem_%s' %(reg)].Fill(el_fbrem,totWeight)
            #histList['el_sc_esE_%s' %(reg)].Fill(el_sc_esE,totWeight)
            histList['el_chisq_%s' %(reg)].Fill(el_chisq,totWeight)
            histList['el_dxy_%s' %(reg)].Fill(el_dxy,totWeight)
            histList['el_dz_%s' %(reg)].Fill(el_dz,totWeight)
            histList['el_nonTrigMVA80X_%s' %(reg)].Fill(el_nonTrigMVA80X,totWeight)
            histList['el_5x5_sieie_%s' %(reg)].Fill(el_5x5_sieie,totWeight)

           

            if(el_sc_abseta > 1.479):
                histList['el_sc_esE_%s' %(reg)].Fill(el_sc_esE,totWeight)


        if(forIso):
            histList['el_ecalIso_%s' %(reg)].Fill(el_ecalIso,totWeight)		
            histList['el_phoIso_%s' %(reg)].Fill(el_phoIso,totWeight)
            histList['el_chIso_%s' %(reg)].Fill(el_chIso,totWeight)
            histList['el_neuIso_%s' %(reg)].Fill(el_neuIso,totWeight)

            ne_iso_pusub = max(el_neuIso - neu_A*event_rho,0)
            pho_iso_pusub = max(el_phoIso - pho_A*event_rho,0)
            ch_iso_pusub = max(el_chIso - cha_A*event_rho,0)

            histList['el_phoIso_puSub_%s' %(reg)].Fill(pho_iso_pusub,totWeight)
            histList['el_chIso_puSub_%s' %(reg)].Fill(ch_iso_pusub,totWeight)
            histList['el_neuIso_puSub_%s' %(reg)].Fill(ne_iso_pusub,totWeight)

            rel_phoiso = pho_iso_pusub/el_pt
            rel_neuiso = ne_iso_pusub/el_pt
            rel_chiso = ch_iso_pusub/el_pt

            histList['el_relphoIso_%s' %(reg)].Fill(rel_phoiso,totWeight)
            histList['el_relchIso_%s' %(reg)].Fill(rel_chiso,totWeight)
            histList['el_relneuIso_%s' %(reg)].Fill(rel_neuiso,totWeight)
            
            histList['el_relphoIso_puSub_%s' %(reg)].Fill(pho_iso_pusub/el_pt,totWeight)
            histList['el_relchIso_puSub_%s' %(reg)].Fill(ch_iso_pusub/el_pt,totWeight)
            histList['el_relneuIso_puSub_%s' %(reg)].Fill(ne_iso_pusub/el_pt,totWeight)

            

    for key in histList:
        print "key ,  integral ",key, histList[key].Integral()

    return histList,xTitle



############Eff areas

def EffArea(eta):
    
    neu_A = 0
    pho_A = 0
    cha_A = 0
    com_A = 0
    
    if(eta < 1.0):
        neu_A = 0.0641
        pho_A = 0.1187
        cha_A = 0.0163
        com_A = 0.1566

    if(eta > 1  and eta < 1.479):
        neu_A = 0.0937
        pho_A = 0.1011
        cha_A = 0.0154
        com_A = 0.1626

    if(eta > 1.479  and eta < 2.0):
        neu_A = 0.0710
        pho_A = 0.0627
        cha_A = 0.0091
        com_A = 0.1073

    if(eta > 2.0  and eta < 2.2):
        neu_A = 0.0253
        pho_A = 0.0833
        cha_A = 0.0130
        com_A = 0.0854

    if(eta > 2.2  and eta < 2.3):
        neu_A = 0.0151
        pho_A = 0.1088
        cha_A = 0.0125
        com_A = 0.1051

    if(eta > 2.3  and eta < 2.4):
        neu_A = 0.0130
        pho_A = 0.1241
        cha_A = 0.0103
        com_A = 0.1204

    if(eta > 2.4  and eta < 2.5):
        neu_A = 0.0201
        pho_A = 0.1529
        cha_A = 0.0113
        com_A = 0.1524

    return neu_A, pho_A, cha_A, com_A


    

######For drawing purpose
def setCanvas():
    
    W = 800
    H = 600
    H_ref = 600
    W_ref = 800
    T = 0.08*H_ref
    B = 0.12*H_ref
    L = 0.12*W_ref
    R = 0.04*W_ref

    tdrstyle.setTDRStyle()
#    setTDRStyle()
    c = rt.TCanvas('c','c',50,50,W,H)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    
    
    
    pad1 = rt.TPad("pad1", "The pad 80% of the height",0.0,0.2,1.0,1.0,21)
    pad2 = rt.TPad("pad2", "The pad 20% of the height",0.0,0.001,1.0,0.25,22)
    
    pad1.SetFillColor(0)
    pad2.SetFillColor(0)
    
    pad2.SetTopMargin(0.02619172);
    pad2.SetBottomMargin(0.3102846);

    pad1.Draw()
    pad2.Draw()

    return c,pad1,pad2


def setLegend():
    leg = rt.TLegend(0.72,0.75,0.9194975,0.9154704)
    leg.SetBorderSize(0)
    leg.SetTextFont(62)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(1001)
    
    return leg


def getRatioPlot(histData,histMC, xTitle):
    hratio = histData.Clone()
        
    hratio.Divide(histData,histMC)
    hratio.GetXaxis().SetTitle(xTitle)
    
    hratio.GetXaxis().SetLabelSize(0.11)
    hratio.GetYaxis().SetLabelSize(0.11)
    hratio.GetYaxis().SetTitleSize(0.09)
    
    hratio.GetXaxis().SetLabelFont(42)
    hratio.GetXaxis().SetLabelSize(0.11)
    hratio.GetXaxis().SetTitleSize(0.035)
    hratio.GetXaxis().SetTitleFont(62)
    hratio.GetYaxis().SetTitle("#frac{Data}{MC}")
    hratio.GetYaxis().SetLabelFont(62)
    hratio.GetYaxis().SetLabelSize(0.11)
    hratio.GetYaxis().SetTitleSize(0.13)
    hratio.GetYaxis().SetTitleOffset(0.3)
    
    hratio.GetYaxis().SetNdivisions(205)
    hratio.GetXaxis().SetTitleSize(0.08)
    hratio.GetXaxis().SetLabelSize(0.13)
    hratio.GetXaxis().SetTitleSize(0.13)
    hratio.GetYaxis().SetLabelSize(0.12)
    hratio.GetYaxis().SetTitleSize(0.13)
    hratio.GetYaxis().SetTitleFont(62)
    hratio.GetZaxis().SetLabelFont(62)
    hratio.GetZaxis().SetLabelSize(0.035)
    hratio.GetZaxis().SetTitleSize(0.035)
    hratio.GetZaxis().SetTitleFont(62)
    
    hratio.GetYaxis().SetTitleOffset(0.3)
    hratio.GetYaxis().SetTitle("#frac{Data}{MC}")
    
    hratio.SetMaximum(2)
    hratio.SetMinimum(0)

    return hratio    



dataSamples = {
    'runB'   : tnpSamples.Run17v2['data_Run2017B'].clone(),
    'runC'   : tnpSamples.Run17v2['data_Run2017C'].clone(),
    'runD'   : tnpSamples.Run17v2['data_Run2017D'].clone(),
    'runE'   : tnpSamples.Run17v2['data_Run2017E'].clone(),
    'runF'   : tnpSamples.Run17v2['data_Run2017F'].clone(),
    'runBCDEF'   : tnpSamples.Run17v2['data_Run2017BCDEF'].clone()
}

mcSamples = {
    'runB'   : tnpSamples.Run17v2['DY_madgraph'].clone(),
    'runC'   : tnpSamples.Run17v2['DY_madgraph'].clone(),
    'runD'   : tnpSamples.Run17v2['DY_madgraph'].clone(),
    'runE'   : tnpSamples.Run17v2['DY_madgraph'].clone(),
    'runF'   : tnpSamples.Run17v2['DY_madgraph'].clone(),
    'runBCDEF'   : tnpSamples.Run17v2['DY_madgraph'].clone()
   
    #'runA'  : tnpSamples.Run17['DY_madgraph'  ].clone(),  
#    'runB'  : tnpSamples.Run17n['DY_madgraphv1'].clone(),
 #   'runBbcorr'  : tnpSamples.Run17n['DY_madgraphv1'].clone(),
  #  'runC'  : tnpSamples.Run17n['DY_madgraphv1'].clone()
}

#dataSamples['runBCD'].add_sample(tnpSamples.Moriond17_80X['data_Run2016C'])
#dataSamples['runBCD'].add_sample(tnpSamples.Moriond17_80X['data_Run2016D'])
########data
#dataSamples['runBCD'].add_sample(tnpSamples.Moriond17_80X['data_Run2016C'])
#dataSamples['runBCD'].add_sample(tnpSamples.Moriond17_80X['data_Run2016D'])
#########data
#mcSamples['runBCD'].set_puTree('root://eoscms.cern.ch//eos/cms/store/group/phys_egamma/tnp/80X/pu/DY_madgraph_MCWinter17_rec_rec.pu.puTree.root')
#mcSamples['runBCD'].set_weight('weights_2016_runBCD.totWeight')

#mcSamples['runAll'].set_puTree('root://eoscms.cern.ch//eos/cms/store/group/phys_egamma/tnp/80X/pu/DY_madgraph_MCWinter17_rec_rec.pu.puTree.root')
#mcSamples['runAll'].set_weight('weights_2016_runBCD.totWeight')

#mcSamples['runEF' ].set_weight('weights_2016_runEF.totWeight' )



epochs = [ 'runC' ]
#epochs = [ 'runBCDEF' ]
#epochs = ['runC','runD','runE','runF']
#epochs = ['runB','runC','runD','runE','runF','runG','runH']



for epoch in  epochs:

    ####loopTree(listOfSamples,isMC)

    histData,xTitle = loopTree(dataSamples[epoch],0) 
    histMC,xTitle   = loopTree(mcSamples[epoch],1)
    
    #nE = len(histData)

    fileoutMC   = rt.TFile("histoMC_%s.root" %(epoch), "RECREATE")
    fileoutData = rt.TFile("histoData_%s.root" %(epoch), "RECREATE")

    os.system("mkdir -p plotsLinear"+epoch )
    os.system("mkdir -p plotsLog"+epoch )

    for key in histMC:

        ####save the hists first in a root file which can be used later###
        fileoutMC.cd()
        histMC[key].Write()
        
        fileoutData.cd()
        histData[key].Write()

        #####linear plots
        c,pad1,pad2 = setCanvas()


        histMC[key].SetFillColor(rt.kOrange-2)
        histMC[key].SetLineColor(rt.kOrange-2)
        
        histData[key].SetLineWidth(2)
        histData[key].SetMarkerStyle(20)
        histData[key].SetLineColor(1)

        print "Data integral ",histData[key].Integral()
        print "MC integral ",histMC[key].Integral()
        if not (histMC[key].Integral() == 0):
            scale = histData[key].Integral()/histMC[key].Integral()
        
        if(histMC[key].Integral() == 0):
               
           print "key ", key, " MC integral is 0 so not plotting"
           continue
           
        histMC[key].Scale(scale)
        
        pad1.cd()
        gStyle.SetOptStat(0)
        histMC[key].GetXaxis().SetLabelSize(0)
        histData[key].GetXaxis().SetLabelSize(0)
        histMC[key].GetYaxis().SetTitle('Events')

        maxbin = max(histMC[key].GetMaximum(),histData[key].GetMaximum())
        print "maximum is ",maxbin
        histMC[key].SetMaximum(maxbin*1.6)
        histData[key].SetMaximum(maxbin*1.6)

        histMC[key].Draw('hist')
        histData[key].Draw('same e')
        c.Update()

        #iPeriod = 2
        #iPos = 11
        CMS_lumi.CMS_lumi(pad1, iPeriod, iPos)
        pad1.Modified()
        pad1.Update()

        leg = setLegend()
        
        leg.AddEntry(histData[key],"Data","P")
        leg.AddEntry(histMC[key], "Z#rightarrow ee (MC)","f")
        leg.Draw()
        pad1.Update()

        tex = rt.TLatex(0.4,0.85,"Z#rightarrow ee")
        tex.SetNDC()
        tex.SetLineWidth(2)
#        tex.Draw()
#        pad1.Modified()


        pad2.cd()
        
        hratio = getRatioPlot(histData[key],histMC[key],xTitle[key])

        hratio.SetTitle('')
        hratio.Draw("E1")

        xlow  = histData[key].GetXaxis().GetXmin()
        xhigh = histData[key].GetXaxis().GetXmax()

        l = rt.TLine(xlow,1.,xhigh,1.)
        l.SetLineColor(2)
        l.SetLineStyle(2)
        l.SetLineWidth(2)
        l.Draw("sames")


        c.Modified()
        c.Update()
        
        pngname = "%s.png" %(key)
        print("png name is ",pngname)
        c.Print( "plotsLinear"+epoch+"/%s" %(pngname) )

        ######log plots
        c,pad1,pad2 = setCanvas()
        pad1.cd()
        pad1.SetLogy()
        histMC[key].SetMinimum(0.1)
        histData[key].SetMinimum(0.1)
        
        maxbin = max(histMC[key].GetMaximum(),histData[key].GetMaximum())
        print "maximum is ",maxbin
        histMC[key].SetMaximum(maxbin*14)
        histData[key].SetMaximum(maxbin*14)

        histMC[key].Draw('hist')
        histData[key].Draw('same e')
        c.Update()
        CMS_lumi.CMS_lumi(pad1, iPeriod, iPos)
        pad1.Modified()
        pad1.Update()

        leg.Draw()
        pad1.Update() 
        
        pad2.cd()
        hratio.Draw("E1")
        l.Draw("sames")

        c.Modified()
        c.Update()
        
        c.Print( "plotsLog"+epoch+"/%s" %(pngname) )

            
        ###### end of log plots
        

    fileoutMC.Write()
    fileoutData.Write()

    fileoutMC.Close()
    fileoutData.Close()
    
######end of the function  
