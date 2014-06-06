#ifndef TRACK_H
#define TRACK_H

#include <TObject.h>
#include <TLorentzVector.h>

/**
 * Simple class used to save a track in a root tree. <br>
 */

/// Class to be saved in the tree
class Track : public TObject
{
public:
  Track() :
    nDof(-999),
    timeAtIpInOut(-999), timeAtIpInOutErr(-999),
    timeAtIpOutIn(-999), timeAtIpOutInErr(-999),
    timeAtIpInOutC(-999), timeAtIpInOutErrC(-999),
    timeAtIpOutInC(-999), timeAtIpOutInErrC(-999),
    inverseBeta(-999), inverseBetaErr(-999),
    freeInverseBeta(-999), freeInverseBetaErr(-999),
    minDxIn(-999), minDyIn(-999), minDzIn(-999),
    minDxOut(-999), minDyOut(-999), minDzOut(-999)
    {}

  double pt, ptError, eta, etaError, phi, phiError;
  int charge;
  double dxy, dxyError, dz, dzError;
  double vx, vy, vz;
  double chi2, normalizedChi2;
  double referencePointRadius, referencePointZ;
  int nHits, nValidHits, nValidPlusInvalidHits;
  double innermostHitRadius, innermostHitZ;
  int muonStationsWithAnyHits;
  // int dtStationsWithAnyHits;
  // int cscStationsWithAnyHits;
  int dtStationsWithValidHits;
  int cscStationsWithValidHits;
  int trackAlgorithm;
  bool trackQuality;
  int nDof;
  double timeAtIpInOut,  timeAtIpInOutErr;
  double timeAtIpOutIn,  timeAtIpOutInErr;
  double timeAtIpInOutC, timeAtIpInOutErrC;
  double timeAtIpOutInC, timeAtIpOutInErrC;
  double inverseBeta, inverseBetaErr;
  double freeInverseBeta, freeInverseBetaErr;
  double minDxIn, minDyIn, minDzIn;
  double minDxOut, minDyOut, minDzOut;

  ClassDef(Track, 2)
};
ClassImp(Track)

#endif // TRACK_H
