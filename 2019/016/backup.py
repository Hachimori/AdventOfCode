#!/usr/bin/env python

PHASE = 100

vList = map(int, raw_input())

pattern = [0, 1, 0, -1]
for phase in range(PHASE):
    newVList = []
    for i in range(1, len(vList) + 1):
        total = 0

        nRep = 1
        nRepIdx = 0
        for j in range(len(vList)):
            if nRep == i:
                nRep = 0
                nRepIdx = (nRepIdx + 1) % len(pattern)
            
            total += vList[j] * pattern[nRepIdx]
            nRep += 1
        newVList.append(abs(total) % 10)
    vList = newVList
    
print "".join(map(str, vList[:8]))
