#!/usr/bin/env python

"""
Environment:
  - MacBook Pro
  - 2.6 GHz 6core Intel Core i7
  - 16 GB 2400 MHz DDR4


Run result:
$ time ./012-1.py < input
7221

real	0m31.833s
user	0m31.722s
sys	0m0.061s
"""


def read():
    caseList = []
    try:
        while 1:
            line = raw_input()
            ch, vListStr = line.split()
            vList = map(int, vListStr.split(','))
            caseList.append((ch, vList))
    except EOFError:
        pass
    return caseList


def convertUnknown(ch, mask):
    ret = ''
    cntUnknown = 0
    for c in ch:
        if c == '?':
            ret += '#' if mask & (1 << cntUnknown) else '.'
            cntUnknown += 1
        else:
            ret += c
    return ret


def isOk(ch, mask, vList):
    curVList = []
    idx = 0
    while idx < len(ch):
        nex = idx
        while nex < len(ch) and ch[nex] == '#':
            nex += 1
        if nex != idx:
            curVList.append(nex - idx)
        idx = nex + 1
    return curVList == vList


def calc(ch, vList):
    nUnknown = ch.count('?')
    ret = 0
    for mask in range(1 << nUnknown):
        newCh = convertUnknown(ch, mask)
        ret += isOk(newCh, mask, vList)
    return ret


def work(caseList):
    ans = 0
    for (ch, vList) in caseList:
        ans += calc(ch, vList)
    print ans


if __name__ == "__main__":
    work(read())
