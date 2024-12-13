#!/usr/bin/env python3

def read():
    caseList = []

    while True:
        def filter(ch):
            return ch if ch.isdigit() else ' '

        def converter(line):
            return ''.join(map(filter, line))

        try:
            vList1 = list(map(int, converter(input()).split()))
            vList2 = list(map(int, converter(input()).split()))
            vList3 = list(map(int, converter(input()).split()))
            caseList.append((vList1, vList2, vList3))
            input()
        except EOFError:
            break

    return caseList


def calc(axy, bxy, gxy):
    ax, ay = axy
    bx, by = bxy
    gx, gy = gxy

    isOk = False
    minV = 1e10
    na = 0
    while True:
        remainX = gx - na * ax
        remainY = gy - na * ay

        if remainX % bx == 0 and remainY % by == 0 and remainX // bx == remainY // by:
            nb = remainX // bx
            minV = min(minV, na * 3 + nb)
            isOk = True

        if na * ax > gx or na * ay > gy:
            break

        na += 1

    return minV if isOk else 0


def work(caseList):
    ans = 0
    for case in caseList:
        ans += calc(*case)
    print(ans)


if __name__ == "__main__":
    work(read())
