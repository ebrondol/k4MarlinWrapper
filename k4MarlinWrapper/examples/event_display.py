#!/usr/bin/env python3

from Gaudi.Configuration import *

from Configurables import MarlinProcessorWrapper, k4DataSvc, PodioInput, EDM4hep2LcioTool
algList = []

evtsvc = k4DataSvc('EventDataSvc')
evtsvc.input = ''

inp = PodioInput('InputReader')
inp.collections = [
  'EventHeader',
  'MCParticles',
  'VertexBarrelCollection',
  'VertexEndcapCollection',
  'InnerTrackerBarrelCollection',
  'OuterTrackerBarrelCollection',
  'InnerTrackerEndcapCollection',
  'OuterTrackerEndcapCollection',
  'ECalEndcapCollection',
  'ECalEndcapCollectionContributions',
  'ECalBarrelCollection',
  'ECalBarrelCollectionContributions',
  'ECalPlugCollection',
  'ECalPlugCollectionContributions',
  'HCalBarrelCollection',
  'HCalBarrelCollectionContributions',
  'HCalEndcapCollection',
  'HCalEndcapCollectionContributions',
  'HCalRingCollection',
  'HCalRingCollectionContributions',
  'YokeBarrelCollection',
  'YokeBarrelCollectionContributions',
  'YokeEndcapCollection',
  'YokeEndcapCollectionContributions',
  'LumiCalCollection',
  'LumiCalCollectionContributions',
  'BeamCalCollection',
  'BeamCalCollectionContributions',
]

MyInitializeDD4hep = MarlinProcessorWrapper("MyInitializeDD4hep")
MyInitializeDD4hep.OutputLevel = INFO
MyInitializeDD4hep.ProcessorType = "InitializeDD4hep"
MyInitializeDD4hep.Parameters = {
                                 "DD4hepXMLFile": ["CLICPerformance/Visualisation/CLIC_o3_v06_CED/CLIC_o3_v06_CED.xml"]
                                 }

MyEventSelector = MarlinProcessorWrapper("MyEventSelector")
MyEventSelector.OutputLevel = INFO
MyEventSelector.ProcessorType = "EventSelector"
MyEventSelector.Parameters = {
                              "EventList": ["28", "0", "33", "0", "52", "0", "63", "0", "73", "0", "78", "0"]
                              }

