#!/usr/bin/env python

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def calc(b):
    row = len(b)
    col = len(b[0])

    ans = 0
    for r in range(row):
        for c in range(col):
            if b[r][c] == '.': continue

            drdcSet = set([])
            for rr in range(row):
                for cc in range(col):
                    if rr == r and cc == c: continue
                    if b[rr][cc] == '.': continue

                    dr = r - rr
                    dc = c - cc

                    div = gcd(abs(dr), abs(dc))

                    dr /= div
                    dc /= div

                    drdcSet.add((dr, dc))
            if ans < len(drdcSet):
                ans = len(drdcSet)
                ansPos = (r, c)
    return ans, ansPos

b = []
while 1:
    try:
        b.append(raw_input())
    except:
        break

print calc(b)
