#!/usr/bin/env python

def read():
    ch = []
    try:
        while 1:
            ch.append(list(raw_input()))
    except EOFError:
        pass
    return ch


def work(ch):
    row = len(ch)
    col = len(ch[0])
    isAvail = [[False for c in range(col)] for r in range(row)]

    for r in range(row):
        for c in range(col):
            if ch[r][c] == 'S':
                isAvail[r][c] = True
                ch[r][c] = '.'

    for step in range(64):
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
    print cnt


if __name__ == "__main__":
    work(read())
