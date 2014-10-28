# === This file was created by the script parseEfficiencyFiles.pl ===
#
s = SignalSampleInfoTk(1000, 350, 35, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.077920 ,  0.149600 ,  0.238000 ,  0.289200 ,  0.321300 ,  0.342700 ,  0.386600 ,  0.392400 , 
 0.378300 ,  0.361700 ,  0.345600 ,  0.271000 ,  0.206900 ,  0.166700 ,  0.139200 ,  0.119400 , 
 0.072210 ,  0.039290 ,  0.027060 ,  0.020690 ,  0.016770 ,  0.008698 ,  0.004481 ,  0.003027 , 
 0.002286 ,  0.001837 ,  0.000927 ,  0.000466 ,  0.000311 ,  0.000234 ,  0.000187 ] )
s.setEffiRelErrs (       "Electrons", [
 0.212224 ,  0.152354 ,  0.121460 ,  0.113000 ,  0.109405 ,  0.107472 ,  0.104124 ,  0.102804 , 
 0.102486 ,  0.102405 ,  0.102437 ,  0.106827 ,  0.106194 ,  0.106279 ,  0.106478 ,  0.106696 , 
 0.135850 ,  0.137211 ,  0.137790 ,  0.138088 ,  0.138298 ,  0.138986 ,  0.140335 ,  0.141254 , 
 0.141808 ,  0.142133 ,  0.143033 ,  0.144188 ,  0.143409 ,  0.142524 ,  0.144723 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000026 ,  0.000267 ,  0.000573 ,  0.000875 ,  0.001161 ,  0.002207 ,  0.002942 , 
 0.003130 ,  0.003175 ,  0.003149 ,  0.000762 ,  0.000989 ,  0.001054 ,  0.001037 ,  0.000988 , 
 0.002260 ,  0.001227 ,  0.000845 ,  0.000646 ,  0.000524 ,  0.000272 ,  0.000140 ,  0.000095 , 
 0.000071 ,  0.000057 ,  0.000029 ,  0.000015 ,  0.000010 ,  0.000007 ,  0.000006 ] )
s.setEffis (             "Muons", [
 0.090360 ,  0.198400 ,  0.315800 ,  0.372000 ,  0.404000 ,  0.424800 ,  0.470600 ,  0.488400 , 
 0.484000 ,  0.474100 ,  0.462400 ,  0.404500 ,  0.325000 ,  0.267600 ,  0.226200 ,  0.195400 , 
 0.127600 ,  0.070540 ,  0.048810 ,  0.037370 ,  0.030290 ,  0.015718 ,  0.008059 ,  0.005425 , 
 0.004090 ,  0.003282 ,  0.001652 ,  0.000829 ,  0.000553 ,  0.000415 ,  0.000332 ] )
