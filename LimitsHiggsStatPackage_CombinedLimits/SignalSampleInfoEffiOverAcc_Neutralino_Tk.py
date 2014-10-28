# === This file was created by the script parseEfficiencyFiles.pl ===
#
s = SignalSampleInfoTk(1500, 494, 16, 2)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.463900 ,  0.513100 ,  0.533900 ,  0.532400 ,  0.531600 ,  0.531200 ,  0.517500 ,  0.469400 , 
 0.429800 ,  0.400600 ,  0.378700 ,  0.321800 ,  0.285100 ,  0.271200 ,  0.263800 ,  0.259200 , 
 0.249700 ,  0.244800 ,  0.243100 ,  0.242200 ,  0.241700 ] )
s.setEffiRelErrs (       "Muons", [
 0.181744 ,  0.138735 ,  0.124365 ,  0.119242 ,  0.115071 ,  0.111759 ,  0.103851 ,  0.100685 , 
 0.100203 ,  0.100244 ,  0.100469 ,  0.102098 ,  0.104683 ,  0.106357 ,  0.107525 ,  0.108382 , 
 0.110579 ,  0.112011 ,  0.112562 ,  0.112861 ,  0.113038 ] )
s.setEffisInControl (    "Muons", [
 0.000197 ,  0.001801 ,  0.004985 ,  0.007090 ,  0.008795 ,  0.010200 ,  0.013610 ,  0.014470 , 
 0.014310 ,  0.013990 ,  0.013660 ,  0.012730 ,  0.012350 ,  0.012330 ,  0.012360 ,  0.012390 , 
 0.012500 ,  0.012580 ,  0.012610 ,  0.012620 ,  0.012640 ] )
samples.append(s)
#
s = SignalSampleInfoTk(1000, 148, 6, 2)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.255800 ,  0.407900 ,  0.488800 ,  0.506100 ,  0.514000 ,  0.518300 ,  0.517500 ,  0.488500 , 
 0.461600 ,  0.441600 ,  0.427200 ,  0.393900 ,  0.375000 ,  0.366900 ,  0.361900 ,  0.358400 , 
 0.349900 ,  0.344600 ,  0.342600 ,  0.341500 ,  0.340900 ] )
s.setEffiRelErrs (       "Muons", [
 0.290667 ,  0.213575 ,  0.167646 ,  0.141049 ,  0.126222 ,  0.117885 ,  0.104769 ,  0.100599 , 
 0.099837 ,  0.099712 ,  0.099815 ,  0.101326 ,  0.104263 ,  0.105659 ,  0.106332 ,  0.106716 , 
 0.107569 ,  0.108248 ,  0.108571 ,  0.108758 ,  0.108882 ] )
s.setEffisInControl (    "Muons", [
 0.002863 ,  0.007380 ,  0.007888 ,  0.006786 ,  0.005832 ,  0.005154 ,  0.003695 ,  0.002872 , 
 0.002647 ,  0.002532 ,  0.002431 ,  0.001952 ,  0.001393 ,  0.001118 ,  0.000958 ,  0.000852 , 
 0.000617 ,  0.000485 ,  0.000438 ,  0.000415 ,  0.000400 ] )
samples.append(s)
#
s = SignalSampleInfoTk(350, 148, 17.3, 2)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.401800 ,  0.479900 ,  0.501800 ,  0.504500 ,  0.504200 ,  0.503200 ,  0.493100 ,  0.450100 , 
 0.408000 ,  0.375500 ,  0.351000 ,  0.290500 ,  0.260900 ,  0.253800 ,  0.251300 ,  0.250100 , 
 0.248900 ,  0.248900 ,  0.249000 ,  0.249100 ,  0.249100 ] )
s.setEffiRelErrs (       "Muons", [
 0.234919 ,  0.170087 ,  0.138922 ,  0.127694 ,  0.122135 ,  0.118657 ,  0.110100 ,  0.105900 , 
 0.105210 ,  0.105240 ,  0.105555 ,  0.110449 ,  0.135265 ,  0.159112 ,  0.176124 ,  0.188263 , 
 0.216967 ,  0.233608 ,  0.239492 ,  0.242470 ,  0.244333 ] )
s.setEffisInControl (    "Muons", [
 0.000002 ,  0.000334 ,  0.002966 ,  0.005249 ,  0.006602 ,  0.007405 ,  0.008762 ,  0.009515 , 
 0.009245 ,  0.008574 ,  0.007883 ,  0.005706 ,  0.004253 ,  0.003736 ,  0.003474 ,  0.003316 , 
 0.003000 ,  0.002842 ,  0.002790 ,  0.002763 ,  0.002748 ] )
samples.append(s)
#
s = SignalSampleInfoTk(120, 48, 16.5, 2)
s.setCtauScales ( [
  0.010   ,   0.020   ,   0.040   ,   0.060   ,   0.080   ,   0.100   ,   0.200   ,   0.400   , 
  0.600   ,   0.800   ,   1.000   ,   2.000   ,   4.000   ,   6.000   ,   8.000   ,  10.000   , 
 20.000   ,  40.000   ,  60.000   ,  80.000   , 100.000   ] )
s.setWidths (          "Muons", [] )
s.setEffis (             "Muons", [
 0.470500 ,  0.665300 ,  0.729800 ,  0.700400 ,  0.661600 ,  0.623900 ,  0.490900 ,  0.384500 , 
 0.342800 ,  0.320600 ,  0.306600 ,  0.275800 ,  0.258000 ,  0.251400 ,  0.248000 ,  0.245900 , 
 0.241700 ,  0.239500 ,  0.238700 ,  0.238300 ,  0.238100 ] )
s.setEffiRelErrs (       "Muons", [
 0.612635 ,  0.319414 ,  0.220557 ,  0.202014 ,  0.194064 ,  0.188866 ,  0.172598 ,  0.160353 , 
 0.158749 ,  0.160068 ,  0.162063 ,  0.169812 ,  0.175981 ,  0.178572 ,  0.179986 ,  0.180893 , 
 0.182790 ,  0.183845 ,  0.184244 ,  0.184444 ,  0.184542 ] )
s.setEffisInControl (    "Muons", [
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 , 
 0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ,  0.000000 ] )
samples.append(s)
