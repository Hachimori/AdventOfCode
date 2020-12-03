#!/usr/bin/env python

sList = []

try:
    while 1:
        sList.append(raw_input())
except EOFError:
    pass

cnt = 0
for s in sList:
    minmax, letterColon, password = s.split()

    minV, maxV = map(int, minmax.split('-'))
    letter = letterColon[0]

    if minV <= password.count(letter) <= maxV:
        cnt += 1

print cnt
