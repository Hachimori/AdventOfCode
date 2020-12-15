#!/usr/bin/env python

def read():
    return map(int, raw_input().split(','))


def work(vList):
    v2idx = {}
    for i in range(len(vList)):
        v2idx[vList[i]] = i
    
    nextVal = 0
    for idx in range(len(vList), 29999999):
        if nextVal in v2idx:
            t = v2idx[nextVal]
            v2idx[nextVal] = idx
            nextVal = idx - t
        else:
            v2idx[nextVal] = idx
            nextVal = 0
    
    print nextVal


if __name__ == "__main__":
    work(read())
