#!/usr/bin/env python

import sys
sys.setrecursionlimit(10 ** 6)

INF = 1 << 30

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ch2inOK = {}
ch2inOK['|'] = [0, 2]
ch2inOK['-'] = [1, 3]
ch2inOK['L'] = [2, 3]
ch2inOK['J'] = [1, 2]
ch2inOK['7'] = [0, 1]
ch2inOK['F'] = [0, 3]
ch2inOK['.'] = []

ch2outOK = {}
ch2outOK['|'] = [0, 2]
ch2outOK['-'] = [1, 3]
ch2outOK['L'] = [0, 1]
ch2outOK['J'] = [0, 3]
ch2outOK['7'] = [2, 3]
ch2outOK['F'] = [1, 2]
ch2outOK['.'] = []

ch2exCh = {}
ch2exCh['|'] = [
    ['.', '#', '.'],
    ['.', '#', '.'],
    ['.', '#', '.']
]
ch2exCh['-'] = [
    ['.', '.', '.'],
    ['#', '#', '#'],
    ['.', '.', '.']
]
ch2exCh['L'] = [
    ['.', '#', '.'],
    ['.', '#', '#'],
    ['.', '.', '.']
]
ch2exCh['J'] = [
    ['.', '#', '.'],
    ['#', '#', '.'],
    ['.', '.', '.']
]
ch2exCh['7'] = [
    ['.', '.', '.'],
    ['#', '#', '.'],
    ['.', '#', '.']
]
ch2exCh['F'] = [
    ['.', '.', '.'],
    ['.', '#', '#'],
    ['.', '#', '.']
]
ch2exCh['.'] = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
]

def read():
    ch = []
    try:
        while 1:
            ch.append(list(raw_input()))
    except EOFError:
        pass
    return ch


def rec(curR, curC, visited, ch):
    visited[curR][curC] = True
    for idx in range(4):
        nr = curR + dr[idx]
        nc = curC + dc[idx]
        if not (0 <= nr < len(ch) and 0 <= nc < len(ch[0])):
            continue
        if not ch2outOK[ch[curR][curC]].count(idx):
            continue
        if not ch2inOK[ch[nr][nc]].count(idx):
            continue
        if visited[nr][nc]:
            continue
        rec(nr, nc, visited, ch)


def bfs(sr, sc, visitedEx, isInside, exCh):
    Q = [(sr, sc)]
    visitedEx[sr][sc] = True
    isInside[sr][sc] = False
    while Q:
        (r, c) = Q[0]
        del Q[0]
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if not (0 <= nr < len(exCh) and 0 <= nc < len(exCh[0])):
                continue
            if exCh[nr][nc] != '.':
                continue
            if visitedEx[nr][nc]:
                continue
            visitedEx[nr][nc] = True
            isInside[nr][nc] = False
            Q.append((nr, nc))


def work(ch):
    row = len(ch)
    col = len(ch[0])

    for r in range(row):
        for c in range(col):
            if ch[r][c] == 'S':
                # ch[r][c] = 'F' # for sample 1~3
                # ch[r][c] = '7' # for sample 4
                ch[r][c] = '-'  # for input
                sr = r
                sc = c

    visited = [[False for c in range(col)] for r in range(row)]
    rec(sr, sc, visited, ch)

    exCh = [['' for c in range(col * 3)] for r in range(row * 3)]
    for r in range(row):
        for c in range(col):
            targetCh = ch[r][c] if visited[r][c] else '.'
            for i in range(3):
                for j in range(3):
                    exCh[r * 3 + i][c * 3 + j] = ch2exCh[targetCh][i][j]

    visitedEx = [[False for c in range(col * 3)] for r in range(row * 3)]
    isInside = [[True for c in range(col * 3)] for r in range(row * 3)]
    for r in range(row * 3):
        for c in range(col * 3):
            if not (r == 0 or r == row * 3 - 1 or c == 0 or c == col * 3 - 1):
                continue
            if exCh[r][c] != '.':
                continue
            if visitedEx[r][c]:
                continue
            bfs(r, c, visitedEx, isInside, exCh)

    ans = 0
    for r in range(row):
        for c in range(col):
            if visited[r][c]:
                continue
            toAdd = 0
            for i in range(3):
                for j in range(3):
                    if exCh[r * 3 + i][c * 3 + j] != '.':
                        continue
                    if isInside[r * 3 + i][c * 3 + j]:
                        toAdd = 1
            ans += toAdd
    print ans


if __name__ == "__main__":
    work(read())
