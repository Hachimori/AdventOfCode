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


def read():
    ch = []
    try:
        while 1:
            ch.append(list(raw_input()))
    except EOFError:
        pass
    return ch


def rec(preR, preC, curR, curC, sr, sc, depth, minStep, ch):
    minStep[curR][curC] = min(minStep[curR][curC], depth)
    for idx in range(4):
        nr = curR + dr[idx]
        nc = curC + dc[idx]
        if not (0 <= nr < len(ch) and 0 <= nc < len(ch[0])):
            continue
        if nr == preR and nc == preC:
            continue
        if not ch2outOK[ch[curR][curC]].count(idx):
            continue
        if not ch2inOK[ch[nr][nc]].count(idx):
            continue
        if nr == sr and nc == sc:
            continue
        rec(curR, curC, nr, nc, sr, sc, depth + 1, minStep, ch)


def work(ch):
    for r in range(len(ch)):
        for c in range(len(ch[r])):
            if ch[r][c] == 'S':
                # ch[r][c] = 'F' # for sample
                ch[r][c] = '-'  # for input
                sr = r
                sc = c

    minStep = [[INF for c in ch[0]] for r in ch]
    rec(-1, -1, sr, sc, sr, sc, 0, minStep, ch)

    maxV = 0
    for r in range(len(ch)):
        for c in range(len(ch[r])):
            if minStep[r][c] != INF:
                maxV = max(maxV, minStep[r][c])
    print maxV


if __name__ == "__main__":
    work(read())
