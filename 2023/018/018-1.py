#!/usr/bin/env python

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
row = 1000
col = 1000


def read():
    opList = []
    try:
        while 1:
            direct, step, color = raw_input().split()
            opList.append((direct, int(step), color))
    except EOFError:
        pass
    return opList


def color(initR, initC, isOutside, visited):
    Q = [(initR, initC)]
    isOutside[initR][initC] = True

    while Q:
        (r, c) = Q[0]
        del Q[0]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < row and 0 <= nc < col and not isOutside[nr][nc] and not visited[nr][nc]:
                isOutside[nr][nc] = True
                Q.append((nr, nc))


def work(opList):
    visited = [[False for c in range(col)] for r in range(row)]
    curR = 500
    curC = 500

    directList = "URDL"
    for (direct, step, _) in opList:
        dIdx = directList.index(direct)
        for i in range(step):
            curR += dr[dIdx]
            curC += dc[dIdx]
            visited[curR][curC] = True

    isOutside = [[False for c in range(col)] for r in range(row)]
    for r in range(row):
        for c in range(col):
            if not (r == 0 or r == row - 1 or c == 0 or c == col - 1):
                continue
            if isOutside[r][c] or visited[r][c]:
                continue
            color(r, c, isOutside, visited)

    ans = row * col
    for r in range(row):
        for c in range(col):
            ans -= isOutside[r][c]
    print ans


if __name__ == "__main__":
    work(read())
