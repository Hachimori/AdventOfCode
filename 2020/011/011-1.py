#!/usr/bin/env python

def read():
    board = []
    try:
        while 1:
            board.append(list(raw_input()))
    except EOFError:
        pass
    return board


def work(board):
    while 1:
        updated = False
        nextBoard = []
        
        for r in range(len(board)):
            nextBoard.append([])
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    nextBoard[r].append('.')
                    continue
                
                dr = [-1, -1, -1, 0, 1, 1, 1, 0]
                dc = [-1, 0, 1, 1, 1, 0, -1, -1]

                cntOccupied = 0
                for i in range(len(dr)):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < len(board) and 0 <= nc < len(board[r]):
                        cntOccupied += board[nr][nc] == '#'

                if board[r][c] == 'L':
                    nextBoard[r].append('#' if cntOccupied == 0 else 'L')
                else:
                    nextBoard[r].append('L' if cntOccupied >= 4 else '#')

        if nextBoard == board:
            break
        
        board = nextBoard

    
    print sum([ch == '#' for ch in sum(board, [])])
        
        
if __name__ == "__main__":
    work(read())
