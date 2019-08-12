from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
eos2018Data_102X = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_20180920/2018Data_1/'
eos2017DataUL='/eos/cms/store/group/phys_egamma/swmukher/UL/ntuple_2017_UltraLegacy/'
eos2017DataRereco='/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/'

Data2018_102X = {
    ### MiniAOD TnP for IDs scale 
    'DY_madgraph_100X_part012' : tnpSample('DY_madgraph_100X_part012', 
                                       eos2018Data_102X + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8-AOD-100X_part012.root',
                                       isMC = True, nEvts =  -1 ),

    'DY_powheg_102X_part01' : tnpSample('DY_powheg_102X_part01', 
                                       eos2018Data_102X + 'mc/DYToEE_M-50_NNPDF31_TuneCP5_13TeV-powheg-pythia8-AOD-102X_part01.root',
                                       isMC = True, nEvts =  -1 ),


    'data_Run2018Av123' : tnpSample('data_Run2018Av123' , eos2018Data_102X + 'data/Prompt2018_RunA_v13.root' , lumi = 13.53),  # LIVIA: 22/9: for some reason do not manage to run on RunAv2

    'data_Run2018Bv12' : tnpSample('data_Run2018Bv12' , eos2018Data_102X + 'data/Prompt2018_RunB_v12.root' , lumi = 6.78),

    'data_Run2018Cv12' : tnpSample('data_Run2018Cv12' , eos2018Data_102X + 'data/Prompt2018_RunC_v12.root' , lumi = 6.61),

    'data_Run2018Dv2' : tnpSample('data_Run2018Dv2' , eos2018Data_102X + 'data/Prompt2018_RunD_v2.root' , lumi = 12.78), # LIVIA: 22/9: lumi to be verified


    }


Data2017UL = {
    ### MiniAOD TnP for IDs scale 
    'DY_madgraph' : tnpSample('DY_madgraph', 
                                       eos2017DataUL + 'mc.root',
                                       isMC = True, nEvts =  -1 ),

    'data_RunC' : tnpSample('data_RunC' , eos2017DataUL + 'data_C_try4.root' , lumi = 6.61),
    'data_RunF' : tnpSample('data_RunF' , eos2017DataUL + 'data_F_try4.root' , lumi = 6.61),
    'data_RunCF' : tnpSample('data_RunCF' , eos2017DataUL + 'data_retry.root' , lumi = 6.61)
    }


Data2017Rereco = {
    ### MiniAOD TnP for IDs scale 
    'DY_madgraph' : tnpSample('DY_madgraph', 
                                       eos2017DataRereco + 'DY1JetsToLLM50madgraphMLM.root',
                                       isMC = True, nEvts =  -1 ),

    'data_RunC' : tnpSample('data_RunC' , eos2017DataRereco + 'RunC.root' , lumi = 6.61),
    'data_RunF' : tnpSample('data_RunF' , eos2017DataRereco + 'RunF.root' , lumi = 6.61),
    }



##about lumi: thse ntuples are done with /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-321221_13TeV_PromptReco_Collisions18_JSON.txt = with recorded luminosity : 31.71 /fb but ~20% are crashed. Also we need to update the single runs lumi


 
