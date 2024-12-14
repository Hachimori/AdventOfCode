#!/usr/bin/env python3

def read():
    # For tmp
    # row, col = 7, 11

    # For input.txt
    row, col = 103, 101

    posList = []
    vecList = []
    while 1:
        def filterNonDigits(line):
            return ''.join([ch if ch.isdigit() or ch == '-' else ' ' for ch in line])

        def getIntList(line):
            return list(map(int, filterNonDigits(line).split()))

        try:
            line = input()
            intList = getIntList(line)
            posList.append(intList[:2])
            vecList.append(intList[2:])
        except EOFError:
            break

    return row, col, posList, vecList


def plot(row, col, posList, vecList, step):
    ch = [['.' for c in range(col)] for r in range(row)]

    n = len(posList)
    for i in range(n):
        x = posList[i][0] + vecList[i][0] * step
        y = posList[i][1] + vecList[i][1] * step
        ch[y % row][x % col] = '*'

    return ch


def dfs(r, c, visited, row, col, ch):
    ret = 1

    visited[r][c] = True

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < row and 0 <= nc < col):
            continue
        if ch[nr][nc] == '.':
            continue
        if visited[nr][nc]:
            continue
        ret += dfs(nr, nc, visited, row, col, ch)

    return ret


def check(row, col, ch, step):
    visited = [[False for c in range(col)] for r in range(row)]

    for r in range(row):
        for c in range(col):
            if ch[r][c] == '.':
                continue
            if visited[r][c]:
                continue

            if dfs(r, c, visited, row, col, ch) >= 20:
                print('t = %d' % step)
                for i in range(row):
                    print(''.join(ch[i]))
                return


def work(row, col, posList, vecList):
    N_STEP = 10000
    for i in range(N_STEP):
        ch = plot(row, col, posList, vecList, i)
        check(row, col, ch, i)


if __name__ == "__main__":
    work(*read())
