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

    for checkY in range(0,4000001):
        for i in range(len(distList)):
            centerX, centerY = xyxyList[i][0], xyxyList[i][1]
            distY = abs(centerY - checkY)
            checkXList = [centerX - distList[i] + distY - 1, centerX + distList[i] - distY + 1]
            
            if checkXList[0] > checkXList[1]:
                continue
            
            for checkX in checkXList:
                if not (0 <= checkX <= 4000000):
                    continue
                isPossiblePos = True
                for j in range(len(xyxyList)):
                    if abs(xyxyList[j][0] - checkX) + abs(xyxyList[j][1] - checkY) <= distList[j]:
                        isPossiblePos = False
                        break
                if isPossiblePos:
                    print checkX * 4000000 + checkY
                    return


if __name__ == "__main__":
    work(read())
