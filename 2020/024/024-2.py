#!/usr/bin/env python

MAX_V = 150
LOOP = 100


def read():
    xyList = []
    for i in range(int(raw_input())):
        xyList.append(map(int, raw_input().split()))
    return xyList


def work(xyList):
    xy2isBlack = {}

    for x in range(-MAX_V, MAX_V):
        for y in range(-MAX_V, MAX_V):
            xy2isBlack[(x, y)] = False

    for (x, y) in xyList:
        xy2isBlack[(x, y)] = True
    
    for loop in range(LOOP):
        nextXy2isBlack = {}
        
        for x in range(-MAX_V, MAX_V):
            for y in range(-MAX_V, MAX_V):
                dxList = [1, 0, -1, -1, 0, 1]
                dyList = [0, -1, -1, 0, 1, 1]
                
                cntBlack = 0
                for i in range(6):
                    nx = x + dxList[i]
                    ny = y + dyList[i]
                    if (nx, ny) in xy2isBlack:
                        cntBlack += xy2isBlack[(nx, ny)]

                if xy2isBlack[(x, y)]:
                    nextXy2isBlack[(x, y)] = False if cntBlack == 0 or cntBlack > 2 else True
                else:
                    nextXy2isBlack[(x, y)] = True if cntBlack == 2 else False
        
        xy2isBlack = nextXy2isBlack

    print sum(nextXy2isBlack.values())


if __name__ == "__main__":
    work(read())
