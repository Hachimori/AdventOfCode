#!/usr/bin/env python

def read():
    lineList = []

    try:
        while 1:
            xy1, _, xy2 = raw_input().split()
            x1, y1 = map(int, xy1.split(','))
            x2, y2 = map(int, xy2.split(','))
            lineList.append(((x1, y1), (x2, y2)))
    except EOFError:
        pass

    return lineList


def work((lineList)):
    cnt = [[0 for j in range(1000)] for i in range(1000)]
    
    for ((x1, y1), (x2, y2)) in lineList:
        if x1 == x2:
            bgn, end = min(y1, y2), max(y1, y2)
            for y in range(bgn, end + 1):
                cnt[x1][y] += 1
        elif y1 == y2:
            bgn, end = min(x1, x2), max(x1, x2)
            for x in range(bgn, end + 1):
                cnt[x][y1] += 1
        else:
            nMove = abs(x1 - x2) + 1
            dx = +1 if x1 < x2 else -1
            dy = +1 if y1 < y2 else -1
            for i in range(nMove):
                cnt[x1 + i * dx][y1 + i * dy] += 1
            
    ans = 0
    for i in range(1000):
        for j in range(1000):
            ans += cnt[i][j] >= 2
    print ans
                

if __name__ == "__main__":
    work(read())
