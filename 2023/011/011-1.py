#!/usr/bin/env python

def read():
    ch = []
    try:
        while 1:
            ch.append(raw_input())
    except EOFError:
        pass
    return ch


def calc((r1, c1), (r2, c2), r2isEmpty, c2isEmpty):
    ret = 0

    for rr in range(min(r1, r2), max(r1, r2)):
        ret += 2 if r2isEmpty[rr] else 1

    for cc in range(min(c1, c2), max(c1, c2)):
        ret += 2 if c2isEmpty[cc] else 1

    return ret


def work(ch):
    row = len(ch)
    col = len(ch[0])

    ptList = []
    for r in range(row):
        for c in range(col):
            if ch[r][c] == '#':
                ptList.append((r, c))

    r2isEmpty = [all(ch[r][c] == '.' for c in range(col)) for r in range(row)]
    c2isEmpty = [all(ch[r][c] == '.' for r in range(row)) for c in range(col)]

    ans = 0
    for i in range(len(ptList)):
        for j in range(i + 1, len(ptList)):
            ans += calc(ptList[i], ptList[j], r2isEmpty, c2isEmpty)
    print ans


if __name__ == "__main__":
    work(read())
