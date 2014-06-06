import math
import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events(
    [
    # 'file:/eos/uscms/store/user/lpcdve/noreplica/Cosmics/Cosmics_Run2012A_v1_RAWtoRECO/zhenhu/Cosmics/CosmicsRun2012A_v1_RAWtoRECO/f2b0c8f0f6f7b95d1bdf24a1cf100f42/reco_RAW2DIGI_L1Reco_RECO_436_1_Hiu.root',
    # 'file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Cosmics/MuonGun_118.root',
    'file:/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_8/src/Analysis/TrackingEfficiencyFromCosmics/test/Macros/TreeAnalyzers/NewMC/MuonGun_1.root'
    ]
)

# create handle outside of loop
handleTrigger = Handle ('edm::TriggerResults')

# a label is just a tuple of strings that is initialized just like an edm::InputTag
labelTrigger = ("TriggerResults")

# Disable drawing to the screen
# ROOT.gROOT.SetBatch()        # don't pop up canvases

# Create histograms, etc.
ROOT.gROOT.SetStyle('Plain') # white background
# Note that the genParticle distances are in mm

passTrigger = 0
totalEvents = 0
# loop over events
for event in events:
    totalEvents += 1
    try:
        # Note that there are also triggerResults for SIM and RECO which are not needed here. Take the HLT results.
        # If not specified it will take the last one by default which is the RECO.
        event.getByLabel(labelTrigger, "", "HLT", handleTrigger)
        triggerResults = handleTrigger.product()
        # print "number of paths = ", triggerResults.size()
    except:
        print "trigger results error"
        continue

    print "Analyzing event", totalEvents

    if triggerResults.accept(415):
        passTrigger += 1

triggerEfficiency = passTrigger/float(totalEvents)
print "trigger efficiency =", triggerEfficiency, "+/-", math.sqrt(triggerEfficiency*(1-triggerEfficiency)/totalEvents)
