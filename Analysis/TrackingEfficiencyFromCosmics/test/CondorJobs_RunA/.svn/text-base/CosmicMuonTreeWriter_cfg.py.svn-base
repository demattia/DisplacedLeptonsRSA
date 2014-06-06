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
'198571:1-198571:max',
'198874:1-198874:max',
'198883:1-198883:max',
'199108:1-199108:max',
'199109:1-199109:max',
'199110:1-199110:max',
'199113:1-199113:max',
'199116:1-199116:max',
'199117:1-199117:max',
'199119:1-199119:max',
'199123:1-199123:max',
'199127:1-199127:max',
'199129:1-199129:max',
'199130:1-199130:max',
'199142:1-199142:max',
'199146:1-199146:max',
'199150:1-199150:max',
'199170:1-199170:max',
'199172:1-199172:max',
'199173:1-199173:max',
'199176:1-199176:max',
'199214:1-199214:max',
'199232:1-199232:max',
'199948:1-199948:max',
'199949:1-199949:max',
'199952:1-199952:max',
'199953:1-199953:max',
'200272:1-200272:max',
'200274:1-200274:max',
'200286:1-200286:max',
'200299:1-200299:max',
'200301:1-200301:max',
'200302:1-200302:max',
'200306:1-200306:max',
'200307:1-200307:max',
'200308:1-200308:max',
'200564:1-200564:max',
'200573:1-200573:max',
'201084:1-201084:max',
'201085:1-201085:max',
'201087:1-201087:max',
'201219:1-201219:max',
'201296:1-201296:max',
'201306:1-201306:max',
'201311:1-201311:max',
'201732:1-201732:max',
'201734:1-201734:max',
'201739:1-201739:max',
'201743:1-201743:max',
'201755:1-201755:max',
'201858:1-201858:max',
'201883:1-201883:max',
'201947:1-201947:max',
'201954:1-201954:max',
'201956:1-201956:max',
'201958:1-201958:max',
'201961:1-201961:max',
'202230:1-202230:max',
'202243:1-202243:max',
'202402:1-202402:max',
'202404:1-202404:max',
'202409:1-202409:max',
'202433:1-202433:max',
'202484:1-202484:max',
'202493:1-202493:max',
'202516:1-202516:max',
'202609:1-202609:max',
'202617:1-202617:max',
'202620:1-202620:max',
'202622:1-202622:max',
'202629:1-202629:max',
'203395:1-203395:max',
'203396:1-203396:max',
'203397:1-203397:max',
'203399:1-203399:max',
'203400:1-203400:max',
'203401:1-203401:max',
'203404:1-203404:max',
'203407:1-203407:max',
'203423:1-203423:max',
'203425:1-203425:max',
'203427:1-203427:max',
'203430:1-203430:max',
'203438:1-203438:max',
'203445:1-203445:max',
'203446:1-203446:max',
'203447:1-203447:max',
'203448:1-203448:max',
'203449:1-203449:max',
'203454:1-203454:max',
'203455:1-203455:max',
'203456:1-203456:max',
'203457:1-203457:max',
'203458:1-203458:max',
'203459:1-203459:max',
'203460:1-203460:max',
'203461:1-203461:max',
'203462:1-203462:max',
'203464:1-203464:max',
'203468:1-203468:max',
'203674:1-203674:max',
'203678:1-203678:max',
])

process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring(
"dcache:/pnfs/cms/WAX/11/store/user/yangf/Cosmics2012-RunC/INPUTFILES",
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
                              TrackCollection = cms.InputTag("generalTracks"),
                              )

process.p = cms.Path(process.demo)
