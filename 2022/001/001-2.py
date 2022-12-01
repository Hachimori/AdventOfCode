#!/usr/bin/env python

import sys


def read():
    txt = "".join(sys.stdin.readlines())
    sList = txt.split("\n\n")
    return [map(int, s.split()) for s in sList]
        


def work(data):
    sumList = []
    for vList in data:
        sumList.append(sum(vList))
    print sum(sorted(sumList)[-3::])
    


if __name__ == "__main__":
    work(read())
