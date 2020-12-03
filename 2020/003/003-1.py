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
    r = 0
    c = 0
    cnt = 0

    while r < len(sList):
        cnt += sList[r][c] == '#'
        c = (c + 3) % len(sList[r])
        r += 1

    print cnt

    
if __name__ == "__main__":
    work(read())
