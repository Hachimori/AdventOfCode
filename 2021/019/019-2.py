#!/usr/bin/env python
#
# Runtime is 35m10.494s
# Environment:
#   - 2.6 GHz 6 core intel Core i7
#   - 16 GB 2400 MHz DDR4 RAM

def read():
    ptListList = []

    try:
        while 1:
            raw_input()
            ptList = []
            while 1:
                s = raw_input()
                if not s: break
                ptList.append(map(int, s.split(',')))
            ptListList.append(ptList)
    except EOFError:
        pass

    return ptListList
            

def rotateX(ptList):
    for i in range(len(ptList)):
        ptList[i][1], ptList[i][2] = -ptList[i][2], ptList[i][1]


def rotateY(ptList):
    for i in range(len(ptList)):
        ptList[i][0], ptList[i][2] = -ptList[i][2], ptList[i][0]
    

def rotateZ(ptList):
    for i in range(len(ptList)):
        ptList[i][0], ptList[i][1] = -ptList[i][1], ptList[i][0]


def isMatch(ptList1, ptList2, scannerPt):
    for rotX in range(4):
        for rotY in range(4):
            for rotZ in range(4):
                for c1 in range(len(ptList1)):
                    for c2 in range(len(ptList2)):
                        diffList1 = [(p[0] - ptList1[c1][0], p[1] - ptList1[c1][1], p[2] - ptList1[c1][2]) for p in ptList1]
                        diffList2 = [(p[0] - ptList2[c2][0], p[1] - ptList2[c2][1], p[2] - ptList2[c2][2]) for p in ptList2]

                        cntMatch = 0
                        for diff in diffList2:
                            if diff in diffList1:
                                cntMatch += 1

                        if cntMatch >= 12:
                            dx = ptList1[c1][0] - ptList2[c2][0]
                            dy = ptList1[c1][1] - ptList2[c2][1]
                            dz = ptList1[c1][2] - ptList2[c2][2]
                            for i in range(len(ptList2)):
                                ptList2[i][0] += dx
                                ptList2[i][1] += dy
                                ptList2[i][2] += dz
                            scannerPt[0] = dx
                            scannerPt[1] = dy
                            scannerPt[2] = dz
                            return True
                        
                rotateZ(ptList2)
            rotateY(ptList2)
        rotateX(ptList2)
    
    return False


def work(ptListList):
    scannerPtList = [[0, 0, 0]]
    matchedPtListList = [ptListList[0]]
    del ptListList[0]

    while ptListList:
        for i in range(len(matchedPtListList)):
            for j in range(len(ptListList)):
                scannerPt = [-1, -1, -1]
                if isMatch(matchedPtListList[i], ptListList[j], scannerPt):
                    scannerPtList.append(scannerPt)
                    matchedPtListList.append(ptListList[j])
                    del ptListList[j]
                    break

    maxV = 0
    for i in range(len(scannerPtList)):
        for j in range(i + 1, len(scannerPtList)):
            total = 0
            for k in range(3):
                total += abs(scannerPtList[i][k] - scannerPtList[j][k])
            maxV = max(maxV, total)
    print maxV


if __name__ == "__main__":
    work(read())
