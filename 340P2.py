# 340P2.py
# Reid Foster and Ethan Guthrie
# 03/03/2020
# Simulates paging on an operating system with Python.

# Libraries named after authors of this assignment contain methods written
# by the author after whom the file was named.
from ethan import *
from reid import *
# The sys library allows for python to access command-line arguments.
from sys import argv

def main():
    if len(argv) !=9:
        print("Usage:python3 340P2.py memorySize pageSize jobCount maxRunTime minRunTime maxMemory minMemory randomSeed")
        return -1

    #how would you do the example he gives with set RANDOMSEED=13

    # Getting command line arguments.
    memSize=int(argv[1])
    pSize=int(argv[2])
    jCount=int(argv[3])
    maxRT=int(argv[4])
    minRT=int(argv[5])
    maxMem=int(argv[6])
    minMem=int(argv[7])
    seed=int(argv[8])

    # Validating command line arguments and setting page count.
    if(memSize%pSize!=0):
        print("Page Size is not multiple of Memory Size")
        return -1
    pageCount=memSize/pSize

    # Creating jobs.
    jobs=createJobs(jCount,maxRT,minRT,maxMem,minMem,seed)

    # Printing output.
    
    printParameters(memSize,pSize,jCount,maxRT,minRT,maxMem,minMem,seed)
    printJobQueue(jobs)

main()