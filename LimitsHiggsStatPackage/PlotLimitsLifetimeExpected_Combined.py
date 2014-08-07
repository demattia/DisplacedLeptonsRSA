# ========================================================================================
# This plots limits for H-->XX or squark --> neutralino.
#
# Where the script refers to Higgs mass, it can mean also Squark mass.
# Where it refers to X boson mass/lifetime, it can mean Neutralino mass/lifetime.
#=======================================================================================

import ROOT as r
import sys, os
import pickle
# Contains exotic masses, luminosity etc.
from SignalSampleInfo_Combined import *

r.gROOT.LoadMacro("tdrstyle.C")
r.setTDRStyle()

# Configurable parameters
logx = 1
logy = 1
drawExpected = 1
smooth = 1  # Smooth top of 95% expected limit band, which is most prone to fluctuations

if len(sys.argv) < 5:
    sys.exit('Usage: python PlotLimitsLifetime.py LeptonType Xlimits HiggsMass getSigmaBRacc \n' +
             'where LeptonType = Muons or Electrons\n' +
             '      Xlimits = True (for H-->XX) or False (for squark --> neutralino)\n' +
             '      HiggsMass to plot = 100, 400, 200 or 125. Not used for squark -> neutralino limits.\n' +
             '      getSigmaBRacc = True (limits on sigma*BR*A) or False (on sigma*BR)')

LeptonType = sys.argv[1]
Xlimits = int(sys.argv[2])
hmass = int(sys.argv[3])
getSigmaBRacc = int(sys.argv[4])
FileDir = LeptonType + "_txt"

# Get exotic masses, luminosity etc.
samples = getSignalSampleInfoCombined()
jobOpt = JobOptions()
lumi = jobOpt.getLumi(LeptonType)

#
#------------------------------------------------------------------------------------------------------------
#=== Define CLASS LIMITS to contain limits at given lifetime scale factor (and Higgs and X boson masses).
class limits:
    def __init__(self):
        # c*tau
        self.lt = 0.
        # c*tau scale factor
        self.ctauScale = 0.
        # relative uncertainty on efficiency
        self.relerr = 0.
        # Limits valid for small branching ratio * efficiency.
        self.up_br0 = 0.
        self.est_br0 = 0.
        self.est1p_br0 = 0.
        self.est1m_br0 = 0.
        self.est2p_br0 = 0.
        self.est2m_br0 = 0.
        # Limits valid for 100% branching ratio.
        self.up_br1 = 0.
        self.est_br1 = 0.
        self.est1p_br1 = 0.
        self.est1m_br1 = 0.
        self.est2p_br1 = 0.
        self.est2m_br1 = 0.


#------------------------------------------------------------------------------------------------------------
#=== Define CLASS GRRAPHS to contain limit curves for specified Higgs and X boson masses.
class graphs:
    def __init__(self, hmass_, xmass_):
        # Contains masses
        self.hmass = hmass_
        self.xmass = xmass_
        # Will contain graphs
        self.g = 0  # observed limit, valid for small branching ratio * efficiency (TGraph)
        self.g_br1 = 0  # observed limit, valid for 100% branching ratio. (TGraph)
        self.gest1 = 0  # expected limit 1 sigma band, valid for small branching ratio * efficiency (TGraphErrors)
        self.gest2 = 0  # expected limit 2 sigma band, valid for small branching ratio * efficiency (TGraphErrors)

#------------------------------------------------------------------------------------------------------------

# Determine (Higgs, X boson) masses for which plots required.
plotsVec = []
for s in samples:
    # We can choose either 1 or 2 here, but must choose one to avoid getting duplicate masses in the list.
    if s.acceptance == 1:
        if hmass == s.MH or not Xlimits:
            plotsVec.append(graphs(s.MH, s.MX))

