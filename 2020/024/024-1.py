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
    xy2cnt = {}

    for s in sList:
        x, y = 0, 0

        dirList = ["e", "se", "sw", "w", "nw", "ne"]
        dxList = [1, 0, -1, -1, 0, 1]
        dyList = [0, -1, -1, 0, 1, 1]
        
        while s:
            for i in range(len(dirList)):
                if s.startswith(dirList[i]):
                    x += dxList[i]
                    y += dyList[i]
                    s = s[len(dirList[i]):]
                    break

        if (x, y) not in xy2cnt:
            xy2cnt[(x, y)] = 0
        xy2cnt[(x, y)] += 1

    print sum(cnt % 2 == 1 for cnt in xy2cnt.values())
    for ((x, y), cnt) in xy2cnt.items():
        if cnt % 2 == 1:
            print x, y

if __name__ == "__main__":
    work(read())
