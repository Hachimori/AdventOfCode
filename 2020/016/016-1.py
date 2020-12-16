#!/usr/bin/env python

import re


def read():
    rangeList = []
    while 1:
        line = raw_input()
        if not line:
            break
        
        mList = [m for m in re.finditer(r"(\d+)-(\d+)", line)]

        for m in mList:
            rangeList.append((int(m.group(1)), int(m.group(2))))

    raw_input()
    myVList = map(int, raw_input().split(','))
    raw_input()

    oppVList = []
    raw_input()
    while 1:
        line = raw_input()
        if not line:
            break
        oppVList.extend(map(int, line.split(',')))
        
    return rangeList, myVList, oppVList


def work((rangeList, myVList, oppVList)):
    total = 0
    for v in sum([myVList, oppVList], []):
        if all(not (bgn <= v <= end) for (bgn, end) in rangeList):
            total += v
    print total


if __name__ == "__main__":
    work(read())
