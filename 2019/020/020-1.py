#!/usr/bin/env python

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

b = []
portal = []
portal2rcList = {}


def read():
    del b[:]
    del portal[:]
    portal2rcList.clear()
    
    while 1:
        try:
            s = raw_input()
        except:
            break
        b.append(s)
    
    row = len(b)
    col = len(b[0])

    for r in range(row):
        portal.append(['' for c in range(col)])
    
    for r in range(row):
        for c in range(col):
            for direct in range(1, 3):
                s = ''
                for nMov in range(3):
                    nr = r + nMov * dr[direct]
                    nc = c + nMov * dc[direct]
                    if 0 <= nr < row and 0 <= nc < col:
                        s += b[nr][nc]
                
                if len(s) < 3: continue
                if (s[0] == '.' and s[1].isupper() and s[2].isupper()) or \
                  (s[0].isupper() and s[1].isupper() and s[2] == '.'):
                  
                    if s[0] == '.':
                        portalName = s[1:]
                        portalRC = r, c
                    else:
                        portalName = s[:2]
                        portalRC = r + 2 * dr[direct], c + 2 * dc[direct]
                  
                  
                    portal[r + dr[direct]][c + dc[direct]] = portalName
                    if portalName not in portal2rcList:
                        portal2rcList[portalName] = []
                    portal2rcList[portalName].append(portalRC)
                        
                    
def work():
    row = len(b)
    col = len(b[0])

    cost = [[-1 for c in range(col)] for r in range(row)]
    Q = []

    initRC = portal2rcList['AA'][0]
    cost[initRC[0]][initRC[1]] = 0
    Q.append(initRC)
    
    while Q:
        r, c = Q[0]
        del Q[0]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < row and 0 <= nc < col): continue
            
            if cost[nr][nc] != -1:
                continue

            if portal[nr][nc]:
                p = portal[nr][nc]
                if p == 'ZZ':
                    print cost[r][c]
                    return
                cost[nr][nc] = cost[r][c] + 1
                for nnr, nnc in portal2rcList[p]:
                    if cost[nnr][nnc] == -1:
                        cost[nnr][nnc] = cost[r][c] + 1
                        Q.append((nnr, nnc))
            elif b[nr][nc] == '.':
                cost[nr][nc] = cost[r][c] + 1
                Q.append((nr, nc))
            else:
                continue

    
read()
work()
