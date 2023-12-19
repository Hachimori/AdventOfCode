#!/usr/bin/env python

def read():
    opList = []
    try:
        while 1:
            _, _, color = raw_input().split()
            opList.append((int(color[2:7], 16), int(color[7])))
    except EOFError:
        pass
    return opList


def work(opList):
    minX = 0
    maxX = 0

    curX = 0
    curY = 0

    horizontalLines = []
    xList = [-1, 0, 1]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for (idx, (step, direct)) in enumerate(opList):
        nx = curX + step * dx[direct]
        ny = curY + step * dy[direct]
        if curY == ny:
            x1, y1, x2, y2 = curX, curY, nx, ny
            if (opList[idx - 1][1] + 1) % 4 != direct:
                x1 += dx[direct]
            if (direct + 1) % 4 != opList[(idx + 1) % len(opList)][1]:
                x2 -= dx[direct]
            horizontalLines.append((min(x1, x2), y1, max(x1, x2), y2))
        curX = nx
        curY = ny
        minX = min(minX, curX)
        maxX = max(maxX, curX)
        xList.append(curX - 1)
        xList.append(curX)
        xList.append(curX + 1)

    xList = sorted(set(xList))

    ans = 0
    for xIdx in range(len(xList) - 1):
        yList = []
        for (x1, y1, x2, y2) in horizontalLines:
            if x1 <= xList[xIdx] <= x2:
                yList.append(y1)
        yList.sort()
        for yIdx in range(0, len(yList), 2):
            ans += (yList[yIdx + 1] - yList[yIdx] + 1) * (xList[xIdx + 1] - xList[xIdx])
    print ans


if __name__ == "__main__":
    work(read())
