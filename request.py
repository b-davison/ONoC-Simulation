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
        else if ~transmitted:
            transmit()
        else if timeTrack == t:


    def schedule():
        if sourceNode < destNode:
            if nodestat[sourceNode:(destNode +1)] = False
                nodestat[sourceNode:(destNode +1)] = [1] * ((destNode +1)-sourceNode)
                schedule = True
                timeTrack += timeSchedule + time


    
    def transmit(): 
    pass
    
