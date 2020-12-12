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

    dStr = 'NESW'
    wpdr = [-1, 0, 1, 0]
    wpdc = [0, 1, 0, -1]
    wpr, wpc = -1, 10
    
    for s in sList:
        ch = s[0]
        v = int(s[1:])

        
        if ch in dStr:
            wpr += wpdr[dStr.index(ch)] * v
            wpc += wpdc[dStr.index(ch)] * v
        elif ch == 'L':
            for i in range(v / 90):
                wpr, wpc = -wpc, wpr
        elif ch == 'R':
            for i in range(v / 90):
                wpr, wpc = wpc, -wpr
        elif ch == 'F':
            r += wpr * v
            c += wpc * v

    print abs(r) + abs(c)


if __name__ == "__main__":
    work(read())
