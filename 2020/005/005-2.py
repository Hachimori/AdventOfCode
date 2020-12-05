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
    isTaken = [False for _ in range(1 << 10)]
    for s in sList:
        value = 0
        for ch in s:
            value <<= 1
            if ch == 'B' or ch == 'R':
                value += 1
        isTaken[value] = True

    for v in range(1, (1 << 10) - 1):
        if isTaken[v - 1] and not isTaken[v] and isTaken[v + 1]:
            print v


if __name__ == "__main__":
    work(read())
