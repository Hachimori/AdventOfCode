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

            candi = 1
            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                cnt = 0
                while 0 <= rr < row and 0 <= cc < col:
                    cnt += 1
                    if board[r][c] <= board[rr][cc]:
                        break
                    rr += dr[i]
                    cc += dc[i]
                candi *= cnt


            ans = max(ans, candi)

    print ans


if __name__ == "__main__":
    work(read())
