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

    Q.append((gr, gc))
    cost[gr][gc] = 0

    while Q:
        r, c = Q[0]
        del Q[0]

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            pr = r + dr[i]
            pc = c + dc[i]
            if not (0 <= pr < row and 0 <= pc < col):
                continue
            if cost[pr][pc] != -1:
                continue
            if ord(board[pr][pc]) >= ord(board[r][c]) - 1:
                cost[pr][pc] = cost[r][c] + 1
                Q.append((pr, pc))

    minV = 10 ** 10
    for r in range(row):
        for c in range(col):
            if board[r][c] == 'a' and cost[r][c] != -1:
                minV = min(minV, cost[r][c])
    print minV


if __name__ == "__main__":
    work(read())
