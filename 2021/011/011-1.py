#!/usr/bin/env python

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
    
    total = 0
    
    for _ in range(100):  
        for r in range(row):
            for c in range(col):
                v[r][c] += 1

        flashed = set()
        while 1:
            flashPos = []
            for r in range(row):
                for c in range(col):
                    if v[r][c] >= 10 and (r, c) not in flashed:
                        flashPos.append((r, c))
                        flashed.add((r, c))
            
            if not flashPos:
                break

            for (r, c) in flashPos:
                for (dr, dc) in zip((-1, -1, -1, 0, 1, 1, 1, 0), (-1, 0, 1, 1, 1, 0, -1, -1)):
                    nr = r + dr
                    nc = c + dc
                    if not (0 <= nr and nr < row and 0 <= nc and nc < col):
                        continue
                    v[nr][nc] += 1

        total += len(flashed)
        for (r, c) in flashed:
            v[r][c] = 0
        
        
    print total


if __name__ == "__main__":
    work(read())
