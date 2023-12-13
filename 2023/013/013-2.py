#!/usr/bin/env python

def read():
    boardList = []
    try:
        while 1:
            board = []
            while 1:
                line = raw_input()
                if not line:
                    break
                board.append(list(line))
            boardList.append(board)
    except EOFError:
        pass
    return boardList


def rotate(board):
    row = len(board)
    col = len(board[0])
    ret = [['' for r in range(row)] for c in range(col)]
    for r in range(row):
        for c in range(col):
            ret[c][row - 1 - r] = board[r][c]
    return ret


def calcStep2(board, origLine):
    row = len(board)
    for r in range(row - 1):
        if r + 1 == origLine:
            continue
        isOk = True
        idx = 0
        while 0 <= r - idx and r + 1 + idx < row:
            if board[r - idx] != board[r + 1 + idx]:
                isOk = False
            idx += 1
        if isOk:
            return r + 1
    return 0


def calcStep1(board, origLine):
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] = '.' if board[r][c] == '#' else '#'
            t = calcStep2(board, origLine)
            board[r][c] = '.' if board[r][c] == '#' else '#'
            if t:
                return t
    return 0


def work(boardList):
    ans = 0
    for board in boardList:
        origLine = calcStep2(board, -1)
        t = calcStep1(board, origLine)
        if t:
            ans += 100 * t
        else:
            board = rotate(board)
            origLine = calcStep2(board, -1)
            ans += calcStep1(board, origLine)
    print ans


if __name__ == "__main__":
    work(read())
