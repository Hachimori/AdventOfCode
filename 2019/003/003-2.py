#!/usr/bin/env python


# Returns (mul, (dr, dc))
def getMulDRC(s):
    # URDL
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    mul = int(s[1:])
    
    if s[0] == 'U': d = 0
    if s[0] == 'R': d = 1
    if s[0] == 'D': d = 2
    if s[0] == 'L': d = 3
    return mul, (dr[d], dc[d])


seq1 = raw_input().split(',')
seq2 = raw_input().split(',')

pt2step = {}
(r, c, step) = (0, 0, 0)
for dirVal in seq1:
    mul, (dr, dc) = getMulDRC(dirVal)
    for i in range(mul):
        r += dr
        c += dc
        step += 1
        if (r, c) not in pt2step:
            pt2step[(r, c)] = step

ans = 1 << 30
(r, c, step) = (0, 0, 0)
for dirVal in seq2:
    mul, (dr, dc) = getMulDRC(dirVal)
    for i in range(mul):
        r += dr
        c += dc
        step += 1
        if (r, c) in pt2step:
            ans = min(ans, pt2step[(r, c)] + step)

print ans
