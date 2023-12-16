#!/usr/bin/env python

import sys
sys.setrecursionlimit(40000)


def read():
    ch = []
    try:
        while 1:
            ch.append(raw_input())
    except EOFError:
        pass
    return ch


def rec(r, c, dIdx, visited, row, col, ch):
    if not (0 <= r < row and 0 <= c < col):
        return
    if visited[r][c][dIdx]:
        return
    visited[r][c][dIdx] = True

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    if (ch[r][c] == '-' and dIdx % 2 == 1) or (ch[r][c] == '|' and dIdx % 2 == 0):
        dIdx = (dIdx + 1) % 4
        rec(r + dr[dIdx], c + dc[dIdx], dIdx, visited, row, col, ch)
        dIdx = (dIdx + 2) % 4
        rec(r + dr[dIdx], c + dc[dIdx], dIdx, visited, row, col, ch)
    elif ch[r][c] == '/':
        if dIdx % 2 == 0:
            dIdx = (dIdx + 3) % 4
        else:
            dIdx = (dIdx + 1) % 4
        rec(r + dr[dIdx], c + dc[dIdx], dIdx, visited, row, col, ch)
    elif ch[r][c] == '\\':
        if dIdx % 2 == 0:
            dIdx = (dIdx + 1) % 4
        else:
            dIdx = (dIdx + 3) % 4
        rec(r + dr[dIdx], c + dc[dIdx], dIdx, visited, row, col, ch)
    else:
        rec(r + dr[dIdx], c + dc[dIdx], dIdx, visited, row, col, ch)


def work(ch):
    row = len(ch)
    col = len(ch[0])

    visited = [[[False for d in range(4)] for c in range(col)] for r in range(row)]
    rec(0, 0, 0, visited, row, col, ch)

    ans = 0
    for r in range(row):
        for c in range(col):
            ans += any(v for v in visited[r][c])
    print ans


if __name__ == "__main__":
    work(read())
