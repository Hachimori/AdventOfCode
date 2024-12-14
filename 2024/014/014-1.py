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


def work(row, col, posList, vecList):
    newPosList = []

    n = len(posList)
    for i in range(n):
        x = posList[i][0] + vecList[i][0] * 100
        y = posList[i][1] + vecList[i][1] * 100
        newPosList.append([x % col, y % row])

    cnt = [[0 for j in range(2)] for i in range(2)]
    for i in range(n):
        x, y = newPosList[i]
        if x == col // 2 or y == row // 2:
            continue
        cnt[x > col // 2][y > row // 2] += 1

    print(cnt[0][0] * cnt[0][1] * cnt[1][0] * cnt[1][1])


if __name__ == "__main__":
    work(*read())
