from libPython.tnpClassUtils import tnpSample

### qll stat
eos2017= '/eos/cms/store/group/phys_egamma/tnp/run2017/RunBC/'

Run17 = {
    'DY_madgraph' : tnpSample('DY_madgraph', eos2017 + 'mc_27July.root', 
                              isMC = True, nEvts = 1528087 ),
    'data_Run2017B' : tnpSample('data_Run2017B' , eos2017 + 'data_RunB_27July.root' , lumi = 2.5 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eos2017 + 'data_RunC_14Aug.root', lumi = 2.5)
}
