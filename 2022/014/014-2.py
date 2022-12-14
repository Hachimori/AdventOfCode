#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            line = raw_input()
            xyList = line.split('->')
            ret.append([map(int, xy.split(',')) for xy in xyList])
        except EOFError:
            break
    return ret


def drawWall((x1, y1), (x2, y2), isWall):
    if x1 == x2:
        dx = 0
    elif x1 < x2:
        dx = +1
    else:
        dx = -1

    if y1 == y2:
        dy = 0
    elif y1 < y2:
        dy = +1
    else:
        dy = -1

    while 1:
        isWall[y1][x1] = True
        if x1 == x2 and y1 == y2:
            break
        x1 += dx
        y1 += dy


def dropSuccess(isWall):
    x, y = 500, 0

    if isWall[y][x]:
        return False
    
    while 1:
        dx = [0, -1, 1]

        isDropping = False
        for i in range(3):
            if not isWall[y + 1][x + dx[i]]:
                y += 1
                x += dx[i]
                isDropping = True
                break
        
        if not isDropping:
            isWall[y][x] = True
            return True
    

def work((wallList)):
    maxY = 0
    for xyList in wallList:
        for (_, y) in xyList:
            maxY = max(maxY, y)
    
    row = maxY + 3
    col = 1000
    isWall = [[False for c in range(col)] for r in range(row)]
    
    for xyList in wallList:
        for i in range(len(xyList) - 1):
            drawWall(xyList[i], xyList[i + 1], isWall)
    drawWall((0, maxY + 2), (999, maxY + 2), isWall)
            
    cntDrop = 0
    while dropSuccess(isWall):
        cntDrop += 1

    print cntDrop
        
        
if __name__ == "__main__":
    work(read())
