#!/usr/bin/env python


def read():
    h = []

    try:
        while 1:
            h.append(map(int, raw_input()))
    except EOFError:
        pass
    
    return h


def work(h):
    row = len(h)
    col = len(h[0])
    
    totalList = []
    
    visited = [[False for j in range(col)] for i in range(row)]
    for initR in range(row):
        for initC in range(col):
            if h[initR][initC] == 9: continue
            if visited[initR][initC]: continue
            
            total = 0
            
            Q = [(initR, initC)]
            visited[initR][initC] = True

            while Q:
                r, c = Q[0]
                del Q[0]

                total += 1
                
                dr = [-1, 0, 1, 0]
                dc = [0, 1, 0, -1]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (0 <= nr < row and 0 <= nc < col): continue
                    if h[nr][nc] == 9: continue
                    if visited[nr][nc]: continue
                    
                    Q.append((nr, nc))
                    visited[nr][nc] = True

            totalList.append(total)

    
    totalList.sort()
    print totalList[-1] * totalList[-2] * totalList[-3]


if __name__ == "__main__":
    work(read())
