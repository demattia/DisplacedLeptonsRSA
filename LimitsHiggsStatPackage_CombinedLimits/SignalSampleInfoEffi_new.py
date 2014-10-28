# === This file was created by the script parseEfficiencyFiles.pl ===
#
s = SignalSampleInfo(125, 50, 500, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000002 ,  0.000013 ,  0.000040 ,  0.000423 ,  0.001549 , 
 0.002339 ,  0.002771 ,  0.002977 ,  0.003254 ,  0.002311 ,  0.001743 ,  0.001392 ,  0.001158 , 
 0.000800 ,  0.000414 ,  0.000279 ,  0.000210 ,  0.000169 ,  0.000085 ,  0.000042 ,  0.000028 , 
 0.000021 ,  0.000017 ,  0.000008 ,  0.000004 ,  0.000003 ,  0.000002 ,  0.000002 ] )
s.setEffiRelErrs (       "Muons", [
 1.030293 ,  1.030293 ,  1.030293 ,  0.531305 ,  0.345938 ,  0.327775 ,  0.276960 ,  0.261819 , 
 0.258772 ,  0.257889 ,  0.257568 ,  0.275597 ,  0.273886 ,  0.273572 ,  0.273527 ,  0.273148 , 
 0.388699 ,  0.389459 ,  0.387735 ,  0.389486 ,  0.386875 ,  0.385198 ,  0.397119 ,  0.378886 , 
 0.378909 ,  0.384922 ,  0.453223 ,  0.356880 ,  0.416277 ,  0.560976 ,  0.566159 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)