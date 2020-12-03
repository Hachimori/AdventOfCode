#!/usr/bin/env python

b = []
while 1:
    try:
        s = raw_input()
    except:
        break
    b.append(s)

dr = [-1, 0, 1, 0, 0]
dc = [0, 1, 0, -1, 0]

ans = 0
for r in range(len(b)):
    for c in range(len(b[0])):
        cnt = 0
        for i in range(5):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < len(b) and 0 <= nc < len(b[0]) and b[nr][nc] == '#':
                cnt += 1
        if cnt == 5:
            ans += r * c
print ans
