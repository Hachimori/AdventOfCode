#!/usr/bin/env python

def read():
    caseList = []
    try:
        while 1:
            caseList.append(map(int, raw_input().split()))
    except EOFError:
        pass
    return caseList


def calc(vList):
    if vList.count(0) == len(vList):
        return 0
    else:
        next = []
        for i in range(len(vList) - 1):
            next.append(vList[i + 1] - vList[i])
        return calc(next) + vList[-1]


def work((caseList)):
    ans = 0
    for vList in caseList:
        ans += calc(vList)
    print ans


if __name__ == "__main__":
    work(read())
