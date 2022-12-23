#!/usr/bin/env python

def read():
    ptList = []
    r = 0
    while 1:
        try:
            line = raw_input()
            for c in range(len(line)):
                if line[c] == '#':
                    ptList.append((r, c))
        except EOFError:
            break
        r += 1
    return ptList


def printState(ptList):
    n = len(ptList)
    maxR = -10**10
    minR = 10**10
    maxC = -10**10
    minC = 10**10
    for (r, c) in ptList:
        maxR = max(maxR, r)
        minR = min(minR, r)
        maxC = max(maxC, c)
        minC = min(minC, c)
    for r in range(minR, maxR + 1):
        toPrint = ''
        for c in range(minC, maxC + 1):
            if (r, c) in ptList:
                toPrint += '#'
            else:
                toPrint += '.'
        print toPrint
    print ""


def work(ptList):
    n = len(ptList)

    toList = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    surroundRC = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    to2checkList = {
        (-1, 0): [(-1, -1), (-1, 0), (-1, 1)],
        (1, 0): [(1, -1), (1, 0), (1, 1)],
        (0, -1): [(-1, -1), (0, -1), (1, -1)],
        (0, 1): [(-1, 1), (0, 1), (1, 1)]
    }

    for _ in range(10):
        moveCandiList = [-1 for i in range(n)]

        for i in range(n):
            hasSurround = False
            for (dr, dc) in surroundRC:
                if (ptList[i][0] + dr, ptList[i][1] + dc) in ptList:
                    hasSurround = True
                    break

            if hasSurround:
                for moveIdx in range(4):
                    movable = True
                    for (dr, dc) in to2checkList[toList[moveIdx]]:
                        if (ptList[i][0] + dr, ptList[i][1] + dc) in ptList:
                            movable = False
                            break
                    if movable:
                        moveCandiList[i] = moveIdx
                        break

        ptCandiList = []
        for i in range(n):
            if moveCandiList[i] != -1:
                dr, dc = toList[moveCandiList[i]]
                ptCandiList.append((ptList[i][0] + dr, ptList[i][1] + dc))

        nextPtList = []
        for i in range(n):
            if moveCandiList[i] != -1:
                dr, dc = toList[moveCandiList[i]]
                if ptCandiList.count((ptList[i][0] + dr, ptList[i][1] + dc)) >= 2:
                    nextPtList.append(ptList[i])
                else:
                    nextPtList.append((ptList[i][0] + dr, ptList[i][1] + dc))
            else:
                nextPtList.append(ptList[i])
            
        t = toList[0]
        del toList[0]
        toList.append(t)
        
        ptList = nextPtList
        # printState(ptList)


    maxR = -10**10
    minR = 10**10
    maxC = -10**10
    minC = 10**10
    for (r, c) in ptList:
        maxR = max(maxR, r)
        minR = min(minR, r)
        maxC = max(maxC, c)
        minC = min(minC, c)
    
    print (maxR - minR + 1) * (maxC - minC + 1) - n


if __name__ == "__main__":
    work(read())
