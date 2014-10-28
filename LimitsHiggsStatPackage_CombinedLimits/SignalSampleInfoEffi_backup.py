# === This file was created by the script parseEfficiencyFiles.pl ===
#
s = SignalSampleInfo(1000, 350, 35, 1)
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
 0.188844 ,  0.139932 ,  0.117659 ,  0.111447 ,  0.108677 ,  0.107134 ,  0.104394 ,  0.103315 , 
 0.103053 ,  0.102987 ,  0.103020 ,  0.105297 ,  0.104773 ,  0.104765 ,  0.104869 ,  0.105018 , 
 0.124536 ,  0.126016 ,  0.126630 ,  0.127099 ,  0.127533 ,  0.129614 ,  0.132740 ,  0.134516 , 
 0.135512 ,  0.136348 ,  0.137953 ,  0.138939 ,  0.138978 ,  0.138872 ,  0.140006 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(1000, 150, 10, 1)
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
 0.245030 ,  0.162592 ,  0.127315 ,  0.116987 ,  0.112280 ,  0.109673 ,  0.105184 ,  0.103516 , 
 0.103122 ,  0.103003 ,  0.102998 ,  0.104592 ,  0.103957 ,  0.103886 ,  0.103935 ,  0.104044 , 
 0.113713 ,  0.114889 ,  0.115506 ,  0.115865 ,  0.116116 ,  0.117089 ,  0.118726 ,  0.119831 , 
 0.120532 ,  0.121061 ,  0.122168 ,  0.122849 ,  0.122966 ,  0.123487 ,  0.123657 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(1000, 50, 4, 1)
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
 0.374955 ,  0.219818 ,  0.148936 ,  0.129348 ,  0.120768 ,  0.116130 ,  0.108237 ,  0.105234 , 
 0.104551 ,  0.104319 ,  0.104243 ,  0.106343 ,  0.105032 ,  0.104781 ,  0.104768 ,  0.104846 , 
 0.116247 ,  0.117090 ,  0.117669 ,  0.118115 ,  0.118479 ,  0.119968 ,  0.121922 ,  0.123001 , 
 0.123703 ,  0.124189 ,  0.125267 ,  0.126034 ,  0.125969 ,  0.125907 ,  0.126397 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(1000, 20, 1.5, 1)
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
 1.005189 ,  0.791473 ,  0.590146 ,  0.452845 ,  0.371934 ,  0.324236 ,  0.231220 ,  0.173902 , 
 0.155925 ,  0.150092 ,  0.149034 ,  0.175592 ,  0.152626 ,  0.145073 ,  0.142644 ,  0.142275 , 
 0.236922 ,  0.224972 ,  0.222937 ,  0.222612 ,  0.222727 ,  0.223833 ,  0.225110 ,  0.226573 , 
 0.227628 ,  0.227463 ,  0.227472 ,  0.226607 ,  0.233459 ,  0.236154 ,  0.239834 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(400, 150, 40, 1)
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
 0.204883 ,  0.146829 ,  0.120450 ,  0.113140 ,  0.109937 ,  0.108184 ,  0.105091 ,  0.103803 , 
 0.103489 ,  0.103416 ,  0.103457 ,  0.106527 ,  0.105877 ,  0.105895 ,  0.106027 ,  0.106186 , 
 0.133151 ,  0.134291 ,  0.134807 ,  0.135083 ,  0.135244 ,  0.135837 ,  0.137277 ,  0.138234 , 
 0.138936 ,  0.139435 ,  0.140317 ,  0.141819 ,  0.141869 ,  0.140579 ,  0.142032 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000725 ,  0.000397 ,  0.000276 ,  0.000213 ,  0.000173 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(400, 50, 8, 1)
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
 0.267840 ,  0.179326 ,  0.134013 ,  0.121008 ,  0.115298 ,  0.112184 ,  0.106866 ,  0.104887 , 
 0.104355 ,  0.104108 ,  0.103989 ,  0.105977 ,  0.104679 ,  0.104434 ,  0.104433 ,  0.104529 , 
 0.117341 ,  0.118185 ,  0.118728 ,  0.119072 ,  0.119346 ,  0.120383 ,  0.121964 ,  0.122951 , 
 0.123496 ,  0.123891 ,  0.124854 ,  0.125260 ,  0.125270 ,  0.125242 ,  0.125459 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(400, 20, 4, 1)
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
 0.359810 ,  0.234325 ,  0.160506 ,  0.136706 ,  0.126265 ,  0.120651 ,  0.111127 ,  0.107161 , 
 0.106089 ,  0.105722 ,  0.105636 ,  0.110022 ,  0.107168 ,  0.106511 ,  0.106379 ,  0.106446 , 
 0.127697 ,  0.128168 ,  0.128674 ,  0.129038 ,  0.129333 ,  0.130322 ,  0.131910 ,  0.132855 , 
 0.133539 ,  0.133997 ,  0.134678 ,  0.135497 ,  0.134867 ,  0.135492 ,  0.136925 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(200, 50, 20, 1)
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
 0.230852 ,  0.179711 ,  0.145339 ,  0.132144 ,  0.125078 ,  0.120653 ,  0.111853 ,  0.108205 , 
 0.107325 ,  0.107115 ,  0.107229 ,  0.115238 ,  0.112758 ,  0.112428 ,  0.112465 ,  0.112602 , 
 0.157793 ,  0.158807 ,  0.159365 ,  0.159726 ,  0.159997 ,  0.160843 ,  0.162064 ,  0.162630 , 
 0.163036 ,  0.163705 ,  0.164823 ,  0.165199 ,  0.165223 ,  0.164811 ,  0.165666 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(200, 20, 7, 1)
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
 0.354919 ,  0.225005 ,  0.160943 ,  0.140393 ,  0.130354 ,  0.124481 ,  0.113218 ,  0.108146 , 
 0.106846 ,  0.106434 ,  0.106415 ,  0.114431 ,  0.111099 ,  0.110395 ,  0.110313 ,  0.110437 , 
 0.137617 ,  0.137913 ,  0.138379 ,  0.138688 ,  0.138909 ,  0.139881 ,  0.141417 ,  0.142238 , 
 0.142813 ,  0.143518 ,  0.144169 ,  0.144374 ,  0.145411 ,  0.144396 ,  0.144302 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(125, 50, 50, 1)
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
 0.124204 ,  0.114277 ,  0.109192 ,  0.107296 ,  0.106288 ,  0.105658 ,  0.104380 ,  0.103840 , 
 0.103760 ,  0.103795 ,  0.103882 ,  0.104203 ,  0.104060 ,  0.104084 ,  0.104104 ,  0.104124 , 
 0.119700 ,  0.119759 ,  0.119870 ,  0.119704 ,  0.119674 ,  0.119407 ,  0.120075 ,  0.119107 , 
 0.118573 ,  0.120400 ,  0.117570 ,  0.126374 ,  0.118626 ,  0.130026 ,  0.143351 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
#
s = SignalSampleInfo(125, 20, 13, 1)
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
 0.134001 ,  0.115757 ,  0.108252 ,  0.106150 ,  0.105193 ,  0.104649 ,  0.103622 ,  0.103155 , 
 0.103042 ,  0.103017 ,  0.103027 ,  0.104679 ,  0.104250 ,  0.104126 ,  0.104069 ,  0.104041 , 
 0.108892 ,  0.108848 ,  0.108848 ,  0.108874 ,  0.108905 ,  0.108789 ,  0.108878 ,  0.109192 , 
 0.109254 ,  0.109178 ,  0.109304 ,  0.109384 ,  0.109282 ,  0.105409 ,  0.107074 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)