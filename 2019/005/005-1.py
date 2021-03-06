#!/usr/bin/env python

def calc(vList):
    idx = 0
    while idx < len(vList):
        a = vList[idx] % 100

        if a not in [1, 2, 3, 4, 99]:
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
            vList[b] = 1 # input
        elif a == 4:
            b = getValue(0)
            nInstruction = 2
            print 'output:', b # output b
        else:
            break
        #vList[idx + 0] += nInstruction
        idx += nInstruction
    return vList[0]



vList = map(int, raw_input().split(','))

calc(vList)
