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
    ans = 0
    for s in sList:
        numStr = s.split(':')[1]
        winNumStr, ownNumStr = numStr.split('|')
        winNum = map(int, winNumStr.split())
        ownNum = map(int, ownNumStr.split())

        cnt = sum([winNum.count(v) for v in ownNum])
        if cnt:
            ans += 2 ** (cnt - 1)

    print ans


if __name__ == "__main__":
    work(read())
