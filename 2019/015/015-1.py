#!/usr/bin/env python


def printBoard(rc2id, robotR, robotC):
    if not rc2id: return
    minR, minC = rc2id.keys()[0]
    maxR, maxC = rc2id.keys()[0]
    for (r, c) in rc2id.keys():
        minR = min(minR, r)
        minC = min(minC, c)
        maxR = max(maxR, r)
        maxC = max(maxC, c)

    for r in range(minR, maxR + 1):
        line = ''
        for c in range(minC, maxC + 1):
            if r == robotR and c == robotC:
                line += '@'
                continue
            tileId = -1 if (r, c) not in rc2id else rc2id[(r, c)]
            if tileId == -1:
                line += '.'
            elif tileId == 0:
                line += ' '
            elif tileId == 1:
                line += '#'
            elif tileId == 2:
                line += 'o'
            elif tileId == 3:
                line += 'S'
        print line
    print ""


dr = [-100, -1, 1, 0, 0]
dc = [-100, 0, 0, -1, 1]

def dfs(robotR, robotC, rc2id, visitedRC):
    if (robotR, robotC) not in rc2id:
        return [0]
    
    if (robotR, robotC) in rc2id and \
      rc2id[(robotR, robotC)] == 1:
        return False

    visitedRC.add((robotR, robotC))
    
    for i in range(1, 5):
        nextR = robotR + dr[i]
        nextC = robotC + dc[i]
        if (nextR, nextC) in visitedRC:
            continue
        ret = dfs(nextR, nextC, rc2id, visitedRC)
        if ret:
            return [i] + ret
    return False


def calc(_vList):
    vList = {}
    for i in range(len(_vList)):
        vList[i] = _vList[i]

    # rc2id[(r, c)] := id
    # id:
    #    0: empty
    #    1: wall
    #    2: oxygen
    rc2id = {(0, 0): 0}
    robotR = 0
    robotC = 0
    moving = [0]
    
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
            printBoard(rc2id, robotR, robotC)
            b = getAddress(0)
            nInstruction = 2
            if moving[0] == 0:
                moving = dfs(robotR, robotC, rc2id, set([]))
                if not moving:
                    print "Search finish"
                    rc2id[(0, 0)] = 3
                    printBoard(rc2id, robotR, robotC)
                    break
            vList[b] = prevMove = moving[0] # input
            del moving[0]
        elif a == 4:
            b = getValue(0)
            nInstruction = 2
            # print 'output:', b # output b
            if b == 0:
                rc2id[(robotR + dr[prevMove], robotC + dc[prevMove])] = 1
            else:
                if b == 1:
                    rc2id[(robotR + dr[prevMove], robotC + dc[prevMove])] = 0
                else:
                    rc2id[(robotR + dr[prevMove], robotC + dc[prevMove])] = 2
                robotR += dr[prevMove]
                robotC += dc[prevMove]
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



vList = map(int, raw_input().split(','))
calc(vList)
