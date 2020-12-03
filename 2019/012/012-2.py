#!/usr/bin/env python


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


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
origXyz = [p[:] for p in posXyz]
vecXyz = [[0, 0, 0] for i in range(len(posXyz))]


N = len(posXyz)
cycle = []
for axis in range(3):
    step = 0
    while step == 0 or \
        not all(posXyz[i][axis] == origXyz[i][axis] for i in range(N)) or \
        not all(vecXyz[i][axis] == 0 for i in range(N)):
        step += 1
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if posXyz[i][axis] < posXyz[j][axis]: vecXyz[i][axis] += 1
                if posXyz[i][axis] > posXyz[j][axis]: vecXyz[i][axis] -= 1
        for i in range(N):
            posXyz[i][axis] += vecXyz[i][axis]
    cycle.append(step)


ans = cycle[0]
for i in range(1, 3):
    ans = lcm(ans, cycle[i])
print ans