MyCEDViewer = MarlinProcessorWrapper("MyCEDViewer")
MyCEDViewer.OutputLevel = INFO
MyCEDViewer.ProcessorType = "DDCEDViewer"
MyCEDViewer.Parameters = {
                          "ColorByEnergy": ["false"],
                          "ColorByEnergyAutoColor": ["false"],
                          "ColorByEnergyBrightness": ["1.0"],
                          "ColorByEnergyMax": ["35.0"],
                          "ColorByEnergyMin": ["0.0"],
                          "ColorByEnergySaturation": ["1.0"],
                          "ColorScheme": ["10"],
                          "DetailledDrawing": ["VXD", "VertexBarrel"],
                          "DrawDetector": ["true"],
                          "DrawDetectorID": ["0"],
                          "DrawHelixForPFOs": ["0"],
                          "DrawHelixForTrack": ["0"],
                          "DrawInLayer": [
                              "VXDCollection", "0", "5", "1",
                              "SITCollection", "0", "5", "1",
                              "FTD_PIXELCollection", "0", "5", "1",
                              "FTD_STRIPCollection", "0", "5", "1",
                              "FTDCollection", "0", "5", "1",
                              "TPCCollection", "0", "3", "1",
                              "SETCollection", "0", "3", "1",
                              "ETDCollection", "0", "3", "1",
                              "VertexBarrelCollection", "0", "5", "1",
                              "VertexEndcapCollection", "0", "5", "1",
                              "InnerTrackerBarrelCollection", "0", "5", "1",
                              "InnerTrackerEndcapCollection", "0", "5", "1",
                              "OuterTrackerBarrelCollection", "0", "5", "1",
                              "OuterTrackerEndcapCollection", "0", "5", "1",
                              "VXDTrackerHits", "0", "5", "11",
                              "SITTrackerHits", "0", "5", "11",
                              "TPCTrackerHits", "0", "5", "11",
                              "FTDTrackerHits", "0", "5", "11",
                              "FTDStripTrackerHits", "0", "5", "11",
                              "FTDPixelTrackerHits", "0", "5", "11",
                              "FTDSpacePoints", "0", "5", "11",
                              "SETTrackerHits", "0", "5", "11",
                              "ITrackerEndcapHits", "0", "5", "11",
                              "ITrackerHits", "0", "5", "11",
                              "OTrackerEndcapHits", "0", "5", "11",
                              "OTrackerHits", "0", "5", "11",
                              "VXDEndcapTrackerHits", "0", "5", "11",
                              "LHcalCollection", "0", "3", "2",
                              "LumiCalCollection", "0", "3", "2",
                              "MuonBarrelCollection", "0", "3", "2",
                              "MuonEndCapCollection", "0", "3", "2",
                              "EcalBarrelSiliconCollection", "0", "3", "2",
                              "EcalBarrelSiliconPreShower", "0", "3", "2",
                              "EcalEndcapRingCollection", "0", "3", "2",
                              "EcalEndcapRingPreShower", "0", "3", "2",
                              "EcalEndcapSiliconCollection", "0", "3", "2",
                              "EcalEndcapSiliconPreShower", "0", "3", "2",
                              "HcalBarrelRegCollection", "0", "3", "2",
                              "HcalEndCapRingCollection", "0", "3", "2",
                              "HcalEndCapsCollection", "0", "3", "2",
                              "HcalEndcapRingCollection", "0", "3", "2",
                              "HcalEndcapsCollection", "0", "3", "2",
                              "ECalBarrelSiHitsEven", "0", "3", "2",
                              "ECalBarrelSiHitsOdd", "0", "3", "2",
                              "ECalEndcapSiHitsEven", "0", "3", "2",
                              "ECalEndcapSiHitsOdd", "0", "3", "2",
                              "EcalBarrelCollection", "0", "3", "2",
                              "EcalEndcapsCollection", "0", "3", "2",
                              "YokeEndcapsCollection", "0", "3", "2",
                              "ECalBarrelCollection", "0", "3", "2",
                              "ECalEndcapCollection", "0", "3", "2",
                              "ECalPlugCollection", "0", "3", "2",
                              "EcalBarrelCollection", "0", "3", "2",
                              "EcalEndcapCollection", "0", "3", "2",
                              "EcalPlugCollection", "0", "3", "2",
                              "HCalBarrelCollection", "0", "3", "2",
                              "HCalEndcapCollection", "0", "3", "2",
                              "HCalRingCollection", "0", "3", "2",
                              "YokeBarrelCollection", "0", "3", "2",
                              "YokeEndcapCollection", "0", "3", "2",
                              "LumiCalCollection", "0", "3", "2",
                              "BeamCalCollection", "0", "3", "2",
                              "HCALEndcap", "0", "5", "12",
                              "HCALOther", "0", "5", "12",
                              "MUON", "0", "2", "12",
                              "LHCAL", "0", "3", "12",
                              "LCAL", "0", "3", "12",
                              "BCAL", "0", "3", "12",
                              "ECALBarrel", "0", "2", "12",
                              "ECALEndcap", "0", "2", "12",
                              "ECALOther", "0", "2", "12",
                              "HCALBarrel", "0", "5", "12",
                              "EcalBarrelCollectionRec", "0", "5", "12",
                              "EcalEndcapRingCollectionRec", "0", "5", "12",
                              "EcalEndcapsCollectionRec", "0", "5", "12",
                              "HcalBarrelCollectionRec", "0", "5", "12",
                              "HcalEndcapRingCollectionRec", "0", "5", "12",
                              "HcalEndcapsCollectionRec", "0", "5", "12",
                              "TruthTracks", "0", "6", "3",
                              "ForwardTracks", "0", "6", "4",
                              "SiTracks", "0", "6", "5",
                              "ClupatraTracks", "0", "6", "6",
                              "MarlinTrkTracks", "0", "6", "7",
                              "PandoraClusters", "0", "3", "8",
                              "PandoraPFOs", "0", "3", "9",
                              "MCParticle", "0", "3", "0",
                              "VertexBarrelHits", "0", "5", "11",
                              "VertexEndcapHits", "0", "5", "11",
                              "InnerTrackerBarrelHits", "0", "5", "11",
                              "InnerTrackerEndcapHits", "0", "5", "11",
                              "OuterTrackerBarrelHits", "0", "5", "11",
                              "OuterTrackerEndcapHits", "0", "5", "11",
                              "ECalBarrelHits", "0", "3", "12",
                              "ECalEndcapHits", "0", "3", "12",
                              "ECalPlugHits", "0", "3", "12",
                              "HCalBarrelHits", "0", "3", "12",
                              "HCalEndcapHits", "0", "3", "12",
                              "HCalRingHits", "0", "3", "12",
                              "YokeBarrelHits", "0", "3", "12",
                              "YokeEndcapHits", "0", "3", "12",
                              "LumiCalHits", "0", "3", "12",
                              "BeamCalHits", "0", "3", "12",
                              "Tracks", "0", "3", "3",
                              "SelectedPandoraPFOCollection", "0", "3", "4",
                              "LooseSelectedPandoraPFOCollection", "0", "3", "5",
                              "TightSelectedPandoraPFOCollection", "0", "3", "6",
                              "PandoraPFOCollection", "0", "3", "7",
                              "JetOut", "0", "0", "3"],
                          "DrawSurfaces": ["true"],
                          "HelixMaxR": ["2000"],
                          "HelixMaxZ": ["2500"],
                          "MCParticleEnergyCut": ["0.001"],
                          "ScaleLineThickness": ["1"],
                          "ScaleMarkerSize": ["1"],
                          "UseColorForHelixTracks": ["0"],
                          "UseTPCForLimitsOfHelix": ["true"],
                          "UsingParticleGun": ["false"],
                          "WaitForKeyboard": ["1"]
                          }

# EDM4hep to LCIO converter
edmConvTool = EDM4hep2LcioTool("EDM4hep2lcio")
edmConvTool.convertAll = True
edmConvTool.collNameMapping = {'MCParticles': 'MCParticle'}
edmConvTool.OutputLevel = DEBUG
MyCEDViewer.EDM4hep2LcioTool = edmConvTool

algList.append(inp)
algList.append(MyInitializeDD4hep)
algList.append(MyCEDViewer)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=INFO
              )