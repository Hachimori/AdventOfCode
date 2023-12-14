#!/usr/bin/env python

def read():
    ch = []
    try:
        while 1:
            ch.append(list(raw_input()))
    except EOFError:
        pass
    return ch


def work(ch):
    row = len(ch)
    col = len(ch[0])

    for c in range(col):
        for r in range(row):
            if ch[r][c] == 'O':
                rr = r
                while rr - 1 >= 0 and ch[rr - 1][c] == '.':
                    ch[rr][c], ch[rr - 1][c] = ch[rr - 1][c], ch[rr][c]
                    rr -= 1

    ans = 0
    for r in range(row):
        for c in range(col):
            if ch[r][c] == 'O':
                ans += row - r
    print ans


if __name__ == "__main__":
    work(read())
