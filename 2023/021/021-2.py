#!/usr/bin/env python

def read():
    ch = []
    try:
        while 1:
            ch.append(list(raw_input()))
    except EOFError:
        pass
    return ch


def calc(ch, maxStep, initR, initC):
    row = len(ch)
    col = len(ch[0])

    isAvail = [[False for c in range(col)] for r in range(row)]
    isAvail[initR][initC] = True

    for step in range(maxStep):
        nex = [[False for c in range(col)] for r in range(row)]
        for r in range(row):
            for c in range(col):
                if not isAvail[r][c]:
                    continue
                dr = [-1, 0, 1, 0]
                dc = [0, 1, 0, -1]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (0 <= nr < row and 0 <= nc < col):
                        continue
                    if ch[nr][nc] == '#':
                        continue
                    nex[nr][nc] = True
        isAvail = nex

    cnt = 0
    for r in range(row):
        for c in range(col):
            cnt += isAvail[r][c]
    return cnt


def work(ch):
    # row = col = 131
    row = len(ch)
    col = len(ch[0])

    odd = calc(ch, 301, row / 2, col / 2)
    even = calc(ch, 300, row / 2, col / 2)

    ans = 0

    n = 26501365 / 131

    # Full
    ans += n * even + (n - 1) * odd
    ans += 2 * (n * (n - 1) / 2 * even + (n - 1) * (n - 2) / 2 * odd)

    # Part - 1
    ans += n * calc(ch, 64, 0, 0)
    ans += n * calc(ch, 64, row - 1, 0)
    ans += n * calc(ch, 64, 0, col - 1)
    ans += n * calc(ch, 64, row - 1, col - 1)

    # Part - 2
    ans += (n - 1) * calc(ch, 195, 0, 0)
    ans += (n - 1) * calc(ch, 195, row - 1, 0)
    ans += (n - 1) * calc(ch, 195, 0, col - 1)
    ans += (n - 1) * calc(ch, 195, row - 1, col - 1)

    # part - 3
    ans += calc(ch, 130, 0, col / 2)
    ans += calc(ch, 130, row / 2, 0)
    ans += calc(ch, 130, row - 1, col / 2)
    ans += calc(ch, 130, row / 2, col - 1)

    print ans


if __name__ == "__main__":
    work(read())
