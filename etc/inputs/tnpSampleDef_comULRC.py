from libPython.tnpClassUtils import tnpSample

### qll stat
eos2017 = '/eos/cms/store/group/phys_egamma/tnp/run2017/RunBC/'
eos2017rc = '/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/'
eos2017ul = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017_AOD/'
eos2017ulmini = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017/'
eos2018rc = '/eos/cms/store/group/phys_egamma/swmukher/rereco2018/ECAL_NOISE/'
eos2018ul = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2018_ForVal_HighStat/ntuple_2018_UL_ForVal_v1/'

eos2016rc = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_04162018-Legacy2016/Legacy16_V1/'
eos2016ul = '/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/'

Run17RC = {
    'DY_madgraph' : tnpSample('DY_madgraph', eos2017rc + 'DY1JetsToLLM50madgraphMLM.root', isMC = True, nEvts = 1528087),
    'DY_mcnlo' : tnpSample('DY_mcnlo', eos2017rc + 'DYJetsToLLM50amcatnloFXFXext.root', isMC = True, nEvts = 1528087),
    'data_Run2017BRC' : tnpSample ('data_Run2017BRC', eos2017rc + 'RunB.root', lumi=7.061),
    'data_Run2017CRC' : tnpSample ('data_Run2017CRC', eos2017rc + 'RunC.root', lumi=6.895),
    'data_Run2017DRC' : tnpSample ('data_Run2017DRC', eos2017rc + 'RunD.root', lumi=31.742),
    'data_Run2017ERC' : tnpSample ('data_Run2017ERC', eos2017rc + 'RunE.root', lumi=31.742),
    'data_Run2017FRC' : tnpSample ('data_Run2017FRC', eos2017rc + 'RunF.root', lumi=31.742),
    'data_Run2017FullRC' : tnpSample ('data_Run2017FullRC', eos2017rc + 'dataRereco.root', lumi=59.402)
}

Run17UL = {
	'DY_madgraph' : tnpSample('DY_madgraph', eos2017ul + 'mc_hs.root', isMC = True, nEvts = 1528087),
	'data_Run2017BUL' : tnpSample ('data_Run2017BUL', eos2017ul + 'RunB_SingEle.root', lumi=7.061),
	'data_Run2017CUL' : tnpSample ('data_Run2017CUL', eos2017ul + 'RunC_SingEle.root', lumi=6.895),
	'data_Run2017DUL' : tnpSample ('data_Run2017DUL', eos2017ul + 'RunD_SingEle.root', lumi=31.742),
	'data_Run2017EUL' : tnpSample ('data_Run2017EUL', eos2017ul + 'RunE_SingEle.root', lumi=31.742),
	'data_Run2017FUL' : tnpSample ('data_Run2017FUL', eos2017ulmini + 'RunF_SingleElectron.root', lumi=31.742),
    #'data_Run2017FullUL' : tnpSample ('data_Run2017FullUL', eos2017ul + 'dataUL_SingEle.root', lumi=59.402)
    'data_Run2017FullUL' : tnpSample ('data_Run2017FullUL', eos2017ulmini + 'SingleElectron_BCDEF.root', lumi=59.402)
}

Run18RC = {
	'DY_madgraph' : tnpSample('DY_madgraph', eos2018rc + 'DYToEEpowheg.root', isMC = True, nEvts = 2869805),
	'data_Run2018ARC' : tnpSample ('data_Run2018ARC', eos2018rc + 'RunA.root', lumi=13.704),
	'data_Run2018BRC' : tnpSample ('data_Run2018BRC', eos2018rc + 'RunB.root', lumi=7.061),
	'data_Run2018CRC' : tnpSample ('data_Run2018CRC', eos2018rc + 'RunC.root', lumi=6.895),
	'data_Run2018DRC' : tnpSample ('data_Run2018DRC', eos2018rc + 'RunD.root', lumi=31.742),
	'data_Run2018FullRC' : tnpSample ('data_Run2018FullRC', eos2018rc + 'RunABC.root', lumi=59.402)
}

Run18UL = {
	'DY_madgraph' : tnpSample('DY_madgraph', eos2018ul + 'mc/mc.root', isMC = True, nEvts = 1528087),
	'data_Run2018AUL' : tnpSample ('data_Run2018AUL', eos2018ul + 'data/runA.root', lumi=13.704),
	'data_Run2018BUL' : tnpSample ('data_Run2018BUL', eos2018ul + 'data/runB.root', lumi=7.061),
	'data_Run2018CUL' : tnpSample ('data_Run2018CUL', eos2018ul + 'data/runC.root', lumi=6.895),
	'data_Run2018DUL' : tnpSample ('data_Run2018DUL', eos2018ul + 'data/runD.root', lumi=31.742),
	'data_Run2018FullUL' : tnpSample ('data_Run2018FullUL', eos2018ul + 'data/data.root', lumi=59.402)
}


