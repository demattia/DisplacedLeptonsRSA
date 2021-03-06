# === This file was created by the script parseEfficiencyFiles.pl ===
#
s = SignalSampleInfoRSA(1500, 494, 160, 1)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.000001 ,  0.000093 ,  0.001406 ,  0.004150 ,  0.007528 ,  0.010970 ,  0.023780 ,  0.031410 , 
 0.030660 ,  0.028120 ,  0.025400 ,  0.015488 ,  0.007548 ,  0.004793 ,  0.003515 ,  0.002796 , 
 0.001456 ,  0.000797 ,  0.000561 ,  0.000435 ,  0.000356 ] )
s.setEffiRelErrs (       "Muons", [
 0.892810 ,  0.332304 ,  0.237640 ,  0.203341 ,  0.192422 ,  0.188045 ,  0.183119 ,  0.182074 , 
 0.181879 ,  0.181816 ,  0.181802 ,  0.181941 ,  0.185606 ,  0.191191 ,  0.195308 ,  0.197591 , 
 0.198278 ,  0.192564 ,  0.188859 ,  0.186861 ,  0.185934 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000006 ,  0.000057 ,  0.000147 ,  0.000259 ,  0.000377 ,  0.000853 ,  0.001208 , 
 0.001213 ,  0.001124 ,  0.001015 ,  0.000636 ,  0.000282 ,  0.000172 ,  0.000124 ,  0.000098 , 
 0.000051 ,  0.000028 ,  0.000020 ,  0.000016 ,  0.000013 ] )
samples.append(s)
#
s = SignalSampleInfoRSA(1000, 148, 60, 1)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.000000 ,  0.000007 ,  0.000287 ,  0.001204 ,  0.002562 ,  0.004162 ,  0.012750 ,  0.023670 , 
 0.027440 ,  0.028010 ,  0.027260 ,  0.020141 ,  0.012033 ,  0.008549 ,  0.006671 ,  0.005495 , 
 0.002981 ,  0.001586 ,  0.001085 ,  0.000826 ,  0.000666 ] )
s.setEffiRelErrs (       "Muons", [
 1.016248 ,  0.788960 ,  0.430593 ,  0.387432 ,  0.331157 ,  0.284909 ,  0.204859 ,  0.189583 , 
 0.187574 ,  0.187070 ,  0.186995 ,  0.187061 ,  0.189713 ,  0.191071 ,  0.191665 ,  0.191927 , 
 0.192504 ,  0.193114 ,  0.193592 ,  0.193900 ,  0.193898 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000001 ,  0.000004 ,  0.000104 ,  0.000408 , 
 0.000554 ,  0.000591 ,  0.000582 ,  0.000420 ,  0.000240 ,  0.000173 ,  0.000137 ,  0.000115 , 
 0.000066 ,  0.000037 ,  0.000026 ,  0.000020 ,  0.000016 ] )
samples.append(s)
#
s = SignalSampleInfoRSA(350, 148, 173, 1)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.000003 ,  0.000083 ,  0.000789 ,  0.002203 ,  0.004050 ,  0.006051 ,  0.014050 ,  0.019290 , 
 0.019480 ,  0.018480 ,  0.017270 ,  0.012332 ,  0.007438 ,  0.005247 ,  0.004050 ,  0.003302 , 
 0.001733 ,  0.000900 ,  0.000610 ,  0.000461 ,  0.000371 ] )
s.setEffiRelErrs (       "Muons", [
 0.820425 ,  0.515337 ,  0.289128 ,  0.229522 ,  0.210211 ,  0.201926 ,  0.191687 ,  0.187974 , 
 0.186790 ,  0.186308 ,  0.186129 ,  0.186739 ,  0.194784 ,  0.199283 ,  0.200947 ,  0.201300 , 
 0.199343 ,  0.197160 ,  0.196856 ,  0.197249 ,  0.197262 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000002 ,  0.000033 ,  0.000093 ,  0.000168 ,  0.000249 ,  0.000620 ,  0.000913 , 
 0.000922 ,  0.000852 ,  0.000768 ,  0.000513 ,  0.000250 ,  0.000163 ,  0.000122 ,  0.000098 , 
 0.000051 ,  0.000027 ,  0.000018 ,  0.000014 ,  0.000011 ] )
samples.append(s)
#
s = SignalSampleInfoRSA(120, 48, 165, 1)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.000000 ,  0.000003 ,  0.000098 ,  0.000351 ,  0.000691 ,  0.001036 ,  0.002178 ,  0.002748 , 
 0.002667 ,  0.002473 ,  0.002276 ,  0.001623 ,  0.000895 ,  0.000588 ,  0.000434 ,  0.000343 , 
 0.000170 ,  0.000086 ,  0.000058 ,  0.000044 ,  0.000035 ] )
s.setEffiRelErrs (       "Muons", [
 1.016248 ,  0.631307 ,  0.440915 ,  0.336668 ,  0.303223 ,  0.287980 ,  0.248953 ,  0.223666 , 
 0.217577 ,  0.215232 ,  0.214531 ,  0.216529 ,  0.238123 ,  0.248621 ,  0.251760 ,  0.253189 , 
 0.245664 ,  0.236166 ,  0.238455 ,  0.226654 ,  0.230664 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000002 ,  0.000009 ,  0.000020 ,  0.000093 ,  0.000162 , 
 0.000173 ,  0.000162 ,  0.000146 ,  0.000101 ,  0.000042 ,  0.000024 ,  0.000017 ,  0.000013 , 
 0.000006 ,  0.000003 ,  0.000002 ,  0.000001 ,  0.000001 ] )
samples.append(s)
