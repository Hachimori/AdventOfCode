#!/usr/bin/env python

import heapq


class QData:
    def __init__(self, r, c, dIdx, nConsec, cost):
        self.r = r
        self.c = c
        self.dIdx = dIdx
        self.nConsec = nConsec
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def read():
    v = []
    try:
        while 1:
            v.append(map(int, list(raw_input())))
    except EOFError:
        pass
    return v


def dijkstra(v):
    row = len(v)
    col = len(v[0])

    Q = []
    visited = {}

    heapq.heappush(Q, QData(0, 0, -1, 4, 0))
    visited[(0, 0, -1, 4)] = 0

    while Q:
        cur = heapq.heappop(Q)

        if visited[(cur.r, cur.c, cur.dIdx, cur.nConsec)] < cur.cost:
            continue

        if cur.r == row - 1 and cur.c == col - 1:
            return cur.cost

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for nexDIdx in range(4):
            if cur.dIdx != nexDIdx and cur.nConsec < 4:
                continue
            if cur.dIdx == nexDIdx and cur.nConsec == 10:
                continue
            if cur.dIdx == (nexDIdx + 2) % 4:
                continue

            nr = cur.r + dr[nexDIdx]
            nc = cur.c + dc[nexDIdx]

            if not (0 <= nr < row and 0 <= nc < col):
                continue

            dIdx = nexDIdx
            nConsec = 1 if cur.dIdx != nexDIdx else cur.nConsec + 1
            cost = cur.cost + v[nr][nc]
            if (nr, nc, dIdx, nConsec) in visited and visited[(nr, nc, dIdx, nConsec)] <= cost:
                continue

            visited[((nr, nc, dIdx, nConsec))] = cost
            heapq.heappush(Q, QData(nr, nc, dIdx, nConsec, cost))

    return -1


def work(v):
    print dijkstra(v)


if __name__ == "__main__":
    work(read())
