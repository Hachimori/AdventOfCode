#!/usr/bin/env python

import sys
sys.setrecursionlimit(10 ** 5)


def read():
    ch = []
    try:
        while 1:
            ch.append(raw_input())
    except EOFError:
        pass
    return ch


def rec(preR, preC, r, c, dp, ch):
    row = len(ch)
    col = len(ch[0])

    if r == row - 1 and c == col - 2:
        return 0

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = -(10**10)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    dirStr = "^>v<"

    for i in range(4):
        if ch[r][c] in dirStr and dirStr.find(ch[r][c]) != i:
            continue

        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < row and 0 <= nc < col):
            continue
        if ch[nr][nc] == '#':
            continue
        if nr == preR and nc == preC:
            continue
        if ch[nr][nc] in dirStr and r == nr + dr[dirStr.find(ch[nr][nc])] and c == nc + dc[dirStr.find(ch[nr][nc])]:
            continue
        dp[r][c] = max(dp[r][c], rec(r, c, nr, nc, dp, ch) + 1)

    return dp[r][c]


def work(ch):
    row = len(ch)
    col = len(ch[0])
    dp = [[-1 for c in range(col)] for r in range(row)]
    print rec(-1, -1, 0, 1, dp, ch)


if __name__ == "__main__":
    work(read())