Run16RC = {
	'DY_madgraph'        : tnpSample ('DY_madgraph',        eos2016rc + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_all.root', isMC = True, nEvts = 1528087),
	'data_Run2016BRC'    : tnpSample ('data_Run2016BRC',    eos2016rc + 'data/TnPTree_07Aug17_Run2016Bv2.root', lumi=7.061),
	'data_Run2016CRC'    : tnpSample ('data_Run2016CRC',    eos2016rc + 'data/TnPTree_07Aug17_Run2016C.root', lumi=6.895),
	'data_Run2016DRC'    : tnpSample ('data_Run2016DRC',    eos2016rc + 'data/TnPTree_07Aug17_Run2016D.root', lumi=31.742),
	'data_Run2016ERC'    : tnpSample ('data_Run2016ERC',    eos2016rc + 'data/TnPTree_07Aug17_Run2016E.root', lumi=31.742),
	'data_Run2016FRC'    : tnpSample ('data_Run2016FRC',    eos2016rc + 'data/TnPTree_07Aug17_Run2016F.root', lumi=31.742),
	'data_Run2016GRC'    : tnpSample ('data_Run2016GRC',    eos2016rc + 'data/TnPTree_07Aug17_Run2016G.root', lumi=31.742),
	'data_Run2016HRC'    : tnpSample ('data_Run2016HRC',    eos2016rc + 'data/TnPTree_07Aug17_Run2016H.root', lumi=31.742),
	'data_Run2016FullRC' : tnpSample ('data_Run2016FullRC', eos2016rc + 'data/TnPTree_07Aug17_Run2016BCDEFGH.root', lumi=59.402)
}
Run16UL = {
	'DY_madgraphB' : tnpSample('DY_madgraphB', eos2016ul + 'UL16_preVFP_v3_nohlt/RelValZEE_preVFP.root', isMC = True, nEvts = 1528087),
	'DY_madgraphC' : tnpSample('DY_madgraphC', eos2016ul + 'UL16_preVFP_v3_nohlt/RelValZEE_preVFP.root', isMC = True, nEvts = 1528087),
	'DY_madgraphD' : tnpSample('DY_madgraphD',  eos2016ul + 'UL16_preVFP_v3_nohlt/RelValZEE_preVFP.root', isMC = True, nEvts = 1528087),
	'DY_madgraphE' : tnpSample('DY_madgraphE',  eos2016ul + 'UL16_preVFP_v3_nohlt/RelValZEE_preVFP.root', isMC = True, nEvts = 1528087),
	'DY_madgraphF' : tnpSample('DY_madgraphF',  eos2016ul + 'UL16_preVFP_v3_nohlt/RelValZEE_preVFP.root', isMC = True, nEvts = 1528087),
	'DY_madgraphG' : tnpSample('DY_madgraphG',  eos2016ul + 'UL16_postVFP_v9_nohlt/RelValZEE_postVFP.root', isMC = True, nEvts = 1528087),
	'DY_madgraphH' : tnpSample('DY_madgraphH',  eos2016ul + 'UL16_postVFP_v9_nohlt/RelValZEE_postVFP.root', isMC = True, nEvts = 1528087),
	'DY_madgraphFull' : tnpSample('DY_madgraphFull',  eos2016ul + 'UL16_postVFP_v9_nohlt/RelValZEE_postVFP.root', isMC = True, nEvts = 1528087),
	
	'data_Run2016BUL' : tnpSample ('data_Run2016BUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunB_HIPM.root', lumi=7.061),
	'data_Run2016CUL' : tnpSample ('data_Run2016CUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunC_HIPM.root', lumi=6.895),
	'data_Run2016DUL' : tnpSample ('data_Run2016DUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunD_HIPM.root', lumi=31.742),
	'data_Run2016EUL' : tnpSample ('data_Run2016EUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunE_HIPM.root', lumi=31.742),
	'data_Run2016FUL' : tnpSample ('data_Run2016FUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunF_HIPM.root', lumi=31.742),
        'data_Run2016BFUL' : tnpSample ('data_Run2016BFUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunBF_HIPM.root', lumi=7.061),
	'data_Run2016GUL' : tnpSample ('data_Run2016GUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunG.root', lumi=31.742),
	'data_Run2016HUL' : tnpSample ('data_Run2016HUL',  eos2016ul + 'UL2016_ForVal_SingleEle/RunH.root', lumi=31.742),
	'data_Run2016FullUL' : tnpSample ('data_Run2016FullUL', eos2016ul + 'SingleElectron_BCDEF.root', lumi=59.402)
}
