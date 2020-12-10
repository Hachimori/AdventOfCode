#!/usr/bin/env python

def read():
    vList = []
    try:
        while 1:
            vList.append(int(raw_input()))
    except EOFError:
        pass
    return vList


def work(vList):
    vList.append(0)
    vList.sort()
    vList.append(vList[-1] + 3)
    
    cntDiff = [0, 0, 0, 0]
    
    for i in range(len(vList) - 1):
        cntDiff[vList[i + 1] - vList[i]] += 1

    print cntDiff[1] * cntDiff[3]

    
if __name__ == "__main__":
    work(read())
