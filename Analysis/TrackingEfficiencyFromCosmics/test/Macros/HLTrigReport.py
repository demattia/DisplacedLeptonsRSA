import FWCore.ParameterSet.Config as cms

process = cms.Process("REPORT")

process.load("FWCore.MessageService.MessageLogger_cfi")
# process.MessageLogger.cerr.FwkReport.reportEvery = 999999999
process.MessageLogger.categories.append('HLTrigReport')

process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(False)
            )

process.source = cms.Source("PoolSource",
                                                        fileNames = cms.untracked.vstring(
    # 'file:/eos/uscms/store/user/lpcdve/noreplica/Cosmics/Cosmics_Run2012A_v1_RAWtoRECO/zhenhu/Cosmics/CosmicsRun2012A_v1_RAWtoRECO/f2b0c8f0f6f7b95d1bdf24a1cf100f42/reco_RAW2DIGI_L1Reco_RECO_436_1_Hiu.root',
    # 'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Cosmics/MuonGun_118.root',
    'file:/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/MuonGun_1.root'
        ),
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
                            )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32( -1 )
        )

process.load('Configuration/StandardSequences/GeometryExtended_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration/StandardSequences/SimL1Emulator_cff')
process.GlobalTag.globaltag = "START52_V9::All"
process.GlobalTag.toGet = cms.VPSet(
        cms.PSet(record = cms.string("HeavyIonRcd"),
                              tag = cms.string("CentralityTable_HFhits40_Hydjet2760GeV_v0_mc"),
                              connect = cms.untracked.string("frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS")
                              )
            )


process.load( "HLTrigger.HLTanalyzers.hlTrigReport_cfi" )
process.hlTrigReport.HLTriggerResults = cms.InputTag("TriggerResults", "", "HLT")
process.hlTrigReport.ReferencePath = cms.untracked.string( "HLTriggerFinalPath" )
process.hlTrigReport.ReferenceRate = cms.untracked.double( 100.0 )
# process.hlTrigReport.ReportEvery = "lumi"

process.report = cms.EndPath( process.hlTrigReport )
