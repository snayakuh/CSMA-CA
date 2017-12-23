
# coding: utf-8

# In[8]:
"""
PREPARED BY:SUKANTI NAYAK
The 1-Persistent CSMA/CA
"""
import numpy as np
import random
import matplotlib.pyplot as py


tSlot=1.0
pLength=1.0
X=np.array([])
L=np.array([])

def countNumArrivals(lambd):
    cnt = 0
    t = 0
    while t < tSlot:
        t += random.expovariate(lambd)
        cnt += 1                ##Counts the no. of packets,waiting for the current transmission to complete.
    return cnt


def getProbSucc(lambd):
    BufferCap=1000
    nPkts=0
    sPkts = 0
    for i in range(BufferCap):
        nPkts+=countNumArrivals(lambd)
        if nPkts == 0:
            sPkts += 0
        else:
            sPkts += 1
    return float(sPkts)/nPkts     ##Throughput is the ratio of successful transmission to total number of packets.

print("\n\n-----------------------\n|  LAMBDA  |Throughput|\n-----------------------")
for lambd in np.arange(0.01, 5, .05):
    Thru = lambd*getProbSucc(lambd)
    print("| %f | %f |" %(lambd,Thru))
    X=np.append(X, Thru)
    L=np.append(L,lambd)
    
py.plot(L,X)
py.ylabel("Throughput\n")
py.xlabel("Arrival Rate(Lambda)\n")
py.title("Performance of 1-Persistent CSMA-CA\n")
py.show()

"""
The graph represents the throughput of the medium in a 1 persistent CSMA/CA Increases as the load on the network increases.
As we have assumed of perfect collision avoidance, so no collisions occurance, 
Additionally, Hidden node problem is not considered in this case as a perfect broadcast channel is assumed,
every terminal can listen to any other station's transmission instantaneously.
so When a station completes its transmission, in the next slot ,only one station successfully sends the packet.
Hence, with incrased load, throughput also increases in the absence of collison and hidden station problem.
"""




