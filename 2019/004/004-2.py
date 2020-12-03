#!/usr/bin/env python

"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; 
  they only ever increase or stay the same (like 111123 or 135679).
The two adjacent matching digits are not part of a larger group of 
  matching digits.
"""


def isOk(v):
    vStr = str(v)
    
    if len(vStr) != 6: return False

    for i in range(len(vStr) - 1):
        if vStr[i] > vStr[i + 1]:
            return False
        
    idx = 0
    while idx < len(vStr):
        cur = idx
        while cur < len(vStr) and vStr[idx] == vStr[cur]:
            cur += 1
        if cur - idx == 2:
            return True
        idx = cur
    return False
    

cnt = 0
for v in range(245182, 790572 + 1):
    if isOk(v):
        cnt += 1
print cnt