if Xlimits:
    # Set graph boundaries for long-lived X boson limits.
    ymin = 0
    if hmass == 1000:
        xmin = 0.002
        xmax = 60000
        ymax = 30.
        if logy == 1:
            if getSigmaBRacc:
                ymin = 5.0e-5
                ymax = 300.0
            else:
                ymin = 5.0e-5
                ymax = 400.0
    elif hmass == 400:
        xmin = 0.003
        xmax = 85000
        ymax = 30.
        if logy == 1:
            if getSigmaBRacc:
                ymin = 5.0e-5
                ymax = 10.0
            else:
                ymin = 1.0e-4
                ymax = 20.0
    elif hmass == 200:
        xmin = 0.001
        xmax = 100000
        ymax = 30.
        if logy == 1:
            if getSigmaBRacc:
                ymin = 9.0e-5
                ymax = 0.3
            else:
                # ymin = 3.0e-4
                ymin = 2.0e-4
                ymax = 20.0
    elif hmass == 125:
        xmin = 0.001
        xmax = 100000
        ymax = 30.
        if logy == 1:
            if getSigmaBRacc:
                ymin = 1.0e-4
                ymax = 0.03
            else:
                ymin = 7.0e-4
                ymax = 40.0
    else:
        print "Oops, requested Higgs mass = ", hmass, " not recognized.", Xlimits
        sys.exit(1)

else:
    # Set graph boundaries for long-lived neutralino limits.
    xmin = 3.0e-2
    xmax = 3.0e3
    ymin = 0.
    ymax = 30.
    if logy == 1:
        if getSigmaBRacc:
            ymin = 7.0e-5
            ymax = 0.02
        else:
            ymin = 1.0e-4
            ymax = 5.0

jcol = 1
jpoly = 20

#r.gROOT.SetStyle("Plain")
r.gStyle.SetErrorX(0)
# have to restore the title though
r.gStyle.SetOptTitle(1)
r.gStyle.SetTitleBorderSize(0)
#r.gStyle.SetTitleFont(42, "")

c = r.TCanvas("c", "c", 600, 600)
r.gPad.SetLeftMargin(0.15)
r.gPad.SetTopMargin(0.08)
r.gPad.SetRightMargin(0.04)
if logx == 1:
    r.gPad.SetLogx()
if logy == 1:
    r.gPad.SetLogy()
r.gStyle.SetTitleFont(42, "")
r.gStyle.SetTitleX(0.55)
r.gStyle.SetTitleY(0.99)
r.gStyle.SetTitleAlign(23)
r.gStyle.SetTitleSize(0.05, "XYZ")
r.gStyle.SetLabelSize(0.045, "XYZ")
fr = c.DrawFrame(xmin, ymin, xmax, ymax)
# Add text to plot with Higgs mass.
if Xlimits:
    if logy == 1:
        yMHtext = ymax / 3
    else:
        yMHtext = 0.9 * ymax
    t1 = r.TLatex(xmax * 0.5, yMHtext, "m_{H} = " + str(hmass) + " GeV/c^{2}")
    t1.SetTextAlign(32)
    t1.SetTextFont(62)
    t1.SetTextSize(0.04)
    t1.Draw()

fr.SetTitle("CMS    #sqrt{s} = 8 TeV    L = %4.1f fb^{-1}" % (lumi / 1000.))

if LeptonType == "Electrons":
    leptName = "e"
elif LeptonType == "Muons":
    leptName = "#mu"
else:
    print "Unrecognised lepton"
    sys.exit(1)
# N.B. #kern[-0.7]{ } creates a narrow space
if getSigmaBRacc:
    accName = ".A"
else:
    accName = ""
if Xlimits:
    fr.GetYaxis().SetTitle(
        "#sigma(H^{0}#rightarrow XX)#kern[-0.7]{ }B%s(X#rightarrow %s^{+}%s^{-}) [pb]" % (accName, leptName, leptName))
else:
    fr.GetYaxis().SetTitle(
        "#sigma(#tilde{q}#bar{#tilde{q}}+#tilde{q}#tilde{q})#kern[-0.7]{ }B%s(#tilde{q}#rightarrow #chi^{0} #rightarrow %s^{+}%s^{-}#nu) [pb]" % (
            accName, leptName, leptName))

