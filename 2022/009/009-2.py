#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            ch, v = raw_input().split()
            ret.append((ch, int(v)))
        except EOFError:
            break
    return ret


def work(data):
    visited = set([(0, 0)])
    rList = [0 for i in range(10)]
    cList = [0 for i in range(10)]
    
    for (ch, v) in data:
        dr, dc = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}[ch]

        for i in range(v):
            rList[0] += dr
            cList[0] += dc

            for j in range(1, 10):
                if abs(rList[j] - rList[j - 1]) == 2 or abs(cList[j] - cList[j - 1]) == 2:
                    if rList[j] != rList[j - 1]:
                        rList[j] += +1 if rList[j] < rList[j - 1] else -1
                    if cList[j] != cList[j - 1]:
                        cList[j] += +1 if cList[j] < cList[j - 1] else -1

            visited.add((rList[-1], cList[-1]))
            
    print len(visited)


if __name__ == "__main__":
    work(read())
