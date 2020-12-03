#!/usr/bin/env python

vList = map(int, raw_input().split(','))
vList[1] = 12
vList[2] = 2

for i in range(0, len(vList), 4):
    a, b, c, d = vList[i], vList[i + 1], vList[i + 2], vList[i + 3]

    print a, b, c, d
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
print vList[0]
