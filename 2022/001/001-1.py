#!/usr/bin/env python

import sys


def read():
    txt = "".join(sys.stdin.readlines())
    sList = txt.split("\n\n")
    return [map(int, s.split()) for s in sList]
        


def work(data):
    maxV = 0
    for vList in data:
        maxV = max(maxV, sum(vList))
    print maxV
    


if __name__ == "__main__":
    work(read())
