#!/usr/bin/env python

WINDOW = 25


def read():
    vList = []
    
    try:
        while 1:
            vList.append(int(raw_input()))
    except EOFError:
        pass
    
    return vList


def work(vList):
    for loop in range(WINDOW, len(vList)):
        isOk = False
        for i in range(loop - WINDOW, loop):
            for j in range(i + 1, loop):
                isOk |= vList[loop] == vList[i] + vList[j]
        
        if not isOk:
            print vList[loop]


if __name__ == "__main__":
    work(read())
