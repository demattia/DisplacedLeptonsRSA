#!/bin/env python

import os, sys
import subprocess

# if len(sys.argv) != 1:
#     print "Please, provide the dir to check"


def checkAndResubmit(crabDir):
    print "Checking status and resubmitting failed jobs for:", crabDir
    # p = subprocess.Popen(["crab", "-status -getoutput -c "+crabDir], stdout=subprocess.PIPE)
    # out, err = p.communicate()
    # print out
    os.system("crab -status -getoutput -c "+crabDir+" > monitorTmpLog.txt")

    p = subprocess.Popen(["crab", "-status", "-c", crabDir], stdout=subprocess.PIPE)
    out, err = p.communicate()
    # print out

    totalJobs = 0
    jobsWithExitCodeZero = 0
    jobsToResubmit = []
    takeNext = False
    created = False
    createdList = ""
    running = False
    runningList = ""
    cancelled = False
    # cancelledList = ""
    takeNextToNext = 0
    for line in out.split('\n'):
        if line.find("Total") != -1:
            totalJobs = int(line.split()[1])
        # print line
        if takeNextToNext == 1:
            takeNext = True
        if takeNextToNext > 0:
            takeNextToNext -= 1
        if created:
            print line
            createdList += line
            created = False
        if running:
            print line
            runningList += line
            running = False
        if cancelled:
            print line
            os.system("crab -kill "+line.split(':')[1].strip()+" -c "+crabDir)
            # cancelledList += line
            cancelled = False
        if takeNext:
            # print line
            # if jobsToResubmit != "": jobsToResubmit += ','
            # jobsToResubmit += line.split(':')[1].strip()
            jobsToResubmit += [line.split(':')[1].strip()]
            takeNext = False
        if line.find('>>>>') != -1 and line.find('Retrieved') == -1 and line.find('Submitted') == -1 and line.find('Done') == -1:
            if line.find('Created') != -1:
                print "Warning: the following jobs are in status created"
                created = True
            elif line.find('Running') != -1:
                print "The following jobs are in status running"
                running = True
            elif line.find('Cancelled') != -1:
                print "the following jobs are Cancelled and will be resubmitted"
                takeNext = True
                cancelled = True
            elif line.find('Aborted') != -1:
                print "the following jobs are Aborted and will be resubmitted"
                takeNextToNext = 2
            else:
                print line.split(':')
                exitCode = line.split(':')[1].strip()
                if exitCode != "0":
                    print "The following jobs have exitCode =", exitCode, "and will be resubmitted"
                    takeNext = True
                else:
                    jobsWithExitCodeZero = int(line.split()[1])

    if len(jobsToResubmit) == 0:
        print "No job to resubmit at this time"
    else:
        print "\nResubmitting all jobs:", jobsToResubmit

        print jobsToResubmit

    for element in jobsToResubmit:
        print "Resubmitting jobs:", element
        # p = subprocess.Popen(["crab", "-resubmit "+element+" -c "+crabDir], stdout=subprocess.PIPE)
        # out, err = p.communicate()
        # print "out: ", out
        os.system("crab -resubmit "+element+" -c "+crabDir)

    print ""
    print "Summary for "+crabDir+":"
    print "--------\n"
    print "Total number of jobs:", totalJobs
    print "Number of jobs in status done (exit code 0):", jobsWithExitCodeZero
    print "Jobs in status created:"
    print createdList
    print "Jobs in status running:"
    print runningList
    print ""
    print "Percentange of successfully completed jobs: "+str(int(float(jobsWithExitCodeZero)/float(totalJobs)*100))+"%"
    if totalJobs == jobsWithExitCodeZero:
        print "All jobs completed sucessfully!"
    # Leave an empty line at the end
    print ""


# Running
while True:
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.001")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.001")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.001")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.001")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.001")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_800.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_80.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.001")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_100.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_150_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_50_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.008")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.04")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.002")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_1.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.06")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.02")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_0.08")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_4.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_1000.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_40.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_8.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_50_20.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_20_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_50_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_200.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_0.01")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_6.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.001")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.004")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.006")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.1")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_10.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_50_60.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_200_20_2.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.2")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.4")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_20_600.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.6")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_1000_350_0.8")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_400_150_400.0")
    checkAndResubmit("counting_job_output_Combined_Bayesian/Muons_125_20_6.0")
