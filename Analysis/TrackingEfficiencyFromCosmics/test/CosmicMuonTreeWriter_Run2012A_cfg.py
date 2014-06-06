import FWCore.ParameterSet.Config as cms

process = cms.Process("CosmicMuonTreeWriter")

# # initialize MessageLogger and output report
# process.load("FWCore.MessageLogger.MessageLogger_cfi")
# # process.MessageLogger.cerr.threshold = 'INFO'
# # process.MessageLogger.categories.append('Demo')
# # process.MessageLogger.cerr.INFO = cms.untracked.PSet(
# #     limit = cms.untracked.int32(-1)
# # )

process.load("FWCore.MessageService.test.Services_cff")
# Here is the configuration of the MessgeLogger Service:
process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('Message'),
    Message = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    )
)

process.load("Configuration.StandardSequences.Services_cff")
process.load('Configuration.StandardSequences.Reconstruction_cff')

process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
# process.load('Configuration.StandardSequences.MagneticField_cff')


# Careful, this needs to be changed for the data
process.GlobalTag.globaltag = 'GR_P_V43::All'

# process.load("MagneticField.Engine.uniformMagneticField_cfi")

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(TOTEVENTS) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

lumiSecs = cms.untracked.VLuminosityBlockRange()

lumiSecs.extend([
'191101:1-191101:max',
'191107:1-191107:max',
'191112:1-191112:max',
'191115:1-191115:max',
'191123:1-191123:max',
'191148:1-191148:max',
'191545:1-191545:max',
'192779:1-192779:max',
'192784:1-192784:max',
'192807:1-192807:max',
'192822:1-192822:max',
'192831:1-192831:max',
'192863:1-192863:max',
'192864:1-192864:max',
'192871:1-192871:max',
'192872:1-192872:max',
'192873:1-192873:max',
'192875:1-192875:max',
'192879:1-192879:max',
'193000:1-193000:max',
'193014:1-193014:max',
'193015:1-193015:max',
'193023:1-193023:max',
'193224:1-193224:max',
'193343:1-193343:max',
'193347:1-193347:max',
'193350:1-193350:max',
'193355:1-193355:max',
'193477:1-193477:max',
'193478:1-193478:max',
'193488:1-193488:max',
'193489:1-193489:max',
'193490:1-193490:max',
'193498:1-193498:max',
'193500:1-193500:max',
'193504:1-193504:max',
'193507:1-193507:max',
'193508:1-193508:max',
'193514:1-193514:max',
'193515:1-193515:max',
'193516:1-193516:max',
'193546:1-193546:max',
'193579:1-193579:max',
'193627:1-193627:max',
'193691:1-193691:max',
'193692:1-193692:max',
'193693:1-193693:max',
'193694:1-193694:max',
'193697:1-193697:max',
])

process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring(
"dcache:/pnfs/cms/WAX/11/store/user/zhenhu/CosmicsRun2012A/INPUTFILES",
		),  
#        skipEvents = cms.untracked.uint32(SKIPEVENTS),
		lumisToProcess = lumiSecs
                            )

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
                                            MaxDPhi = cms.double(1.6),
                                            ComponentName = cms.string('PropagatorWithMaterial'),
                                            Mass = cms.double(0.105),
                                            PropagationDirection = cms.string('alongMomentum'),
                                            useRungeKutta = cms.bool(False),
                                            # If ptMin > 0, uncertainty in reconstructed momentum will be taken into account when estimating rms scattering angle.
                                            # (By default, it is neglected). However, it will also be assumed that the track pt can't be below specified value,
                                            # to prevent this scattering angle becoming too big.
                                            ptMin = cms.double(-1.)
                                            )

process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
                                                    ComponentName = cms.string('SteppingHelixPropagatorAny'),
                                                    NoErrorPropagation = cms.bool(False),
                                                    PropagationDirection = cms.string('anyDirection'),
                                                    useTuningForL2Speed = cms.bool(False),
                                                    useIsYokeFlag = cms.bool(True),
                                                    endcapShiftInZNeg = cms.double(0.0),
                                                    SetVBFPointer = cms.bool(False),
                                                    AssumeNoMaterial = cms.bool(False),
                                                    endcapShiftInZPos = cms.double(0.0),
                                                    useInTeslaFromMagField = cms.bool(False),
                                                    VBFName = cms.string('VolumeBasedMagneticField'),
                                                    useEndcapShiftsInZ = cms.bool(False),
                                                    sendLogWarning = cms.bool(False),
                                                    useMatVolumes = cms.bool(True),
                                                    debug = cms.bool(False),
                                                    #This sort of works but assumes a measurement at propagation origin
                                                    ApplyRadX0Correction = cms.bool(True),
                                                    useMagVolumes = cms.bool(True),
                                                    returnTangentPlane = cms.bool(True)
                                                    )

# Smart propagator with IP
process.smartPropagatorWithIPESProducer = cms.ESProducer("SmartPropagatorWithIPESProducer",
                                                         ComponentName = cms.string('SmartPropagatorWithIP'),
                                                         TrackerPropagator = cms.string('PropagatorWithMaterial'),
                                                         # TrackerPropagator = cms.string('RungeKuttaTrackerPropagator'),
                                                         MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
                                                         PropagationDirection = cms.string('alongMomentum'),
                                                         Epsilon = cms.double(10.0) # the standard one has 5., but uses 10 hardcoded internally...
                                                         )

process.demo = cms.EDAnalyzer('CosmicMuonTreeWriter',
                              UseMCtruth = cms.bool(False),
                              RecomputeIP = cms.bool(False),
                              OutPutName = cms.InputTag("cosmicMuons1Leg_NUMBER"),
                              # MuonCollection = cms.InputTag("standAloneMuons"),
                              # MuonCollection = cms.InputTag("muons1Leg"),
                              MuonCollection = cms.InputTag("cosmicMuons1Leg"),
                              # TrackCollection = cms.InputTag("ALCARECOTkAlCosmicsCTF0T"),
                              TrackCollection = cms.InputTag("refittedStandAloneMuons"),
                              RecoMuonCollection  = cms.InputTag("muons"),
                              timeExtraSrc = cms.InputTag("muons"),
                              )

process.p = cms.Path(process.demo)
