#!/usr/bin/env python

b = []
while 1:
    try:
        s = raw_input()
    except:
        break
    b.append(s)

for r in range(len(b)):
    for c in range(len(b[r])):
        if b[r][c] == 'S':
            startR, startC = r, c
        elif b[r][c] == 'o':
            goalR, goalC = r, c

cost = {(startR, startC): 0}
Q = [(startR, startC)]

while Q:
    currR, currC = Q[0]
    del Q[0]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nextR, nextC = currR + dr[i], currC + dc[i]
        if b[nextR][nextC] == '#':
            continue
        if (nextR, nextC) in cost:
            continue
        cost[(nextR, nextC)] = cost[(currR, currC)] + 1
        Q.append((nextR, nextC))

print cost[(goalR, goalC)]
