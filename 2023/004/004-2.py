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
    cntCard = [1 for _ in range(len(sList))]

    ans = 0
    for idx, s in enumerate(sList):
        numStr = s.split(':')[1]
        winNumStr, ownNumStr = numStr.split('|')
        winNum = map(int, winNumStr.split())
        ownNum = map(int, ownNumStr.split())

        cntMatch = sum([winNum.count(v) for v in ownNum])
        for i in range(idx + 1, idx + 1 + cntMatch):
            cntCard[i] += cntCard[idx]

    print sum(cntCard)


if __name__ == "__main__":
    work(read())
