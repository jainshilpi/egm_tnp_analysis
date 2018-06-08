from libPython.tnpClassUtils import tnpSample

### qll stat
#eos2016 = '/eos/cms/store/group/phys_egamma/tnp/ntuples_04232018-Legacy2016/Legacy16_V1/'
#eos2016= '/eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
eos2017n= '/eos/cms/store/group/phys_egamma/tnp/run2017/RunBC_17Aug/'
eos2017v2 = '/eos/cms/store/group/phys_egamma/tnp/run2017/RunBC_3sept/'
eos2017v3 = '/eos/cms/store/group/phys_egamma/tnp/run2017/RunCD_14Oct/'
#eos2017 = '/eos/cms/store/group/phys_egamma/tnp/run2017/RunBCrereco_DEFprompt_2Nov/'
eos2017 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01162018/Moriond18_V1/'
eos2016 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_04162018-Legacy2016/Legacy16_V1/'
# Run17 = {
    # 'DY_madgraph' : tnpSample('DY_madgraph', eos2017 + 'mc_27July.root', 
                              # isMC = True, nEvts = 1528087 ),
    # 'data_Run2017B' : tnpSample('data_Run2017B' , eos2017 + 'data_RunB_27July.root' , lumi = 2.5 ),
    # 'data_Run2017C' : tnpSample('data_Run2017C' , eos2017 + 'data_RunC_14Aug.root', lumi = 2.5)
# }
# Run17n = {
    # 'DY_madgraphv1' : tnpSample('DY_madgraphv1', eos2017n + 'mc_17Aug.root', 
    # 'DY_madgraphv1' : tnpSample('DY_madgraphv1', eos2017n + 'mc_17Aug_sample1.root', 
                              # isMC = True, nEvts = 1528087 ),
    # 'data_Run2017Bv1' : tnpSample('data_Run2017Bv1' , eos2017n + 'data_runB_17Aug.root' , lumi = 2.5 ),
    # 'data_Run2017Cv1' : tnpSample('data_Run2017Cv1' , eos2017n + 'data_runC_17Aug.root', lumi = 2.5)
    # 'data_Run2017Cv1' : tnpSample('data_Run2017Cv1' , eos2017v2 + 'data_runCv1.root' , lumi = 2.5 ),
    # 'data_Run2017Cv1' : tnpSample('data_Run2017Cv2' , eos2017v2 + 'data_runCv2.root' , lumi = 2.5 )
