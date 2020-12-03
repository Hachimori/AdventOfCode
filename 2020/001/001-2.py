#!/usr/bin/env python

vList = []

try:
    while 1:
        vList.append(int(raw_input()))
except EOFError:
    pass


vSet = set(vList)

for i in range(len(vList)):
    for j in range(i + 1, len(vList)):
        if 2020 - vList[i] - vList[j] in vSet:
            rem = 2020 - vList[i] - vList[j]
            print vList[i] * vList[j] * rem
