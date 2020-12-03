#!/usr/bin/env python

"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; 
  they only ever increase or stay the same (like 111123 or 135679).
"""


def isOk(v):
    vStr = str(v)
    
    if len(vStr) != 6: return False

    hasSameAdj = False
    for i in range(len(vStr) - 1):
        if vStr[i] == vStr[i + 1]:
            hasSameAdj = True
        if vStr[i] > vStr[i + 1]:
            return False
        
    return hasSameAdj
    

cnt = 0
for v in range(245182, 790572 + 1):
    if isOk(v):
        cnt += 1
print cnt
