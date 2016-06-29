#Global Constants for system parameters
OCC 		    = 40 #GHz
ECC             = 2 #GHz
packetSize      = 1 #bits
nodeCount       = 16 #number of nodes
weighted_cutoff = 9	#number of nodes preoccupied 


#Global time constants to account for certain processes.
EccToOcc       = OCC/ECC
tBuffer        = 1 *EccToOcc
tMUX           = 1 *EccToOcc
tSequence      = 1 *EccToOcc
tSchedule      = 1 *EccToOcc
tOpenChannels  = 1 *EccToOcc
tCloseChannels = 1 *EccToOcc


#Global Variable to act as system processes
activereq = []
nodestat  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
isover 	  = False


# tracks time in simulation, uses OCC as a time step
t = 0




while ~isover:
