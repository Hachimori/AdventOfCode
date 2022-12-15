#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            line = raw_input()
            nums = "".join([ch if ch.isdigit() or ch == '-' else ' ' for ch in line ]).split()
            ret.append(map(int, nums))
        except EOFError:
            break
    return ret


def work(xyxyList):
    distList = []
    for (x1, y1, x2, y2) in xyxyList:
        distList.append(abs(x1 - x2) + abs(y1 - y2))

    xSet = set([])
    checkY = 2000000
    for i in range(len(distList)):
        centerX, centerY = xyxyList[i][0], xyxyList[i][1]
        distY = abs(centerY - checkY)
        for x in range(centerX - distList[i] + distY, centerX + distList[i] - distY + 1):
            xSet.add(x)

    for (x1, y1, x2, y2) in xyxyList:
        if y1 == checkY:
            xSet.discard(x1)
        if y2 == checkY:
            xSet.discard(x2)
    
    print len(xSet)


if __name__ == "__main__":
    work(read())