fr.GetXaxis().SetTitle("c#tau [cm]")
fr.GetXaxis().SetTitleOffset(1.05)
fr.GetYaxis().SetTitleOffset(1.40)
if Xlimits:
    # x1, y1, x2, y2
    leg = r.TLegend(0.16, 0.58, 0.62, 0.83)
else:
    # Higher than for X boson, as text about M_H mass is not needed.
    # Wider as text is longer
    leg = r.TLegend(0.16, 0.62, 0.70, 0.90)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.SetTextFont(42)
dummy = r.TH1F("dummy", "dummy", 1, 1, 1)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetFillColor(0)
leg.AddEntry(dummy, "Observed limits")

xmax_seen = 0.
xmin_seen = 9.9e9
ymax_seen = 0.
ymin_seen = 9.9e9
# Loop over Higgs and X boson masses.
for index, plots in enumerate(plotsVec):
    flist = []
    # Find limits at all lifetimes for these masses.
    for filename in os.listdir(FileDir):
        if filename.find('.txt') > -1 and filename.find(str(plots.hmass) + "_" + str(plots.xmass)) == 0:
            flist.append(filename[:-4])

    if len(flist) > 0:

        # sort by increasing c*tau
        flist.sort(key=lambda str: float(str.split("_")[2]))
        print "Files found for (", plots.hmass, ",", plots.xmass, ") = " + str(flist)
        flist = [str(a) + '.txt' for a in flist]

        # graph for limits, with specified number of lifetime points in each:
        plots.g = r.TGraph(2 + len(flist))
        plots.g_br1 = r.TGraph(2 + len(flist))
        plots.gest1 = r.TGraphErrors(2 + len(flist))
        plots.gest2 = r.TGraphErrors(2 + len(flist))
        lmax = -1
        lmin = 9999
        expLimitFactor = 1

        # Create dictionary to store limits results at all lifetimes.
        vecLims = []

        #--- loop over lifetimes
        for filename in flist:

            # Create object to store limit results at this lifetime.
            lims = limits()

            # Note c*tau
            lims.lt = float(filename[:-4].split("_")[2])
            print "Lifetime in " + FileDir + "/" + filename + " is " + str(lims.lt)

            # Note min and max lifetime seen at any point on curve.
            xmax_seen = max(xmax_seen, lims.lt)
            xmin_seen = min(xmin_seen, lims.lt)

            if lims.lt > lmax:
                lmax = lims.lt
            if lims.lt < lmin:
                lmin = lims.lt

            f = open(FileDir + "/" + filename)

            q = pickle.load(f)
            mh = q[0]
            mx = q[1]
            lims.ctauScale = q[2]
            lims.relerr = q[3]
            # Limits valid for small branching ratio * efficiency.
            lims.up_br0 = q[4]
            lims.est_br0 = q[6]
            lims.est1p_br0 = q[8]
            lims.est1m_br0 = q[10]
            lims.est2p_br0 = q[12]
            lims.est2m_br0 = q[14]
            # Limits valid for 100% branching ratio.
            lims.up_br1 = q[5]
            lims.est_br1 = q[7]
            lims.est1p_br1 = q[9]
            lims.est1m_br1 = q[11]
            lims.est2p_br1 = q[13]
            lims.est2m_br1 = q[15]
            # print "CHECK ",filename," ",mh," ",lims.up_br0, " ",lims.est1p_br0

            # Store limit results for this lifetime
            vecLims.append(lims)

        #--- loop over lifetimes again, now accessing them from stored results.

        for ctauIndex, lims in enumerate(vecLims):

            # c*tau
            lt = lims.lt
            # relative uncertainty on efficiency
            relerr = lims.relerr
            # Limits valid for small branching ratio * efficiency.
            up_br0 = lims.up_br0
            est_br0 = lims.est_br0
            est1p_br0 = lims.est1p_br0
            est1m_br0 = lims.est1m_br0
            est2p_br0 = lims.est2p_br0
            est2m_br0 = lims.est2m_br0
            # Limits valid for 100% branching ratio.
            up_br1 = lims.up_br1
            est_br1 = lims.est_br1
            est1p_br1 = lims.est1p_br1
            est1m_br1 = lims.est1m_br1
            est2p_br1 = lims.est2p_br1
            est2m_br1 = lims.est2m_br1

            # Band becomes unstable if too narrow.
            #if abs(est1p_br0 - est1m_br0) < 1.0e-1*est_br0:
            #	est1p_br0 = (1 + 1.0e-1)*est_br0
            #if abs(est2p_br0 - est2m_br0) < 2.0e-1*est_br0:
            #	est2p_br0 = (1 + 2.0e-1)*est_br0
            # Note min and max limit seen at any point on curve.

            # Optionally smooth statistical fluctuations in the limit curves.
            print "SMOOTH CHECK ", relerr
            if smooth and relerr > 0.2:
                lastInd = ctauIndex - 1
                nextInd = ctauIndex + 1
                # Do this only for points of transition between different generated c*tau values.
                if lastInd >= 0 and nextInd < len(vecLims):
                    lastLims = vecLims[lastInd]
                    nextLims = vecLims[nextInd]
                    lastScale = lastLims.ctauScale
                    print "SHIT", lastScale
                    # Only smear points immediately after transition, since have biggest weights.
                    if lastScale == 0.1 or lastScale == 1.0:
                        print "ALMOST SMOOTHING ", lastScale
                        if (up_br0 > max(lastLims.up_br0, nextLims.up_br0) or up_br0 < min(lastLims.up_br0,
                                                                                           nextLims.up_br0)):
                            print "SMOOTHING up_br0", mh, mx, lt
                            up_br0 = 0.5 * up_br0 + 0.25 * (lastLims.up_br0 + nextLims.up_br0)
                        if (up_br1 > max(lastLims.up_br1, nextLims.up_br1) or up_br1 < min(lastLims.up_br1,
                                                                                           nextLims.up_br1)):
                            print "SMOOTHING up_br1", mh, mx, lt
                            up_br1 = 0.5 * up_br1 + 0.25 * (lastLims.up_br1 + nextLims.up_br1)
                        if (est1p_br0 > max(lastLims.est1p_br0, nextLims.est1p_br0) or est1p_br0 < min(
                                lastLims.est1p_br0, nextLims.est1p_br0)):
                            print "SMOOTHING est1p_br0", mh, mx, lt
                            est1p_br0 = 0.5 * est1p_br0 + 0.25 * (lastLims.est1p_br0 + nextLims.est1p_br0)
                        if (est1m_br0 > max(lastLims.est1m_br0, nextLims.est1m_br0) or est1m_br0 < min(
                                lastLims.est1m_br0, nextLims.est1m_br0)):
                            print "SMOOTHING est1m_br0", mh, mx, lt
                            est1m_br0 = 0.5 * est1m_br0 + 0.25 * (lastLims.est1m_br0 + nextLims.est1m_br0)
                        if (est2p_br0 > max(lastLims.est2p_br0, nextLims.est2p_br0) or est2p_br0 < min(
                                lastLims.est2p_br0, nextLims.est2p_br0)):
                            print "SMOOTHING est2p_br0", mh, mx, lt
                            est2p_br0 = 0.5 * est2p_br0 + 0.25 * (lastLims.est2p_br0 + nextLims.est2p_br0)
                        if (est2m_br0 > max(lastLims.est2m_br0, nextLims.est2m_br0) or est2m_br0 < min(
                                lastLims.est2m_br0, nextLims.est2m_br0)):
                            print "SMOOTHING est2m_br0", mh, mx, lt
                            est2m_br0 = 0.5 * est2m_br0 + 0.25 * (lastLims.est2m_br0 + nextLims.est2m_br0)

                        # Do not expect a limit to be weaker than its two neighbouring points on the c*tau curve.
                        # So optionally reduce wiggles in the limit curve by preventing this (but not if it exceeds its
                        # neighbours by more than 20%, suggesting it is a real effect).
                        # Only necessary for 2*sigma expected upper limit, which has largest fluctuations.
                        #			if smooth:
                        #				if est2pLast > max(est2pBeforeLast, est2p_br0) and est2pLast < 1.2*max(est2pBeforeLast, est2p_br0):
                        #					print "WARNING: SMOOTHING +2*sigma expected band point ",i-1,"(",ltLast,") : ", est2pBeforeLast, " ", est2pLast, " ", est2p_br0, "\n"
                        #					est2pLast = max(est2pBeforeLast, est2p_br0)
                        #					plots.gest2.SetPoint(i-1,ltLast,(est2pLast+est2mLast)/2)
                        #					plots.gest2.SetPointError(i-1,ltLast,(est2pLast-est2mLast)/2)

                        #			est2pBeforeLast = est2pLast
                        #			est2pLast = est2p_br0
                        #			est2mLast = est2m_br0
                        #			ltLast = lt

            ymax_seen = max(ymax_seen, up_br0, est2p_br0)
            ymin_seen = min(ymin_seen, up_br0, est2m_br0)

            ibinIndex = ctauIndex + 1

            plots.g.SetPoint(ibinIndex, lt, up_br0)
            plots.g_br1.SetPoint(ibinIndex, lt, up_br1)

            plots.gest1.SetPoint(ibinIndex, lt, (est1p_br0 + est1m_br0) / 2)
            plots.gest1.SetPointError(ibinIndex, 0, (est1p_br0 - est1m_br0) / 2)
            plots.gest2.SetPoint(ibinIndex, lt, (est2p_br0 + est2m_br0) / 2)
            plots.gest2.SetPointError(ibinIndex, 0, (est2p_br0 - est2m_br0) / 2)

            # This is needed to ensure the curve extrapolates smoothly between the points.
            # i.e. Avoids "bouncing" mentioned in http://root.cern.ch/root/html/TGraphPainter.html
            if ibinIndex == 1 or ibinIndex == len(vecLims):
                if ibinIndex == 1:
                    ibinExtra = 0
                elif ibinIndex == len(vecLims):
                    ibinExtra = len(vecLims) + 1
                plots.g.SetPoint(ibinExtra, lt, up_br0)
                plots.g_br1.SetPoint(ibinExtra, lt, up_br1)
                plots.gest1.SetPoint(ibinExtra, lt, (est1p_br0 + est1m_br0) / 2)
                plots.gest1.SetPointError(ibinExtra, 0, (est1p_br0 - est1m_br0) / 2)
                plots.gest2.SetPoint(ibinExtra, lt, (est2p_br0 + est2m_br0) / 2)
                plots.gest2.SetPointError(ibinExtra, 0, (est2p_br0 - est2m_br0) / 2)

            print "PLOTTING ", filename, " mh=", plots.hmass, " tau=", lt, " obs=", up_br0, " est=", est_br0, " (1) ",\
                est1p_br0, "/", est1m_br0, " (2) ", est2p_br0, "/", est2m_br0, "\n"

        # Draw in order: +/- 2 sigma band, +/- 1 sigma band, actual

        plots.gest2.SetFillColor(r.kYellow)
        #		plots.gest2.SetFillStyle(3005)
        plots.gest2.SetFillStyle(1001)
        plots.gest2.SetMarkerStyle(0)
        plots.gest2.SetMarkerColor(0)
        plots.gest2.SetLineColor(0)
        plots.gest1.SetFillColor(r.kGreen)
        #		plots.gest1.SetFillStyle(3005)
        plots.gest1.SetFillStyle(1001)
        plots.gest1.SetMarkerStyle(0)
        plots.gest1.SetMarkerColor(0)
        plots.gest1.SetLineColor(0)
        if drawExpected:
            # 			plots.gest2.Draw("4 same")
            plots.gest1.Draw("4 same")

        plots.g.SetLineColor(jcol)
        plots.g.SetFillColor(0)
        plots.g.SetMarkerColor(jcol)
        plots.g.SetMarkerStyle(jpoly)
        plots.g.SetMarkerSize(1.5)
        plots.g.SetLineWidth(2)

        plots.g_br1.SetLineColor(jcol)
        plots.g_br1.SetFillColor(0)
        plots.g_br1.SetMarkerColor(jcol)
        plots.g_br1.SetMarkerStyle(jpoly)
        plots.g_br1.SetMarkerSize(1.5)
        plots.g_br1.SetLineWidth(2)
        plots.g_br1.SetLineStyle(2)

        # Plot all observed limit curves later, outside the loop, since otherwise
        # they can be covered by the expected limit curve.

        #plots.g.Fit("pol3", "", "", lmin, lmax)
        #f1 = plots.g.GetFunction("pol3")
        #f1 = r.TF1("f"+str(xmass), "1/([0]+[1]/x + [2]/(x*x) + [3]/(x*x*x))", lmin, lmax)
        #plots.g.Fit(f1, "", "", lmin, lmax)
        #f1.SetLineColor(jcol)

        jpoly += 1  # Change polymarker
        jcol += 1  # Change line color
        if jcol == 3 or jcol == 5:
            jcol += 1  # Don't want light green or yellow

