#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            ret.append(raw_input())
        except EOFError:
            break
    return ret


def work(board):
    ans = 0
    row, col = len(board), len(board[0])

    for r in range(row):
        for c in range(col):
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            
            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                isVisible = True
                while 0 <= rr < row and 0 <= cc < col:
                    if board[r][c] <= board[rr][cc]:
                        isVisible = False
                        break
                    rr += dr[i]
                    cc += dc[i]
                if isVisible:
                    ans += 1
                    break

    print ans


if __name__ == "__main__":
    work(read())
