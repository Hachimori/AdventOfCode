#!/usr/bin/env python

def read():
    board = []
    r = 0
    
    while 1:
        try:
            line = raw_input()
            if 'S' in line:
                sr, sc = r, line.index('S')
            if 'E' in line:
                gr, gc = r, line.index('E')
            board.append(list(line))
        except EOFError:
            break
        r += 1

    board[sr][sc] = 'a'
    board[gr][gc] = 'z'
        
    return board, sr, sc, gr, gc


def work((board, sr, sc, gr, gc)):
    row, col = len(board), len(board[0])
    
    Q = []
    cost = [[-1 for j in range(col)] for i in range(row)]

    Q.append((sr, sc))
    cost[sr][sc] = 0

    while Q:
        r, c = Q[0]
        del Q[0]

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < row and 0 <= nc < col):
                continue
            if cost[nr][nc] != -1:
                continue
            if ord(board[r][c]) >= ord(board[nr][nc]) - 1:
                cost[nr][nc] = cost[r][c] + 1
                Q.append((nr, nc))

    print cost[gr][gc]


if __name__ == "__main__":
    work(read())
