class request:
    # This is the initializer for the request class
    def __init__(self, sourceNode, destNode, volume, timeStamp,timeTrack,lastReqFlag):
        self.sourceNode = sourceNode
        self.destNode = destNode
        self.volume = volume
        self.timeStamp = timeStamp
        self.timeTrack = timeTrack
        self.lastReqFlag = lastReqFlag   
    pass
    
