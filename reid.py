# reid.py
# Reid Foster
# 03/03/2020
# Provides the following class:
#   Job
# Provides the following methods:
#   createJobs()
#   printJobQueue()
#   printParameters()

# Random class allows use of random integers (with seeds).
import random

# A class for holding information on a job
class Job:
    # Class initializers.
    STATUS = ['RUNNING', 'COMPLETE', 'WAITING', 'STOPPED']
    def __init__(self,memSize,runTime):
            self.memSize=memSize
            self.pageCount=0
            self.runTime=runTime
            self.timeRemaining=runTime
            self.complete=False
    
    # Class methods.
    def getMemSize(self):
        return self.memSize
    def getPageCount(self):
        return self.pageCount
    def getRunTime(self):
        return self.runTime
    def getStatus(self):
        return self.status
    def getTimeRemaining(self):
        return self.timeRemaining
    def runJob(self,timeslice):
        self.timeRemaining=self.timeRemaining-timeslice
        if(self.timeRemaining<=0):
            self.timeRemaining=0
            setStatus("COMPLETE")
    def setPageCount(self,count):
        self.pageCount=count
    def setStatus(self, status):
        if status not in STATUS:
            print("Cannot update status to invalid state: " + str(status))
            return False
        self.status = status
        return True

# Creates a list of jobs with given parameters
def createJobs(jCount,maxRT,minRT,maxMem,minMem,seed):
    random.seed(seed)
    jobs=[]
    for i in range(0,jCount):
        jMemSize=random.randint(minMem,maxMem)
        jRunTime=random.randint(minRT,maxRT)
        newJob=Job(jMemSize,jRunTime)
        jobs.append(newJob)
    return jobs

# Prints the job queue.
def printJobQueue(jobs):
    print("Job Queue:")
    print("Job #    Runtime    Memory")
    for i in range(0,len(jobs)):
        print((" "*(5-len(str(i))))+str(i)+(" "*(11-len(str(jobs[i].getRunTime()))))+str(jobs[i].getRunTime())+(" "*(10-len(str(jobs[i].getMemSize()))))+str(jobs[i].getMemSize()))

# Prints provided parameters.
def printParameters(memSize,pSize,jCount,maxRT,minRT,maxMem,minMem,seed):
    print("Simulator Parameters:")
    print("Memory Size:"+str(memSize))
    print("Page Size:"+str(pSize))
    print("Random Seed:"+str(seed))
    print("Number of Jobs:"+str(jCount))
    print("Runtime (min-max) timesteps:"+str(minRT)+"-"+str(maxRT))
    print("Memory (min-max):"+str(minMem)+"-"+str(maxMem))