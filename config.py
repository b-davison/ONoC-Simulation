activeReq = []
nodestate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
isover = False
OCC = 40 #GHz
ECC = 2 #GHz
packetSize = 1 #bits
nodeCount = 16
logFile = 'flow_barnes.log' # the log file that will be tested
weighted_cutoff = 9 # max nodes allowedd to be bypassed on furthest path

#Global time constants to account for certain processes.
EccToOcc       = OCC/ECC
tBuffer        = 1 *EccToOcc
tMUX           = 1 *EccToOcc
tSequence      = 1 *EccToOcc
tSchedule      = 1 *EccToOcc
tOpenChannels  = 1 *EccToOcc
tCloseChannels = 1 *EccToOcc

#Global clock cycle constant for tracking t clock intervals
t = 0