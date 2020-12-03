#!/usr/bin/env python

import time

class ComputerState:
    robotId = 0
    vList = {}
    idx = 0
    inputList = []
    outputList = []
    base = 0
    

def calc(state, computer2state):
    vList = state.vList
    idx = state.idx
    base = state.base
    inputList = state.inputList
    outputList = state.outputList

    a = vList[idx] % 100

    if a not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]:
        print a
        print "???"
        return

    # pos: 0, 1, 2, ...
    def getValue(pos):
        if vList[idx] < 0:
            print vList[idx]
            print "????"
        mode = vList[idx] / 100 / (10 ** pos) % 10
        if mode == 0:
            # address
            if vList[idx + pos + 1] not in vList:
                vList[vList[idx + pos + 1]] = 0
            return vList[vList[idx + pos + 1]]
        elif mode == 1:
            # value
            return vList[idx + pos + 1]
        elif mode == 2:
            # relative
            if not vList[idx + pos + 1] + base in vList:
                vList[vList[idx + pos + 1] + base] = 0
            return vList[vList[idx + pos + 1] + base]

    # pos: 0, 1, 2, ...
    def getAddress(pos):
        if vList[idx] < 0:
            print vList[idx]
            print "????"
        mode = vList[idx] / 100 / (10 ** pos) % 10
        if mode == 0:
            # address
            return vList[idx + pos + 1]
        elif mode == 1:
            # value
            print "value mode is not available in getAddress()"
            return -1
        elif mode == 2:
            # relative
            if not vList[idx + pos + 1] + base in vList:
                vList[vList[idx + pos + 1] + base] = 0
            return vList[idx + pos + 1] + base

    nInstruction = 0

    if a == 1:
        b, c, d = getValue(0), getValue(1), getAddress(2)
        nInstruction = 4
        vList[d] = b + c
    elif a == 2:
        b, c, d = getValue(0), getValue(1), getAddress(2)
        nInstruction = 4
        vList[d] = b * c
    elif a == 3:
        b = getAddress(0)
        nInstruction = 2
        # input
        if inputList:
            vList[b] = inputList[0]
            del inputList[0]
        else:
            vList[b] = -1
    elif a == 4:
        b = getValue(0)
        nInstruction = 2
        print 'output:', b # output b
        outputList.append(b)
        if len(outputList) % 3 == 0:
            print "Send packet: %d %d %d" % (outputList[-3], outputList[-2], outputList[-1])
            if outputList[-3] == 255:
                print "packet sent to 255"
                time.sleep(10)
            else:
                computer2state[outputList[-3]].inputList.append(outputList[-2])
                computer2state[outputList[-3]].inputList.append(outputList[-1])
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
        b, c, d = getValue(0), getValue(1), getAddress(2)
        nInstruction = 4
        if b < c:
            vList[d] = 1
        else:
            vList[d] = 0
    elif a == 8:
        b, c, d = getValue(0), getValue(1), getAddress(2)
        nInstruction = 4
        if b == c:
            vList[d] = 1
        else:
            vList[d] = 0
    elif a == 9:
        b = getValue(0)
        nInstruction = 2
        state.base += b
    else:
        return
        
    state.idx += nInstruction


COMPUTER = 50
origVList = map(int, raw_input().split(','))
computer2state = [ComputerState() for i in range(COMPUTER)]

for i in range(COMPUTER):
    vList = {}
    for j in range(len(origVList)):
        vList[j] = origVList[j]
    computer2state[i].vList = vList
    computer2state[i].robotId = i
    computer2state[i].idx = 0
    computer2state[i].inputList = [i]
    computer2state[i].outputList = []


while 1:
    for i in range(COMPUTER):
        calc(computer2state[i], computer2state)
