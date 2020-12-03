#!/usr/bin/env python

def calc(vList, inputSeq):
    output = []
    idx = 0
    while idx < len(vList):
        a = vList[idx] % 100
        
        if a not in [1, 2, 3, 4, 5, 6, 7, 8, 99]:
            print a
            print "???"
            break

        # pos: 0, 1, 2, ...
        def getValue(pos):
            mode = vList[idx] / 100 / (10 ** pos) % 10
            if mode == 0:
                # address
                return vList[vList[idx + pos + 1]]
            else:
                # value
                return vList[idx + pos + 1]
            
        nInstruction = 0
        
        if a == 1:
            b, c, d = getValue(0), getValue(1), vList[idx + 3]
            nInstruction = 4
            vList[d] = b + c
        elif a == 2:
            b, c, d = getValue(0), getValue(1), vList[idx + 3]
            nInstruction = 4
            vList[d] = b * c
        elif a == 3:
            b = vList[idx + 1]
            nInstruction = 2
            if inputSeq:
                vList[b] = inputSeq[0] # input
                inputSeq.pop(0)
            else:
                vList[b] = 0 # input
        elif a == 4:
            b = getValue(0)
            nInstruction = 2
            print 'output:', b # output b
            output.append(b)
        elif a == 5:
            b = getValue(0)
            if b != 0:
                # idx + nInstruction => getValue(1)
                nInstruction = getValue(1) - idx
            else:
                nInstruction = 3
        elif a == 6:
            b = getValue(0)
            if b == 0:
                # idx + nInstruction => getValue(1)
                nInstruction = getValue(1) - idx
            else:
                nInstruction = 3
        elif a == 7:
            b, c, d = getValue(0), getValue(1), vList[idx + 3]
            nInstruction = 4
            if b < c:
                vList[d] = 1
            else:
                vList[d] = 0
        elif a == 8:
            b, c, d = getValue(0), getValue(1), vList[idx + 3]
            nInstruction = 4
            if b == c:
                vList[d] = 1
            else:
                vList[d] = 0
        else:
            break
        #vList[idx + 0] += nInstruction
        idx += nInstruction
    return output



original = map(int, raw_input().split(','))

maxValue = 0

import itertools
for order in itertools.permutations([0, 1, 2, 3, 4]):
    lastOutput = []
    for i in range(5):
        copy = original[:]
        curInput = [order[i]]
        curInput.extend(lastOutput)
        lastOutput = calc(copy, curInput)

    maxValue = max(maxValue, max(lastOutput))

print maxValue
