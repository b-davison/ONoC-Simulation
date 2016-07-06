from request import request
import config

#Converts a log file of XY coordinates to node numbers and returns a reduced list of lists that contains the log information in its elements.
#Ex.     S|D |#|V|tStamp
#       [1,15,1,4 , 0  ],
#       [2,3,2,3  , 30 ],...
#       
def convXYtoNode(logFile):
    benchmark = []

    with open(logFile,"r") as bmread:
        for line in bmread:
            benchmarkLine = []
            benchmarkItems = line.split()
            for i in benchmarkItems:
                benchmarkLine.append(int(i))
            benchmark.append(benchmarkLine)

    newBenchmark = []
    for row in benchmark:
        if (row[0] != 0) & (row[2] != 0):
            newRow = [(row[0] - 1) * 8 + row[1], (row[2] - 1) * 8 + row[3]]
            newRow.extend(row[4:])
            newBenchmark.append(newRow)
    return newBenchmark


nodeBenchmarkList = convXYtoNode(config.logFile)
listLen = len(nodeBenchmarkList)
print listLen
reqCount = 0
endFlag = False
t = 0

while config.isover == False:
    while  (t == nodeBenchmarkList[reqCount][4]):
        if reqCount+1 == listLen:
            endFlag = True
        config.activeReq.append(request(nodeBenchmarkList[reqCount][0],nodeBenchmarkList[reqCount][1],nodeBenchmarkList[reqCount][3],nodeBenchmarkList[reqCount][4],nodeBenchmarkList[reqCount][4],endFlag))
        if endFlag == False:
            reqCount += 1


    for req in config.activeReq:
    	req.reqProcessing(t)
        print req.scheduled
        print req.transmitted
        print req.timeStamp
        print req.timeTrack
        print t
        print "\n"
    t += 1


    print config.activeReq
    print "new list \n \n \n"


print t
