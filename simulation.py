import request

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






activeReq = []
nodestat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
isover = False
OCC = 40 #GHz
ECC = 2 #GHz
packetSize = 1 #bits
logFile = 'test_flow_barnes.log' # the log file that will be tested

#Global time constants to account for certain processes.
EccToOcc = OCC/ECC
tBuffer= 1 *EccToOcc
tMUX= 1*EccToOcc
tSequence= 1*EccToOcc
tSchedule= 1*EccToOcc
tOpenChannels= 1*EccToOcc
tCloseChannels= 1*EccToOcc

nodeBenchmarkList = convXYtoNode(logFile)
endFlag=False
t=0
reqCount=0

while ~isover:
    while t==nodeBenchmarkList[reqCount][4]:
        if reqCount+1 == len(nodeBenchmarkList):
            endFlag=True
        activeReq.append(request(nodeBenchmarkList[reqCount][0],nodeBenchmarkList[reqCount][1],nodeBenchmarkList[reqCount][3],nodeBenchmarkList[reqCount][4],nodeBenchmarkList[reqCount][4],endFlag))
    t += 1
