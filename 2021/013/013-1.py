#!/usr/bin/env python

def read():
    xyList = []
    foldList = []

    while 1:
        s = raw_input()
        if not s: break
        xyList.append(map(int, s.split(',')))
    xyList = map(tuple, xyList)

    try:
        while 1:
            s = raw_input()
            fold, val = s.split('=')
            foldList.append((fold[-1], int(val)))
    except EOFError:
        pass

    return xyList, foldList


def work((xyList, foldList)):
    xySet = set(xyList)

    for (x, y) in xyList:
        foldAxis, foldValue = foldList[0]
        if foldAxis == 'x' and foldValue < x:
            xySet.add((foldValue - (x - foldValue), y))
            xySet.remove((x, y))
        elif foldAxis == 'y' and foldValue < y:
            xySet.add((x, foldValue - (y - foldValue)))
            xySet.remove((x, y))

    print len(xySet)


if __name__ == "__main__":
    work(read())
