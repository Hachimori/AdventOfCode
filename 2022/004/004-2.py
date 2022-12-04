#!/usr/bin/env python


def read():
    ret = []
    while 1:
        try:
            line = raw_input()
            a, b = line.split(',')
            aBgn, aEnd = map(int, a.split('-'))
            bBgn, bEnd = map(int, b.split('-'))
            ret.append((aBgn, aEnd, bBgn, bEnd))
        except EOFError:
            break
    return ret


def work(data):
    ans = 0
    for (aBgn, aEnd, bBgn, bEnd) in data:
        maxV = max(aBgn, bBgn)
        minV = min(aEnd, bEnd)
        ans += maxV <= minV
    print ans


if __name__ == "__main__":
    work(read())
