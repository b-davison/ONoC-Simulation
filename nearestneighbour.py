
import config
import time

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
def keyMapping(key):
    for row in benchmark:
        row[1] = key[row[1]]
        row[2] = key[row[2]]

startTime = time.time()
nodeBenchmarkList = convXYtoNode(config.logFile)


def rank():
	n = 0
	for row in trafficto:
		for i in range(0,n):
			trafcounts.append(row[i])
			trafpositions.append((n,i,row[i]))
		n += 1




trafficto = [[0 for col in range(16)] for row in range(16)]
for row in trafficto:
	print row 
trafcounts = []
trafpositions = []

def getkey(item):
	return item[2]

print '\n'

for row in nodeBenchmarkList:
	trafficto[row[0]][row[1]] += row[4]
	trafficto[row[1]][row[0]] += row[4]

for row in trafficto:
	print row 
	





print trafcounts

rank()
ntraffic = sorted(trafpositions, key=getkey)

print ntraffic