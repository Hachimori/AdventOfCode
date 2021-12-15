#!/usr/bin/env python

import heapq


INF = 1 << 30

def read():
    v = []

    try:
        while 1:
            v.append(map(int, list(raw_input())))
    except EOFError:
        pass

    return v



def work(v):
    row = len(v)
    col = len(v[0])

    Q = []
    cost = [[INF for j in range(col)] for i in range(row)]
    
    heapq.heappush(Q, (0, 0, 0))
    cost[0][0] = 0

    while Q:
        curCost, r, c = heapq.heappop(Q)

        if cost[r][c] < curCost: continue

        if r == row - 1 and c == col - 1:
            print curCost
            break
        
        for (dr, dc) in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < row and 0 <= nc < col and cost[nr][nc] > curCost + v[nr][nc]:
                cost[nr][nc] = curCost + v[nr][nc]
                heapq.heappush(Q, (cost[nr][nc], nr, nc))


if __name__ == "__main__":
    work(read())
