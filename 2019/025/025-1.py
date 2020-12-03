#!/usr/bin/env python

import sys

def printBoard(rc2id, selfR, selfC, lastMove):
    if not rc2id: return
    minR, minC = rc2id.keys()[0]
    maxR, maxC = rc2id.keys()[0]
    for (r, c) in rc2id.keys():
        minR = min(minR, r)
        minC = min(minC, c)
        maxR = max(maxR, r)
        maxC = max(maxC, c)

    print "Current pos: (%d, %d)" % (selfR, selfC)
    for r in range(minR, maxR + 1):
        line = ''
        for c in range(minC, maxC + 1):
            tileId = 0 if (r, c) not in rc2id else rc2id[(r, c)]
            if r == selfR and c == selfC:
                tileId = 2
            if tileId == 0:
                line += '?'
            elif tileId == 1:
                line += '.'
            elif tileId == 2:
                if lastMove == 0:
                    line += '^'
                elif lastMove == 1:
                    line += '>'
                elif lastMove == 2:
                    line += 'v'
                elif lastMove == 3:
                    line += '<'
                else:
                    print "Error"
            else:
                print "Error"
        print line
    print ""

POSSIBLE_ITEM_LIST = ['whirled peas', 'bowl of rice', 'mutex', 'easter egg', 'mug', 'astronaut ice cream', 'tambourine', 'ornament']
WHITE_ITEM_LIST = []
BLACK_ITEM_LIST = ["photons", "escape pod", "molten lava", "giant electromagnet", "infinite loop"]

def getChoice(text, selfR, selfC, inventory):
    moveList = []
    itemList = []
    for line in text.split('\n'):
        if not line.startswith('- '):
            continue
        word = line[2:]
        if word in ["north", "east", "south", "west"]:
            moveList.append(word)
        elif word in WHITE_ITEM_LIST:
            itemList.append(word)
    
    if (selfR, selfC) == (4, -1) and sorted(inventory) != sorted(WHITE_ITEM_LIST) and "west" in moveList:
        moveList.remove("west")
    
    return moveList, itemList
    

def calc(_vList):
    vList = {}
    for i in range(len(_vList)):
        vList[i] = _vList[i]
    
    lastMove = 0
    selfR = 0
    selfC = 0
    inventory = []
    placeName = ''
    rc2id = {(0, 0): 1}

    inputQuery = []
    output = []
    idx = 0
    base = 0
    while True:
        a = vList[idx] % 100
        
        if a not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]:
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

            text = "".join(map(chr, output))
            if text:
                print text
                print ""
                printBoard(rc2id, selfR, selfC, lastMove)
                if "Alert! Droids on this ship are" in text:
                    return output
                print inventory

            if text.startswith("=="):
                placeName = text.split('\n')[0]
            
            moveList, itemList = getChoice(text, selfR, selfC, inventory)
            del output[:]
                
            # input
            if not inputQuery:
                for item in itemList:
                    inputQuery.extend(map(ord, "take " + item + "\n"))
                    inventory.append(item)

                direct = ["north", "east", "south", "west"]
                dr = [-1, 0, 1, 0]
                dc = [0, 1, 0, -1]
                for move in range(4):
                    goCandi = direct[(lastMove + 5 - move) % 4]
                    if goCandi in moveList:
                        lastMove = (lastMove + 5 - move) % 4
                        selfR += dr[lastMove]
                        selfC += dc[lastMove]
                        rc2id[(selfR, selfC)] = 1
                        inputQuery.extend(map(ord, goCandi))
                        inputQuery.append(ord('\n'))
                        break

            sys.stdout.write(chr(inputQuery[0]))
            
            vList[b] = inputQuery[0]
            del inputQuery[0]
        elif a == 4:
            b = getValue(0)
            nInstruction = 2
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
            base += b
        else:
            break
        idx += nInstruction

    return output



origVList = map(int, raw_input().split(','))

for mask in range(1 << len(POSSIBLE_ITEM_LIST)):
    WHITE_ITEM_LIST = []
    for i in range(len(POSSIBLE_ITEM_LIST)):
        if mask & (1 << i):
            WHITE_ITEM_LIST.append(POSSIBLE_ITEM_LIST[i])

    vList = origVList[:]
    output = calc(vList)
    print "".join(map(chr, output))


                
