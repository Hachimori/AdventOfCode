#!/usr/bin/env python


def readXYZ():
    s = raw_input()
    for ch in '<=,>xyz':
        s = s.replace(ch, '')
    return map(int, s.split())


def read():
    ret = []
    for i in range(4):        
        ret.append(readXYZ())
    return ret


posXyz = read()
vecXyz = [[0, 0, 0] for i in range(len(posXyz))]

STEP = 1000
N = len(posXyz)
for step in range(STEP):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(3):
                if posXyz[i][k] < posXyz[j][k]: vecXyz[i][k] += 1
                if posXyz[i][k] > posXyz[j][k]: vecXyz[i][k] -= 1
    for i in range(N):
        for j in range(3):
            posXyz[i][j] += vecXyz[i][j]

ans = 0
for i in range(N):
    pot = sum(abs(p) for p in posXyz[i])
    kin = sum(abs(v) for v in vecXyz[i])
    ans += pot * kin

print ans
