#!/usr/bin/env python

import sys
import copy
sys.setrecursionlimit(10 ** 5)


def read():
    ch = []
    try:
        while 1:
            ch.append(raw_input())
    except EOFError:
        pass
    return ch


def makeRC2ID(ch):
    row = len(ch)
    col = len(ch[0])

    rc2id = [[-1 for c in range(col)] for r in range(row)]
    rc2id[0][1] = 0
    rc2id[row - 1][col - 2] = 1
    nID = 2

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for r in range(row):
        for c in range(col):
            if ch[r][c] == '#':
                continue

            cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < row and 0 <= nc < col):
                    continue
                if ch[nr][nc] == '#':
                    continue
                cnt += 1

            if cnt >= 3:
                rc2id[r][c] = nID
                nID += 1

    return nID, rc2id


def getDist(preR, preC, curR, curC, adj, rc2id, ch):
    row = len(ch)
    col = len(ch[0])

    if preR != -1 and preC != -1 and rc2id[curR][curC] != -1:
        return (rc2id[curR][curC], 1)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(4):
        nr = curR + dr[i]
        nc = curC + dc[i]
        if not (0 <= nr < row and 0 <= nc < col):
            continue
        if nr == preR and nc == preC:
            continue
        if ch[nr][nc] == '#':
            continue

        t = getDist(curR, curC, nr, nc, adj, rc2id, ch)

        if not t:
            continue

        if preR == -1 and preC == -1:
            adj[rc2id[curR][curC]].append(t)
            continue
        else:
            return (t[0], t[1] + 1)

    return []


def makeAdj(nID, rc2id, ch):
    row = len(ch)
    col = len(ch[0])
    adj = [[] for i in range(nID)]

    for r in range(row):
        for c in range(col):
            if rc2id[r][c] != -1:
                getDist(-1, -1, r, c, adj, rc2id, ch)

    return adj


def rec(cur, visited, adj):
    if cur == 1:
        return 0

    maxV = -(10 ** 10)

    for (nex, dist) in adj[cur]:
        if visited[nex]:
            continue
        visited[nex] = True
        maxV = max(maxV, rec(nex, visited, adj) + dist)
        visited[nex] = False

    return maxV


def work(ch):
    row = len(ch)
    col = len(ch[0])

    nID, rc2id = makeRC2ID(ch)

    adj = makeAdj(nID, rc2id, ch)

    visited = [False for i in range(nID)]
    print rec(0, visited, adj)

if __name__ == "__main__":
    work(read())
