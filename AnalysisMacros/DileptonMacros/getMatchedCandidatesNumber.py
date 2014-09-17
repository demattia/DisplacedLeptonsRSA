print "get"

matched = 0
complementary = 0

foundComplementary = False
inputFile = open("log_noD0Sig.txt")
for line in inputFile:
    if line.find("processing") != -1:
        print line.split("/")[-1].split()[0]
    if line.find("matched") != -1:
        # print line.strip("\n")
        matched = float(line.strip("\n").split("=")[1].strip())
    elif line.find("complementary") != -1:
        # print line.strip("\n")
        complementary = float(line.strip("\n").split("=")[1].strip())
        foundComplementary = True

    if foundComplementary:
        print "match efficiency =", matched/(matched+complementary)
        foundComplementary = False
