#!/usr/bin/env python

total = 0
while 1:
    try:
        v = input()
    except:
        break
    total += v / 3 - 2
print total