# Plot observed limits (do after expected limits, to ensure not covered up)
for plots in plotsVec:
    if plots.g:
        plots.g.Draw("lp same")  # valid for small BR*efficiency
        plots.g_br1.Draw("l same")  # valid for 100% BR
        if Xlimits:
            leg.AddEntry(plots.g, "m_{X} = " + str(int(plots.xmass)) + " GeV/c^{2}")
        else:
            leg.AddEntry(plots.g, "m_{#tilde{q}} / m_{#chi} = " + str(int(plots.hmass)) + " / " + str(
                int(plots.xmass)) + " GeV/c^{2}")


# Add key to legend for expected limit band.
if drawExpected:
    for plots in plotsVec:
        if plots.gest1:
            leg.AddEntry(plots.gest1, "Expected limits (#pm1#sigma)", "f")
            #			leg.AddEntry(plots.gest2, "Expected limits (#pm2#sigma)", "f")
            # Only want one expected limit entry in key
            break

leg.Draw()
c.Update()

print "x-range seen = %s - %s" % (xmin_seen, xmax_seen)
print "y-range seen = %s - %s" % (ymin_seen, ymax_seen)
rangeError = False

if xmin_seen < xmin or xmax_seen > xmax:
    rangeError = True
    print "ERROR PlotLimitsLifetimeExpected MH=%f: Either xmax is too small or xmin too large. TGraphErrors may plot error bands incorrectly unless you adjust them: xmax %f -> %f; xmin %f -> %f" % (
        hmass, xmax, xmax_seen, xmin, xmin_seen)

