#!/usr/bin/env python

import cmath
import math


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def calc(b):
    SR = 23
    SC = 17
    row = len(b)
    col = len(b[0])


    # drdcMap[(dr, dc)] = [min Distance from (SR, SC), target position]
    drdcMap = {}
    for r in range(row):
        for c in range(col):
            if r == SR and c == SC: continue
            if b[r][c] == '.': continue

            dr = r - SR
            dc = c - SC

            div = gcd(abs(dr), abs(dc))

            dr /= div
            dc /= div

            if (dr, dc) in drdcMap:
                cmpDistance = drdcMap[(dr, dc)][0]
                if cmpDistance > abs(r - SR) + abs(c - SC):
                    drdcMap[(dr, dc)][0] = abs(r - SR) + abs(c - SR)
                    drdcMap[(dr, dc)][1] = (r, c)
            else:
                drdcMap[(dr, dc)] = [abs(r - SR) + abs(c - SR), (r, c)]


    rcAngle = []
    for (_, (r, c)) in drdcMap.values():
        vec1 = complex(c - SC, r - SR)
        vec2 = complex(     0,     -1)
        angle = math.fmod(2 * cmath.pi + cmath.phase(vec1 / vec2), 2 * cmath.pi)
        rcAngle.append((r, c, angle))

    # sort by angle
    rcAngle.sort(key = lambda element: element[2])
    
    return rcAngle[199][1], rcAngle[199][0]


b = []
while 1:
    try:
        b.append(raw_input())
    except:
        break

print calc(b)
