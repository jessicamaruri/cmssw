import FWCore.ParameterSet.Config as cms

ecalBarrelMonitorClient = cms.EDAnalyzer("EcalBarrelMonitorClient",
    inputFile = cms.untracked.string(''),
    dbName = cms.untracked.string(''),
    dbHostName = cms.untracked.string(''),
    dbHostPort = cms.untracked.int32(1521),
    dbUserName = cms.untracked.string(''),
    dbPassword = cms.untracked.string(''),
    dbTagName = cms.untracked.string('CMSSW'),
    mergeRuns = cms.untracked.bool(False),
    location = cms.untracked.string(''),
    cloneME = cms.untracked.bool(False),
    updateTime = cms.untracked.int32(0),
    dbUpdateTime = cms.untracked.int32(0),
    enabledClients = cms.untracked.vstring('Integrity', 
        'StatusFlags', 
        'Occupancy', 
        'PedestalOnline', 
        'Pedestal', 
        'TestPulse', 
        'Laser', 
        'Timing', 
        'Cosmic', 
        'BeamCalo', 
        'BeamHodo', 
        'Summary'),
    prefixME = cms.untracked.string('EcalBarrel'),
    enableCleanup = cms.untracked.bool(False),
    superModules = cms.untracked.vint32(1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36),
    laserWavelengths = cms.untracked.vint32(1, 2, 3, 4),
    MGPAGains = cms.untracked.vint32(1, 6, 12),
    MGPAGainsPN = cms.untracked.vint32(1, 16),                                         
    verbose = cms.untracked.bool(True),
    debug = cms.untracked.bool(False),
    prescaleFactor = cms.untracked.int32(1)
)