if ymin_seen < ymin or ymax_seen > ymax:
    rangeError = True
    print "ERROR PlotLimitsLifetimeExpected MH=%f: Either ymax is too small or ymin too large. TGraphErrors may plot error bands incorrectly unless you adjust them: ymax %f -> %f; ymin %f -> %f" % (
        hmass, ymax, ymax_seen, ymin, ymin_seen)

if rangeError:
    exit(1)

suffix = ""
if logx == 1:
    if logy == 1:
        suffix = "LogXY"
    else:
        suffix = "LogX"
else:
    if logy == 1:
        suffix = "LogY"

#f = r.TFile("limits"+FileInfix+"Lifetime"+LeptonType+str(hmass)+suffix+"Exp2.png", "RECREATE")
#for plots in plotsVec:
#	plots.g.Write()
#	plots.gest1.Write()
#f.Close()

if Xlimits:
    c.Print("limitsLifetime" + LeptonType + "MH" + str(hmass) + ".png")
    c.Print("limitsLifetime" + LeptonType + "MH" + str(hmass) + ".pdf")
else:
    c.Print("limitsLifetime" + LeptonType + "_neutralino.png")
    c.Print("limitsLifetime" + LeptonType + "_neutralino.pdf")

#raw_input("Press ENTER to finish...")
#sys.stdin.read(1)
