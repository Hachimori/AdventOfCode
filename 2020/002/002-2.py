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

    p1, p2 = map(int, minmax.split('-'))
    letter = letterColon[0]

    p1 -= 1
    p2 -= 1
    
    if (password[p1] == letter) + (password[p2] == letter) == 1:
        cnt += 1

print cnt
