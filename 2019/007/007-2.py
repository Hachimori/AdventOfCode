#!/usr/bin/env python
import itertools


def calc(idx, vList, inputSeq):
    output = []
    while idx < len(vList):
        a = vList[idx] % 100
        
        if a not in [1, 2, 3, 4, 5, 6, 7, 8, 99]:
            print a
            print "???"
            break

        # pos: 0, 1, 2, ...
        def getValue(pos):
            if vList[idx] < 0:
                print vList[idx]
                print "????"
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
                vList[b] = inputSeq[0] # consume input
                inputSeq.pop(0)
            else:
                return [idx, vList, output] # no input, process next amplifier
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
        idx += nInstruction
    print vList[idx: idx+3]
    return [idx, vList, output] # program halt, process next amplifier



original = map(int, raw_input().split(','))

maxValue = 0
for order in itertools.permutations([5, 6, 7, 8, 9]):
    # states[i] = (idx, vList, output)
    states = [[0, original[:], [order[0], 0]],
              [0, original[:], [order[1]]],
              [0, original[:], [order[2]]],
              [0, original[:], [order[3]]],
              [0, original[:], [order[4]]]
              ]

    haltCount = 0
    while haltCount < 3:
        for i in range(5):
            #print states[i]
            (nextIdx, nextVList, nextOutput) = calc(states[i][0], states[i][1], states[i][2])
            states[i][0] = nextIdx 
            states[i][1] = nextVList
            states[(i + 1) % 5][2].extend(nextOutput)
            if i == 4:
                if nextOutput:
                    maxValue = max(maxValue, max(nextOutput))
                    print nextOutput
                if len(nextOutput) == 0:
                    haltCount += 1
            

print maxValue
