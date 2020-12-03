#!/usr/bin/env python

total = 0
while 1:
    try:
        v = input()
    except:
        break
    while v / 3 - 2 >= 0:
        total += v / 3 - 2
        v = v / 3 - 2
print total
