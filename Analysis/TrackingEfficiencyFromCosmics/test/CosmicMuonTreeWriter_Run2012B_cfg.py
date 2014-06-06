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
'193786:1-193786:max',
'193796:1-193796:max',
'193797:1-193797:max',
'194010:1-194010:max',
'194011:1-194011:max',
'194019:1-194019:max',
'194079:1-194079:max',
'194082:1-194082:max',
'194084:1-194084:max',
'194086:1-194086:max',
'194088:1-194088:max',
'194090:1-194090:max',
'194092:1-194092:max',
'194159:1-194159:max',
'194160:1-194160:max',
'194162:1-194162:max',
'194233:1-194233:max',
'194246:1-194246:max',
'194489:1-194489:max',
'194511:1-194511:max',
'194545:1-194545:max',
'194548:1-194548:max',
'194669:1-194669:max',
'195043:1-195043:max',
'195047:1-195047:max',
'195051:1-195051:max',
'195058:1-195058:max',
'195070:1-195070:max',
'195079:1-195079:max',
'195080:1-195080:max',
'195081:1-195081:max',
'195082:1-195082:max',
'195090:1-195090:max',
'195092:1-195092:max',
'195197:1-195197:max',
'195200:1-195200:max',
'195203:1-195203:max',
'195206:1-195206:max',
'195466:1-195466:max',
'195469:1-195469:max',
'195512:1-195512:max',
'196473:1-196473:max',
'196486:1-196486:max',
])

process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring(
"dcache:/pnfs/cms/WAX/11/store/user/zhenhu/CosmicsRun2012B/INPUTFILES",
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
