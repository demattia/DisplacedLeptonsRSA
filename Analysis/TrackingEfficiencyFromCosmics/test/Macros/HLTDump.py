import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackingEfficiencyFromCosmics")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.categories.append("HLTrigReport")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V43::All', '')

process.hltTrigReport = cms.EDAnalyzer( 'HLTrigReport',
                                        HLTriggerResults = cms.InputTag( 'TriggerResults','','HLT' )
                                        )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:/eos/uscms/store/user/lpcdve/noreplica/Cosmics/Cosmics_Run2012A_v1_RAWtoRECO/zhenhu/Cosmics/CosmicsRun2012A_v1_RAWtoRECO/f2b0c8f0f6f7b95d1bdf24a1cf100f42/reco_RAW2DIGI_L1Reco_RECO_246_1_cO3.root'
    )
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1))


process.HLTAnalyzerEndpath = cms.EndPath( process.hltTrigReport )




    
