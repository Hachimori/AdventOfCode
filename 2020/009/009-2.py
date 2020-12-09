#!/usr/bin/env python

INVALID_NUMBER = 2089807806


def read():
    vList = []
    
    try:
        while 1:
            vList.append(int(raw_input()))
    except EOFError:
        pass
    
    return vList


def work(vList):
    L = 0
    R = 0
    total = 0
    
    while R < len(vList):
        while total < INVALID_NUMBER and R < len(vList):
            total += vList[R]
            R += 1
            
        if total == INVALID_NUMBER and R - L >= 3:
            print min(vList[L:R]) + max(vList[L:R])

        total -= vList[L]
        L += 1


if __name__ == "__main__":
    work(read())
