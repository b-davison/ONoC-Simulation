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
        
    def __del__(self):
        
    def reqProcessing(t):
        if ~scheduled:
            schedule(t)
        elif ~transmitted:
            transmit()
        elif timeTrack == t:


    def schedule():
        # makes source lower than destination
        if sourceNode > destNode:
            temp = sourceNode
            sourceNode = destNode
            destNode = temp 

        # checks for shortest path
        # first if triggers if direct (e.g. 123...14 15 16) path is the shortest or equadistant, elif triggers if opposite direction path is shorter
        if (destNode - sourceNode) =< (nodeCount - destNode + sourceNode):
            # checks that path is available and if so reserves path
            if nodestat[sourceNode:(destNode +1)] == [False] * (destNode +1 - sourceNode)     
                global nodestat[sourceNode:(destNode +1)] = [1] * ((destNode +1)-sourceNode)
                schedule = True
                timeTrack += timeSchedule # insert time parameters

            elif (nodeCount - destNode + sourceNode) < weighted_cutoff
                if (nodestat[0:(sourceNode +1)] == [False] * (sourceNode +1)) & (nodestat[destNode:] == [False] * (nodeCount - destNode)):
                    for i in nodestat:
                        if i <= sourceNode | i >= destNode:
                            global nodestat[i] = 1
                    schedule = True
                    timeTrack += timeSchedule # insert time parameters
                else:
                    timeTrack += 1
            else:
                timeTrack += 1
        else:
            if (nodestat[0:(sourceNode +1)] == [False] * (sourceNode +1)) & (nodestat[destNode:] == [False] * (nodeCount - destNode)):
                for i in nodestat:
                    if i <= sourceNode | i >= destNode:
                        global nodestat[i] = 1
                schedule = True
                timeTrack += timeSchedule # insert time parameters
            elif (destNode - sourceNode) < weighted_cutoff:
                if nodestat[sourceNode:(destNode +1)] == [False] * (destNode +1 - sourceNode):     
                    global nodestat[sourceNode:(destNode +1)] = [1] * ((destNode +1) - sourceNode)
                    schedule = True
                    timeTrack += timeSchedule # insert time parameters
                else:
                    timeTrack += 1
            else:
                timeTrack += 1





    
    def transmit(): 
    pass
    
