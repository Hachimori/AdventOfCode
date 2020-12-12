#!/usr/bin/env python

def read():
    sList = []
    try:
        while 1:
            sList.append(raw_input())
    except EOFError:
        pass
    return sList


def work(sList):
    r, c = [0, 0]

    dire = 1
    dStr = 'NESW'
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    for s in sList:
        ch = s[0]
        v = int(s[1:])

        
        if ch in dStr:
            r += dr[dStr.index(ch)] * v
            c += dc[dStr.index(ch)] * v
        elif ch == 'L':
            dire = (dire + 3 * v / 90) % 4
        elif ch == 'R':
            dire = (dire + v / 90) % 4
        elif ch == 'F':
            r += dr[dire] * v
            c += dc[dire] * v

    print abs(r) + abs(c)


if __name__ == "__main__":
    work(read())