s.setEffiRelErrs (       "Muons", [
 0.178379 ,  0.125451 ,  0.100003 ,  0.092614 ,  0.089262 ,  0.087377 ,  0.083994 ,  0.082650 , 
 0.082322 ,  0.082239 ,  0.082280 ,  0.085115 ,  0.084466 ,  0.084455 ,  0.084584 ,  0.084769 , 
 0.108010 ,  0.109713 ,  0.110418 ,  0.110956 ,  0.111453 ,  0.113828 ,  0.117376 ,  0.119380 , 
 0.120501 ,  0.121441 ,  0.123240 ,  0.124342 ,  0.124386 ,  0.124268 ,  0.125533 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(1000, 150, 10, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.010480 ,  0.046050 ,  0.115000 ,  0.164500 ,  0.200300 ,  0.227400 ,  0.301000 ,  0.348400 , 
 0.360300 ,  0.361100 ,  0.357700 ,  0.332100 ,  0.290400 ,  0.258800 ,  0.232500 ,  0.210500 , 
 0.128800 ,  0.074390 ,  0.052450 ,  0.040550 ,  0.033060 ,  0.017137 ,  0.008662 ,  0.005783 , 
 0.004338 ,  0.003471 ,  0.001735 ,  0.000867 ,  0.000578 ,  0.000433 ,  0.000347 ] )
s.setEffiRelErrs (       "Electrons", [
 0.295497 ,  0.184850 ,  0.134917 ,  0.120703 ,  0.114405 ,  0.110987 ,  0.105310 ,  0.103193 , 
 0.102626 ,  0.102420 ,  0.102373 ,  0.105622 ,  0.104615 ,  0.104407 ,  0.104399 ,  0.104461 , 
 0.119831 ,  0.120911 ,  0.121569 ,  0.122033 ,  0.122368 ,  0.123765 ,  0.126121 ,  0.127546 , 
 0.128393 ,  0.129085 ,  0.130349 ,  0.131160 ,  0.131609 ,  0.131253 ,  0.131128 ] )
s.setEffisInControl (    "Electrons", [
 0.000011 ,  0.000227 ,  0.000702 ,  0.000856 ,  0.000878 ,  0.000868 ,  0.000894 ,  0.001082 , 
 0.001146 ,  0.001130 ,  0.001081 ,  0.000001 ,  0.000030 ,  0.000079 ,  0.000117 ,  0.000142 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.011140 ,  0.057540 ,  0.149800 ,  0.214000 ,  0.259000 ,  0.291900 ,  0.377400 ,  0.434700 , 
 0.454800 ,  0.461700 ,  0.461700 ,  0.475900 ,  0.426200 ,  0.378800 ,  0.338100 ,  0.304000 , 
 0.189500 ,  0.111700 ,  0.078740 ,  0.060850 ,  0.049730 ,  0.026414 ,  0.013895 ,  0.009457 , 
 0.007171 ,  0.005776 ,  0.002928 ,  0.001475 ,  0.000985 ,  0.000740 ,  0.000592 ] )
s.setEffiRelErrs (       "Muons", [
 0.237058 ,  0.150310 ,  0.111203 ,  0.099212 ,  0.093615 ,  0.090471 ,  0.084974 ,  0.082901 , 
 0.082409 ,  0.082260 ,  0.082253 ,  0.084240 ,  0.083451 ,  0.083363 ,  0.083423 ,  0.083559 , 
 0.095329 ,  0.096729 ,  0.097461 ,  0.097886 ,  0.098183 ,  0.099332 ,  0.101256 ,  0.102550 , 
 0.103368 ,  0.103985 ,  0.105271 ,  0.106060 ,  0.106196 ,  0.106799 ,  0.106996 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(1000, 50, 4, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.000327 ,  0.006114 ,  0.031820 ,  0.059670 ,  0.084260 ,  0.105300 ,  0.175100 ,  0.237200 , 
 0.263000 ,  0.274700 ,  0.279900 ,  0.288000 ,  0.265900 ,  0.240000 ,  0.216500 ,  0.196100 , 
 0.135600 ,  0.080180 ,  0.056700 ,  0.043850 ,  0.035770 ,  0.018716 ,  0.009630 ,  0.006489 , 
 0.004894 ,  0.003929 ,  0.001978 ,  0.000992 ,  0.000662 ,  0.000497 ,  0.000398 ] )
s.setEffiRelErrs (       "Electrons", [
 0.316018 ,  0.218097 ,  0.152303 ,  0.131476 ,  0.122009 ,  0.116766 ,  0.107615 ,  0.104155 , 
 0.103300 ,  0.102977 ,  0.102862 ,  0.106323 ,  0.104623 ,  0.104212 ,  0.104116 ,  0.104165 , 
 0.117409 ,  0.117866 ,  0.118289 ,  0.118599 ,  0.118827 ,  0.119785 ,  0.121437 ,  0.122502 , 
 0.123225 ,  0.123650 ,  0.124712 ,  0.125177 ,  0.125452 ,  0.125709 ,  0.126228 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000000 ,  0.000001 ,  0.000011 ,  0.000040 ,  0.000080 ,  0.000276 ,  0.000463 , 
 0.000525 ,  0.000533 ,  0.000518 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.000184 ,  0.004810 ,  0.030480 ,  0.061040 ,  0.089070 ,  0.113400 ,  0.193600 ,  0.264100 , 
 0.294400 ,  0.309700 ,  0.318300 ,  0.318100 ,  0.296700 ,  0.269400 ,  0.244000 ,  0.221800 , 
 0.159500 ,  0.094960 ,  0.067470 ,  0.052320 ,  0.042750 ,  0.022517 ,  0.011685 ,  0.007907 , 
 0.005977 ,  0.004805 ,  0.002427 ,  0.001220 ,  0.000815 ,  0.000611 ,  0.000489 ] )
s.setEffiRelErrs (       "Muons", [
 0.369795 ,  0.210895 ,  0.135421 ,  0.113525 ,  0.103643 ,  0.098200 ,  0.088725 ,  0.085037 , 
 0.084190 ,  0.083901 ,  0.083807 ,  0.086404 ,  0.084786 ,  0.084476 ,  0.084460 ,  0.084555 , 
 0.098338 ,  0.099333 ,  0.100014 ,  0.100540 ,  0.100967 ,  0.102710 ,  0.104985 ,  0.106236 , 
 0.107049 ,  0.107610 ,  0.108852 ,  0.109734 ,  0.109659 ,  0.109589 ,  0.110151 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(1000, 20, 1.5, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.000059 ,  0.000537 ,  0.002278 ,  0.005636 ,  0.010330 ,  0.015780 ,  0.044180 ,  0.084550 , 
 0.107800 ,  0.121900 ,  0.130600 ,  0.153300 ,  0.143600 ,  0.127800 ,  0.113600 ,  0.101800 , 
 0.059140 ,  0.034690 ,  0.024520 ,  0.018980 ,  0.015510 ,  0.008143 ,  0.004189 ,  0.002820 , 
 0.002125 ,  0.001705 ,  0.000858 ,  0.000430 ,  0.000287 ,  0.000215 ,  0.000172 ] )
s.setEffiRelErrs (       "Electrons", [
 1.012034 ,  0.896106 ,  0.459283 ,  0.251630 ,  0.183935 ,  0.156342 ,  0.120460 ,  0.109318 , 
 0.106761 ,  0.105862 ,  0.105588 ,  0.111052 ,  0.108114 ,  0.107521 ,  0.107458 ,  0.107602 , 
 0.137087 ,  0.136923 ,  0.137133 ,  0.137334 ,  0.137510 ,  0.138306 ,  0.139689 ,  0.140681 , 
 0.141340 ,  0.141547 ,  0.142336 ,  0.143809 ,  0.142915 ,  0.143822 ,  0.145505 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.000000 ,  0.000022 ,  0.000376 ,  0.001045 ,  0.001825 ,  0.002594 ,  0.005454 ,  0.008608 , 
 0.010460 ,  0.011560 ,  0.012190 ,  0.015720 ,  0.016560 ,  0.016190 ,  0.015500 ,  0.014750 , 
 0.010770 ,  0.007137 ,  0.005312 ,  0.004215 ,  0.003485 ,  0.001837 ,  0.000932 ,  0.000623 , 
 0.000467 ,  0.000374 ,  0.000187 ,  0.000094 ,  0.000062 ,  0.000047 ,  0.000037 ] )
s.setEffiRelErrs (       "Muons", [
 1.003275 ,  0.789042 ,  0.586881 ,  0.448582 ,  0.366731 ,  0.318254 ,  0.222755 ,  0.162477 , 
 0.143072 ,  0.136691 ,  0.135529 ,  0.164285 ,  0.139469 ,  0.131161 ,  0.128469 ,  0.128059 , 
 0.228668 ,  0.216262 ,  0.214144 ,  0.213806 ,  0.213926 ,  0.215077 ,  0.216406 ,  0.217928 , 
 0.219024 ,  0.218852 ,  0.218861 ,  0.217963 ,  0.225078 ,  0.227873 ,  0.231684 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(400, 150, 40, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.070310 ,  0.132800 ,  0.183100 ,  0.204600 ,  0.216900 ,  0.224800 ,  0.239800 ,  0.236500 , 
 0.224800 ,  0.212800 ,  0.201700 ,  0.153400 ,  0.113000 ,  0.090000 ,  0.074720 ,  0.063810 , 
 0.036630 ,  0.019930 ,  0.013660 ,  0.010380 ,  0.008374 ,  0.004287 ,  0.002192 ,  0.001477 , 
 0.001114 ,  0.000895 ,  0.000451 ,  0.000226 ,  0.000151 ,  0.000113 ,  0.000091 ] )
s.setEffiRelErrs (       "Electrons", [
 0.219638 ,  0.160392 ,  0.130894 ,  0.120836 ,  0.115882 ,  0.113002 ,  0.107599 ,  0.105192 , 
 0.104509 ,  0.104265 ,  0.104239 ,  0.113536 ,  0.111466 ,  0.111114 ,  0.111171 ,  0.111352 , 
 0.164278 ,  0.164437 ,  0.164688 ,  0.164937 ,  0.165068 ,  0.165698 ,  0.166469 ,  0.167325 , 
 0.167625 ,  0.167887 ,  0.168820 ,  0.170369 ,  0.166585 ,  0.166863 ,  0.166103 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000000 ,  0.000002 ,  0.000015 ,  0.000043 ,  0.000076 ,  0.000189 ,  0.000258 , 
 0.000304 ,  0.000335 ,  0.000349 ,  0.000427 ,  0.000426 ,  0.000369 ,  0.000316 ,  0.000275 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.084850 ,  0.180500 ,  0.285000 ,  0.334800 ,  0.362400 ,  0.379600 ,  0.410600 ,  0.412600 , 
 0.403200 ,  0.392500 ,  0.382000 ,  0.318800 ,  0.251800 ,  0.205600 ,  0.172900 ,  0.148800 , 
 0.076750 ,  0.042200 ,  0.029070 ,  0.022160 ,  0.017910 ,  0.009118 ,  0.004583 ,  0.003058 , 
 0.002294 ,  0.001835 ,  0.000917 ,  0.000459 ,  0.000306 ,  0.000229 ,  0.000183 ] )
s.setEffiRelErrs (       "Muons", [
 0.195279 ,  0.133101 ,  0.103272 ,  0.094645 ,  0.090792 ,  0.088661 ,  0.084859 ,  0.083259 , 
 0.082868 ,  0.082775 ,  0.082827 ,  0.086631 ,  0.085831 ,  0.085853 ,  0.086016 ,  0.086212 , 
 0.117840 ,  0.119126 ,  0.119708 ,  0.120019 ,  0.120199 ,  0.120867 ,  0.122483 ,  0.123554 , 
 0.124339 ,  0.124896 ,  0.125880 ,  0.127553 ,  0.127609 ,  0.126172 ,  0.127789 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000725 ,  0.000397 ,  0.000276 ,  0.000213 ,  0.000173 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(400, 50, 8, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.004150 ,  0.024780 ,  0.066050 ,  0.093590 ,  0.112700 ,  0.126900 ,  0.165300 ,  0.191500 , 
 0.199800 ,  0.202100 ,  0.201500 ,  0.203600 ,  0.180900 ,  0.162100 ,  0.145900 ,  0.132100 , 
 0.084140 ,  0.049350 ,  0.034740 ,  0.026750 ,  0.021720 ,  0.011112 ,  0.005564 ,  0.003700 , 
 0.002770 ,  0.002213 ,  0.001103 ,  0.000551 ,  0.000367 ,  0.000275 ,  0.000220 ] )
s.setEffiRelErrs (       "Electrons", [
 0.287104 ,  0.190796 ,  0.145426 ,  0.130299 ,  0.122535 ,  0.117883 ,  0.109116 ,  0.105432 , 
 0.104477 ,  0.104166 ,  0.104150 ,  0.109601 ,  0.107337 ,  0.106620 ,  0.106350 ,  0.106277 , 
 0.130816 ,  0.130478 ,  0.130673 ,  0.130860 ,  0.131038 ,  0.131932 ,  0.133641 ,  0.134825 , 
 0.135509 ,  0.135825 ,  0.137205 ,  0.137200 ,  0.138481 ,  0.137368 ,  0.137427 ] )
s.setEffisInControl (    "Electrons", [
 0.000001 ,  0.000073 ,  0.000381 ,  0.000553 ,  0.000613 ,  0.000620 ,  0.000495 ,  0.000316 , 
 0.000259 ,  0.000262 ,  0.000286 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.004709 ,  0.031040 ,  0.093390 ,  0.141000 ,  0.175400 ,  0.201000 ,  0.268700 ,  0.313500 , 
 0.328400 ,  0.334200 ,  0.336300 ,  0.323900 ,  0.298200 ,  0.270800 ,  0.245200 ,  0.222600 , 
 0.141800 ,  0.082090 ,  0.057490 ,  0.044260 ,  0.036030 ,  0.018783 ,  0.009679 ,  0.006531 , 
 0.004930 ,  0.003960 ,  0.001997 ,  0.001003 ,  0.000669 ,  0.000502 ,  0.000402 ] )
s.setEffiRelErrs (       "Muons", [
 0.260568 ,  0.168270 ,  0.118813 ,  0.103923 ,  0.097214 ,  0.093500 ,  0.087048 ,  0.084606 , 
 0.083946 ,  0.083639 ,  0.083491 ,  0.085954 ,  0.084348 ,  0.084045 ,  0.084043 ,  0.084162 , 
 0.099628 ,  0.100622 ,  0.101259 ,  0.101662 ,  0.101982 ,  0.103194 ,  0.105034 ,  0.106179 , 
 0.106809 ,  0.107266 ,  0.108377 ,  0.108845 ,  0.108856 ,  0.108824 ,  0.109073 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(400, 20, 4, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.000046 ,  0.001916 ,  0.014430 ,  0.029390 ,  0.042590 ,  0.053680 ,  0.088380 ,  0.116900 , 
 0.129200 ,  0.136200 ,  0.140800 ,  0.152700 ,  0.144900 ,  0.131800 ,  0.119100 ,  0.107800 , 
 0.064390 ,  0.038610 ,  0.027380 ,  0.021160 ,  0.017220 ,  0.008845 ,  0.004480 ,  0.003002 , 
 0.002257 ,  0.001809 ,  0.000908 ,  0.000455 ,  0.000303 ,  0.000228 ,  0.000182 ] )
s.setEffiRelErrs (       "Electrons", [
 0.383578 ,  0.243734 ,  0.170663 ,  0.147361 ,  0.135583 ,  0.128494 ,  0.114702 ,  0.108574 , 
 0.106791 ,  0.106013 ,  0.105717 ,  0.111177 ,  0.108039 ,  0.107381 ,  0.107315 ,  0.107460 , 
 0.135700 ,  0.135708 ,  0.136090 ,  0.136356 ,  0.136607 ,  0.137419 ,  0.138893 ,  0.139721 , 
 0.140243 ,  0.140434 ,  0.141726 ,  0.141572 ,  0.141616 ,  0.143052 ,  0.141576 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.000227 ,  0.004604 ,  0.025440 ,  0.049190 ,  0.070250 ,  0.087820 ,  0.139600 ,  0.177900 , 
 0.193400 ,  0.200800 ,  0.204100 ,  0.186400 ,  0.176400 ,  0.161700 ,  0.147400 ,  0.134600 , 
 0.086900 ,  0.051600 ,  0.036740 ,  0.028530 ,  0.023310 ,  0.012192 ,  0.006249 ,  0.004204 , 
 0.003167 ,  0.002541 ,  0.001278 ,  0.000641 ,  0.000428 ,  0.000321 ,  0.000257 ] )
s.setEffiRelErrs (       "Muons", [
 0.354429 ,  0.225976 ,  0.148051 ,  0.121842 ,  0.110000 ,  0.103507 ,  0.092229 ,  0.087409 , 
 0.086092 ,  0.085639 ,  0.085533 ,  0.090895 ,  0.087419 ,  0.086611 ,  0.086450 ,  0.086532 , 
 0.111640 ,  0.112179 ,  0.112757 ,  0.113171 ,  0.113508 ,  0.114634 ,  0.116436 ,  0.117505 , 
 0.118278 ,  0.118795 ,  0.119563 ,  0.120485 ,  0.119775 ,  0.120478 ,  0.122087 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(200, 50, 20, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.009980 ,  0.025430 ,  0.044050 ,  0.054630 ,  0.061380 ,  0.065970 ,  0.075370 ,  0.076200 , 
 0.072880 ,  0.069130 ,  0.065650 ,  0.059330 ,  0.044940 ,  0.036270 ,  0.030380 ,  0.026090 , 
 0.018590 ,  0.010380 ,  0.007210 ,  0.005527 ,  0.004480 ,  0.002281 ,  0.001135 ,  0.000752 , 
 0.000562 ,  0.000449 ,  0.000223 ,  0.000111 ,  0.000074 ,  0.000056 ,  0.000044 ] )
s.setEffiRelErrs (       "Electrons", [
 0.379480 ,  0.251078 ,  0.182252 ,  0.158796 ,  0.147250 ,  0.140242 ,  0.125306 ,  0.116926 , 
 0.114416 ,  0.113576 ,  0.113437 ,  0.133939 ,  0.127879 ,  0.126453 ,  0.126086 ,  0.126084 , 
 0.207503 ,  0.208112 ,  0.208547 ,  0.208835 ,  0.209068 ,  0.209823 ,  0.210957 ,  0.211929 , 
 0.212513 ,  0.212705 ,  0.213799 ,  0.214548 ,  0.214528 ,  0.205548 ,  0.208283 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.043090 ,  0.079190 ,  0.109000 ,  0.122300 ,  0.130000 ,  0.135300 ,  0.147900 ,  0.153800 , 
 0.153500 ,  0.151300 ,  0.148000 ,  0.141400 ,  0.114600 ,  0.095490 ,  0.081500 ,  0.070880 , 
 0.040460 ,  0.022140 ,  0.015270 ,  0.011650 ,  0.009403 ,  0.004736 ,  0.002350 ,  0.001559 , 
 0.001166 ,  0.000931 ,  0.000464 ,  0.000231 ,  0.000154 ,  0.000116 ,  0.000092 ] )
s.setEffiRelErrs (       "Muons", [
 0.222372 ,  0.168680 ,  0.131455 ,  0.116701 ,  0.108635 ,  0.103509 ,  0.093103 ,  0.088687 , 
 0.087611 ,  0.087353 ,  0.087493 ,  0.097143 ,  0.094188 ,  0.093792 ,  0.093837 ,  0.094001 , 
 0.145105 ,  0.146207 ,  0.146813 ,  0.147206 ,  0.147499 ,  0.148416 ,  0.149738 ,  0.150351 , 
 0.150791 ,  0.151514 ,  0.152721 ,  0.153126 ,  0.153152 ,  0.152708 ,  0.153631 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(200, 20, 7, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.001025 ,  0.007227 ,  0.021000 ,  0.030470 ,  0.036920 ,  0.041620 ,  0.054750 ,  0.066240 , 
 0.070790 ,  0.072580 ,  0.073230 ,  0.063110 ,  0.056600 ,  0.050350 ,  0.044970 ,  0.040470 , 
 0.030070 ,  0.018200 ,  0.013020 ,  0.010140 ,  0.008308 ,  0.004365 ,  0.002239 ,  0.001505 , 
 0.001133 ,  0.000909 ,  0.000456 ,  0.000229 ,  0.000153 ,  0.000114 ,  0.000092 ] )
s.setEffiRelErrs (       "Electrons", [
 0.443655 ,  0.295549 ,  0.208465 ,  0.177869 ,  0.161617 ,  0.151237 ,  0.128202 ,  0.116340 , 
 0.113248 ,  0.112173 ,  0.111919 ,  0.130586 ,  0.121250 ,  0.118337 ,  0.117386 ,  0.117164 , 
 0.165029 ,  0.164111 ,  0.164231 ,  0.164306 ,  0.164537 ,  0.165101 ,  0.166393 ,  0.166940 , 
 0.167956 ,  0.168002 ,  0.169438 ,  0.168936 ,  0.170437 ,  0.173036 ,  0.165018 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000000 ,  0.000005 ,  0.000032 ,  0.000074 ,  0.000117 ,  0.000225 ,  0.000219 , 
 0.000182 ,  0.000153 ,  0.000131 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.003669 ,  0.018590 ,  0.047420 ,  0.067530 ,  0.081720 ,  0.092190 ,  0.119900 ,  0.139000 , 
 0.145400 ,  0.148100 ,  0.149300 ,  0.141800 ,  0.130200 ,  0.117200 ,  0.105200 ,  0.094830 , 
 0.059920 ,  0.035330 ,  0.024930 ,  0.019210 ,  0.015590 ,  0.007940 ,  0.003962 ,  0.002634 , 
 0.001972 ,  0.001576 ,  0.000786 ,  0.000392 ,  0.000261 ,  0.000196 ,  0.000157 ] )
s.setEffiRelErrs (       "Muons", [
 0.349464 ,  0.216297 ,  0.148525 ,  0.125965 ,  0.114670 ,  0.107946 ,  0.094738 ,  0.088614 , 
 0.087023 ,  0.086517 ,  0.086493 ,  0.096184 ,  0.092195 ,  0.091346 ,  0.091247 ,  0.091397 , 
 0.122863 ,  0.123195 ,  0.123717 ,  0.124062 ,  0.124309 ,  0.125394 ,  0.127106 ,  0.128018 , 
 0.128657 ,  0.129438 ,  0.130160 ,  0.130387 ,  0.131534 ,  0.130412 ,  0.130308 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(125, 50, 50, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.004487 ,  0.006471 ,  0.007776 ,  0.008282 ,  0.008544 ,  0.008684 ,  0.008659 ,  0.007933 , 
 0.007284 ,  0.006758 ,  0.006321 ,  0.006084 ,  0.004010 ,  0.002982 ,  0.002371 ,  0.001967 , 
 0.001044 ,  0.000539 ,  0.000363 ,  0.000274 ,  0.000220 ,  0.000111 ,  0.000056 ,  0.000037 , 
 0.000028 ,  0.000022 ,  0.000011 ,  0.000006 ,  0.000004 ,  0.000003 ,  0.000002 ] )
s.setEffiRelErrs (       "Electrons", [
 0.180127 ,  0.145161 ,  0.124971 ,  0.117654 ,  0.113941 ,  0.111724 ,  0.107648 ,  0.105778 , 
 0.105069 ,  0.104777 ,  0.104641 ,  0.114268 ,  0.113445 ,  0.113300 ,  0.113392 ,  0.113388 , 
 0.169950 ,  0.169577 ,  0.170678 ,  0.170774 ,  0.168193 ,  0.170715 ,  0.163327 ,  0.171253 , 
 0.177548 ,  0.172332 ,  0.210248 ,  0.227593 ,  0.271295 ,  0.103298 ,  0.125801 ] )
s.setEffisInControl (    "Electrons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.017310 ,  0.026270 ,  0.032560 ,  0.035010 ,  0.036290 ,  0.037050 ,  0.038050 ,  0.036940 , 
 0.035410 ,  0.033960 ,  0.032590 ,  0.028610 ,  0.020210 ,  0.015450 ,  0.012470 ,  0.010440 , 
 0.005299 ,  0.002796 ,  0.001898 ,  0.001436 ,  0.001155 ,  0.000584 ,  0.000293 ,  0.000196 , 
 0.000147 ,  0.000118 ,  0.000059 ,  0.000029 ,  0.000020 ,  0.000015 ,  0.000012 ] )
s.setEffiRelErrs (       "Muons", [
 0.107628 ,  0.096002 ,  0.089889 ,  0.087575 ,  0.086337 ,  0.085561 ,  0.083977 ,  0.083306 , 
 0.083205 ,  0.083249 ,  0.083357 ,  0.083757 ,  0.083579 ,  0.083609 ,  0.083634 ,  0.083659 , 
 0.102397 ,  0.102466 ,  0.102595 ,  0.102401 ,  0.102366 ,  0.102054 ,  0.102835 ,  0.101703 , 
 0.101076 ,  0.103215 ,  0.099898 ,  0.110124 ,  0.101140 ,  0.114297 ,  0.129254 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfoTk(125, 20, 13, 1)
s.setCtauScales ( [
  0.001   ,   0.002   ,   0.004   ,   0.006   ,   0.008   ,   0.010   ,   0.020   ,   0.040   , 
  0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   ,   0.600   ,   0.800   ,   1.000   , 
  2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   ,  20.000   ,  40.000   ,  60.000   , 
 80.000   , 100.000   , 200.000   , 400.000   , 600.000   , 800.000   , 1000.000   ] )
s.setWidths (      "Electrons", [] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Electrons", [
 0.001091 ,  0.003627 ,  0.007020 ,  0.008816 ,  0.009919 ,  0.010680 ,  0.012580 ,  0.013680 , 
 0.013810 ,  0.013650 ,  0.013410 ,  0.012390 ,  0.009994 ,  0.008278 ,  0.007026 ,  0.006088 , 
 0.003556 ,  0.001955 ,  0.001346 ,  0.001026 ,  0.000829 ,  0.000423 ,  0.000214 ,  0.000143 , 
 0.000108 ,  0.000086 ,  0.000043 ,  0.000022 ,  0.000014 ,  0.000011 ,  0.000009 ] )
s.setEffiRelErrs (       "Electrons", [
 0.182755 ,  0.139130 ,  0.119532 ,  0.113511 ,  0.110447 ,  0.108559 ,  0.104880 ,  0.103452 , 
 0.103240 ,  0.103293 ,  0.103447 ,  0.106268 ,  0.105018 ,  0.104735 ,  0.104649 ,  0.104659 , 
 0.123087 ,  0.122977 ,  0.122849 ,  0.123048 ,  0.122905 ,  0.123486 ,  0.123009 ,  0.122951 , 
 0.125331 ,  0.122754 ,  0.122765 ,  0.136553 ,  0.125237 ,  0.136492 ,  0.152756 ] )
s.setEffisInControl (    "Electrons", [
 0.000003 ,  0.000018 ,  0.000031 ,  0.000030 ,  0.000028 ,  0.000025 ,  0.000016 ,  0.000009 , 
 0.000006 ,  0.000005 ,  0.000004 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
s.setEffis (             "Muons", [
 0.003964 ,  0.011810 ,  0.021810 ,  0.027430 ,  0.031020 ,  0.033520 ,  0.039490 ,  0.042930 , 
 0.043740 ,  0.043760 ,  0.043460 ,  0.041160 ,  0.034240 ,  0.028810 ,  0.024690 ,  0.021520 , 
 0.012800 ,  0.007124 ,  0.004929 ,  0.003768 ,  0.003050 ,  0.001563 ,  0.000792 ,  0.000531 , 
 0.000399 ,  0.000320 ,  0.000160 ,  0.000080 ,  0.000054 ,  0.000040 ,  0.000032 ] )
s.setEffiRelErrs (       "Muons", [
 0.118799 ,  0.097758 ,  0.088744 ,  0.086167 ,  0.084986 ,  0.084311 ,  0.083034 ,  0.082450 , 
 0.082308 ,  0.082278 ,  0.082289 ,  0.084349 ,  0.083816 ,  0.083662 ,  0.083590 ,  0.083555 , 
 0.089523 ,  0.089471 ,  0.089470 ,  0.089501 ,  0.089540 ,  0.089398 ,  0.089506 ,  0.089888 , 
 0.089964 ,  0.089871 ,  0.090025 ,  0.090122 ,  0.089997 ,  0.085252 ,  0.087304 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)