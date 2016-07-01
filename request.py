class request:
	# This is the initializer for the request class
    def __init__(self, sourceNode, destNode, volume, timeStamp,timeTrack,lastReqFlag):
        self.sourceNode     = sourceNode
        self.destNode       = destNode
        self.volume         = volume
        self.timeStamp      = timeStamp
        self.timeTrack      = timeStamp
        self.lastReqFlag    = lastReqFlag
        self.scheduled      = False
        self.transmitted    = False
        self.right          = False





    def schedule(self):
		# makes source lower than destination
        if self.sourceNode > self.destNode:
			temp = self.sourceNode
			self.sourceNode = self.destNode
			self.destNode = temp 

		# checks for shortest path
		# first if triggers if direct (e.g. 123...14 15 16) path is the shortest or equadistant, elif triggers if opposite direction path is shorter
        if (self.destNode - self.sourceNode) <= (nodeCount - self.destNode + self.sourceNode):
			# checks that path is available and if so reserves path
            if (nodestat[self.sourceNode:(self.destNode +1)] == [False] * (self.destNode +1 - self.sourceNode)):     
                nodestat[self.sourceNode:(dself.estNode +1)] = [1] * ((self.destNode +1) - self.sourceNode)
                self.schedule = True
                self.timeTrack += tBuffer + tMUX + tSequence + tSchedule # insert time parameters
                self.right = True

            elif (nodeCount - self.destNode + self.sourceNode) < weighted_cutoff:
                if (nodestat[0:(self.sourceNode +1)] == [False] * (self.sourceNode +1)) & (nodestat[self.destNode:] == [False] * (self.nodeCount - self.destNode)):
                    for i in nodestat:
                        if i <= self.sourceNode | i >= self.destNode:
                            nodestat[i] = 1
                    self.schedule = True
                    self.timeTrack += tBuffer + tMUX + tSequence + tSchedule # insert time parameters
                else:
                    self.timeTrack += 1
            else:
                self.timeTrack += 1
        else:
            if (nodestat[0:(self.sourceNode +1)] == [False] * (self.sourceNode +1)) & (nodestat[self.destNode:] == [False] * (nodeCount - self.destNode)):
                for i in nodestat:
                    if i <= self.sourceNode | i >= self.destNode:
                        nodestat[i] = 1
                self.schedule = True
                self.timeTrack += tBuffer + tMUX + tSequence + tSchedule # insert time parameters
            elif (self.destNode - self.sourceNode) < weighted_cutoff:
                if nodestat[self.sourceNode:(self.destNode +1)] == [False] * (self.destNode +1 - self.sourceNode):     
                    nodestat[self.sourceNode:(self.destNode +1)] = [1] * ((self.destNode +1) - self.sourceNode)
                    self.schedule = True
                    self.timeTrack += tBuffer + tMUX + tSequence + tSchedule # insert time parameters
                    self.right = True
                else:
                    self.timeTrack += 1
            else:
                self.timeTrack += 1






    def transmit(self):
        volume = self.volume
        dataTransTime = volume*packetsize/(OCC*(10**9)) 
        self.timeTrack += tCloseChannels + topenChannels + dataTransTime #insert addition parameters
    def release(self):
        if self.right == True:
            nodestat[self.sourceNode:(self.destNode +1)] = [0] * ((self.destNode +1) - self.sourceNode)
        else:
            for i in nodestat:
                    if i <= self.sourceNode | i >= self.destNode:
                        nodestat[i] = 0
        if self.lastReqFlag:
            isover = True
        activeReq.remove(self)
    pass


    def reqProcessing(self, t):
        if ~self.scheduled:
            self.schedule()
        elif ~self.transmitted:
            self.transmit()
        elif self.timeTrack == t:
            self.release()
