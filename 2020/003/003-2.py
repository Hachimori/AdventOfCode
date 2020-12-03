#!/usr/bin/env python

def read():
    sList = []

    try:
        while 1:
            sList.append(raw_input())
    except EOFError:
        pass
    
    return sList


def getTrees(dr, dc, sList):
    r = 0
    c = 0
    cnt = 0

    while r < len(sList):
        cnt += sList[r][c] == '#'
        c = (c + dc) % len(sList[r])
        r += dr
    return cnt


def work(sList):
    ans = 1

    for (dr, dc) in ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1)):
        ans *= getTrees(dr, dc, sList)
    print ans

    
if __name__ == "__main__":
    work(read())