# }
Run17v2 = {
'DY_madgraph' : tnpSample('DY_madgraph1', eos2017 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root', isMC = True, nEvts = 6854210 ),
'data_Run2017B' : tnpSample('data_Run2017B' , eos2017 + 'data/TnPTree_17Nov2017_RunB.root' , lumi = 4.8 ),
'data_Run2017C' : tnpSample('data_Run2017C' , eos2017 + 'data/TnPTree_17Nov2017_RunC.root' , lumi = 9.8 ),
'data_Run2017D' : tnpSample('data_Run2017D' , eos2017 + 'data/TnPTree_17Nov2017_RunD.root' , lumi = 4.3 ),
'data_Run2017E' : tnpSample('data_Run2017E' , eos2017 + 'data/TnPTree_17Nov2017_RunE.root' , lumi = 9.8 ),
'data_Run2017F' : tnpSample('data_Run2017F' , eos2017 + 'data/TnPTree_17Nov2017_RunF.root' , lumi = 9.8 ),
'data_Run2017BCDEF' : tnpSample('data_Run2017BCDEF' , '/eos/cms/store/group/phys_egamma/tnp/run2017DPS/TnPTree_17Nov2017_RunBCDEF.root' , lumi = 9.8 ),
}

Run16 = {
'DY_madgraph' : tnpSample('DY_madgraph', eos2016 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_all.root', isMC = True, nEvts = 6854210 ),
'data_Run2016B' : tnpSample('data_Run2016B' , eos2016 + 'data/TnPTree_07Aug17_Run2016Bv2.root' , lumi = 4.8 ),
'data_Run2016C' : tnpSample('data_Run2016C' , eos2016 + 'data/TnPTree_07Aug17_Run2016C.root' , lumi = 9.8 ),
'data_Run2016D' : tnpSample('data_Run2016D' , eos2016 + 'data/TnPTree_07Aug17_Run2016D.root' , lumi = 4.3 ),
'data_Run2016E' : tnpSample('data_Run2016E' , eos2016 + 'data/TnPTree_07Aug17_Run2016E.root' , lumi = 9.8 ),
'data_Run2016F' : tnpSample('data_Run2016F' , eos2016 + 'data/TnPTree_07Aug17_Run2016F.root' , lumi = 9.8 ),
'data_Run2016G' : tnpSample('data_Run2016G' , eos2016 + 'data/TnPTree_07Aug17_Run2016G.root' , lumi = 9.8 ),
'data_Run2016H' : tnpSample('data_Run2016H' , eos2016 + 'data/TnPTree_07Aug17_Run2016H.root' , lumi = 9.8 ),
'data_Run2016BCDEFGH' : tnpSample('data_Run2016BCDEFGH' , '/eos/cms/store/group/phys_egamma/tnp/ntuples_04232018-Legacy2016/TnPTree_07Aug17_Run2016BCDEFGH.root' , lumi = 9.8 )
}
eoslivia  = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
Moriond18_v1 = {
'DY_madgraph' : tnpSample('DY_madgraph', eoslivia + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root', isMC = True, puTree = ' /eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/mc-V2/DY_madgraph_ele.pu.puTree.root',nEvts = 6854210 ),
'DY_madgraphv1' : tnpSample('DY_madgraph', eoslivia + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root', isMC = True, puTree = ' /eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/mc-V2-customW/DY_madgraph_ele.pu.puTree.root',nEvts = 6854210 ),
'data_Run2017B_new' : tnpSample('data_Run2017B_new' , eoslivia + 'data/TnPTree_17Nov2017_RunB.root' , lumi = 4.8 ),
'data_Run2017C_new' : tnpSample('data_Run2017C_new' , eoslivia + 'data/TnPTree_17Nov2017_RunC.root' , lumi = 9.8 ),
'data_Run2017D_new' : tnpSample('data_Run2017D_new' , eoslivia + 'data/TnPTree_17Nov2017_RunD.root' , lumi = 4.3 ),
'data_Run2017E_new' : tnpSample('data_Run2017E_new' , eoslivia + 'data/TnPTree_17Nov2017_RunE.root' , lumi = 9.8 ),
'data_Run2017F_new' : tnpSample('data_Run2017F_new' , eoslivia + 'data/TnPTree_17Nov2017_RunF.root' , lumi = 9.8 )
}
Legacy16 ={
'DY_madgraph' : tnpSample('DY_madgraph', eos2016 + 'TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_all.root', isMC = True, puTree = '/eos/cms/store/group/phys_egamma/tnp/ntuples_04232018-Legacy2016/Legacy16_V1/PU/DY_madgraph_Moriond17_rec.pu.puTree.root', nEvts= 5184589),
'DY_amcatnlo' : tnpSample('DY_amcatnlo', eos2016 + 'TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcnlo_all.root', isMC = True, puTree ='/eos/cms/store/group/phys_egamma/tnp/ntuples_04232018-Legacy2016/Legacy16_V1/PU/DY_amcatnlo_Moriond17_rec.pu.puTree.root', nEvts= 5184589),
'data_Run2016B' : tnpSample('data_Run2016B' , eos2016 + 'TnPTree_07Aug17_Run2016Bv2.root' , lumi = 4.8 ),
'data_Run2016C' : tnpSample('data_Run2016C' , eos2016 + 'TnPTree_07Aug17_RunC.root' , lumi = 9.8 ),
'data_Run2016D' : tnpSample('data_Run2016D' , eos2016 + 'TnPTree_07Aug17_RunD.root' , lumi = 4.3 ),
'data_Run2016E' : tnpSample('data_Run2016E' , eos2016 + 'TnPTree_07Aug17_RunE.root' , lumi = 9.8 ),
'data_Run2016F' : tnpSample('data_Run2016F' , eos2016 + 'TnPTree_07Aug17_RunF.root' , lumi = 9.8 ),
'data_Run2016G' : tnpSample('data_Run2016G' , eos2016 + 'TnPTree_07Aug17_RunG.root' , lumi = 9.8 ),
'data_Run2016H' : tnpSample('data_Run2016H' , eos2016 + 'TnPTree_07Aug17_RunH.root' , lumi = 9.8 ),

}
