# === This file was created by the script parseEfficiencyFiles.pl ===
#
s = SignalSampleInfo(1000, 350, 35, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.077920 ,  0.149600 ,  0.238000 ,  0.289200 ,  0.321300 ,  0.342700 ,  0.386600 ,  0.392400 , 
 0.378300 ,  0.361700 ,  0.345600 ,  0.271000 ,  0.206900 ,  0.139200 ,  0.119400 , 
 0.072210 ,  0.039290 ,  0.027060 ,  0.008698 ,  0.004481 ,  0.003027 , 
 0.002286 ,  0.001837 ,  0.000927 ,  0.000466 ,  0.000311 ,  0.000234 ,  0.000187 ] )
s.setEffiRelErrs (       "Electrons", [
 0.212224 ,  0.152354 ,  0.121460 ,  0.113000 ,  0.109405 ,  0.107472 ,  0.104124 ,  0.102804 , 
 0.102486 ,  0.102405 ,  0.102437 ,  0.106827 ,  0.106194 ,  0.106279 ,  0.106478 ,  0.106696 , 
 0.135850 ,  0.137211 ,  0.137790 ,  0.138986 ,  0.140335 ,  0.141254 , 
 0.141808 ,  0.142133 ,  0.143033 ,  0.144188 ,  0.143409 ,  0.142524 ,  0.144723 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000026 ,  0.000267 ,  0.000573 ,  0.000875 ,  0.001161 ,  0.002207 ,  0.002942 , 
 0.003130 ,  0.003175 ,  0.003149 ,  0.000762 ,  0.000989 ,  0.001054 ,  0.001037 ,  0.000988 , 
 0.002260 ,  0.001227 ,  0.000845 ,  0.000272 ,  0.000140 ,  0.000095 , 
 0.000071 ,  0.000057 ,  0.000029 ,  0.000015 ,  0.000010 ,  0.000007 ,  0.000006 ] )
s.setEffis (             "Muons", [
 0.090360 ,  0.198400 ,  0.315800 ,  0.372000 ,  0.404000 ,  0.424800 ,  0.470600 ,  0.488400 , 
 0.484000 ,  0.474100 ,  0.462400 ,  0.404500 ,  0.325000 ,  0.226200 ,  0.195400 , 
 0.127600 ,  0.070540 ,  0.048810 ,  0.015718 ,  0.008059 ,  0.005425 , 
 0.004090 ,  0.003282 ,  0.001652 ,  0.000829 ,  0.000553 ] )
s.setEffiRelErrs (       "Muons", [
 0.188844 ,  0.139932 ,  0.117659 ,  0.111447 ,  0.108677 ,  0.107134 ,  0.104394 ,  0.103315 , 
 0.103053 ,  0.102987 ,  0.103020 ,  0.105297 ,  0.104773 ,  0.104869 ,  0.105018 , 
 0.124536 ,  0.126016 ,  0.126630 ,  0.129614 ,  0.132740 ,  0.134516 , 
 0.135512 ,  0.136348 ,  0.137953 ,  0.138939 ,  0.138978 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
