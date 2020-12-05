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
    maxV = 0
    for s in sList:
        value = 0
        for ch in s:
            value <<= 1
            if ch == 'B' or ch == 'R':
                value += 1
        maxV = max(maxV, value)
    print maxV


if __name__ == "__main__":
    work(read())
