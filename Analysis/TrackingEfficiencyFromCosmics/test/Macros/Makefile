CC=g++
CFLAGS=-c -O3 -Wall `root-config --cflags`
LDFLAGS=`root-config --glibs`
INCDIR=-I/uscms_data/d3/demattia/DisplacedLeptons/RefittedStandAloneMuons/Analysis/CMSSW_5_3_7/src
TREEDIR=../../../../RootTreeProducers/
OBJECTS=main.o CosmicMuonAnalyzer.o libMyLib.so
HEADERS = $(TREEDIR)/interface/Track.h $(TREEDIR)/interface/GenParticle.h

all : $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -O3 -o main

main.o: main.cpp CosmicMuonAnalyzer.h
	$(CC) $(CFLAGS) $(INCDIR) main.cpp

CosmicMuonAnalyzer.o : CosmicMuonAnalyzer.h CosmicMuonAnalyzer.cpp $(TREEDIR)/interface/Track.h $(TREEDIR)/interface/GenParticle.h
	$(CC) $(CFLAGS) $(INCDIR) CosmicMuonAnalyzer.cpp

MyDict.cxx: $(HEADERS) $(TREEDIR)/src/LinkDef.h
	rootcint -f $@ $(CFLAGS) $(INCDIR) -p $^

libMyLib.so: MyDict.cxx MyDict.h $(HEADERS) $(TREEDIR)/src/LinkDef.h
	$(CC) $(CFLAGS) $(INCDIR) MyDict.cxx -o libMyLib.so

clean:
	rm ./*.o ./*.so ./main
