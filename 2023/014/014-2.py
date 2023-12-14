#!/usr/bin/env python

def read():
    ch = []
    try:
        while 1:
            ch.append(list(raw_input()))
    except EOFError:
        pass
    return ch


def move(orig):
    row = len(orig)
    col = len(orig[0])

    ret = [[orig[r][c] for c in range(col)] for r in range(row)]

    for c in range(col):
        for r in range(row):
            if ret[r][c] == 'O':
                rr = r
                while rr - 1 >= 0 and ret[rr - 1][c] == '.':
                    ret[rr][c], ret[rr - 1][c] = ret[rr - 1][c], ret[rr][c]
                    rr -= 1

    return ret


def rotate(orig):
    row = len(orig)
    col = len(orig[0])

    ret = [['' for r in range(row)] for c in range(col)]

    for r in range(row):
        for c in range(col):
            ret[c][row - 1 - r] = orig[r][c]

    return ret


def calc(ch):
    row = len(ch)
    col = len(ch[0])

    ret = 0
    for r in range(row):
        for c in range(col):
            if ch[r][c] == 'O':
                ret += row - r
    return ret


def tuplize(ch):
    return tuple(tuple(ch[r]) for r in range(len(ch)))


def work(ch):
    visited = {}
    totalLen = 1000000000
    for curCycle in xrange(totalLen):
        if tuplize(ch) in visited:
            remain = totalLen - curCycle
            cycleLen = curCycle - visited[tuplize(ch)] + 1
            remain %= cycleLen

            for i in range(remain):
                for j in range(4):
                    ch = move(ch)
                    ch = rotate(ch)
            break

        visited[tuplize(ch)] = curCycle

        for loop in range(4):
            ch = move(ch)
            ch = rotate(ch)

    print calc(ch)


if __name__ == "__main__":
    work(read())