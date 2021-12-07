#!/usr/bin/env python

def read():
    return map(int, raw_input().split(','))


def work(vList):
    vList.sort()

    ans = 0
    for v in vList:
        ans += abs(v - vList[len(vList) / 2])
        
    print ans


if __name__ == "__main__":
    work(read())
