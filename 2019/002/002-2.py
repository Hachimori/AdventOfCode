#!/usr/bin/env python

def calc(vList):
    for i in range(0, len(vList), 4):
        a, b, c, d = vList[i], vList[i + 1], vList[i + 2], vList[i + 3]

        if a not in [1, 2, 99]:
            print a, b, c, d
            print "???"
            break

        if a == 1:
            vList[d] = vList[b] + vList[c]
        elif a == 2:
            vList[d] = vList[b] * vList[c]
        else:
            break
        vList[i + 0] += 4
    return vList[0]



vList = map(int, raw_input().split(','))

for i in range(0, 100):
    for j in range(0, 100):
        vList[1] = i
        vList[2] = j
        copied = vList[:]
        if calc(copied) == 19690720:
            print i, j


