#!/usr/bin/env python

vList = []

try:
    while 1:
        vList.append(int(raw_input()))
except EOFError:
    pass

for i in range(len(vList)):
    for j in range(i + 1, len(vList)):
        if vList[i] + vList[j] == 2020:
            print vList[i] * vList[j]
