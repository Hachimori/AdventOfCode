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
    ans = 0
    
    for r in range(len(h)):
        for c in range(len(h[0])):
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            
            cntOK = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < len(h) and 0 <= nc < len(h[0])) or \
                  h[r][c] < h[nr][nc]:
                    cntOK += 1
                    
            if cntOK == 4:
                ans += h[r][c] + 1
    
    print ans


if __name__ == "__main__":
    work(read())
