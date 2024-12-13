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
    gx += 10000000000000
    gy += 10000000000000

    # ax * na + bx * nb = gx ... (1)
    # ay * na + by * nb = gy ... (2)

    # (1) * by - (2) * bx
    # => ax * by * na - ay * bx * na = gx * by - gy * bx
    # => na = (gx * by - gy * bx) / (ax * by - ay * bx)

    if ax * by - ay * bx == 0:
        return 0

    if (gx * by - gy * bx) % (ax * by - ay * bx) != 0:
        return 0

    na = (gx * by - gy * bx) // (ax * by - ay * bx)
    if na < 0:
        return 0

    # ax * na + bx * nb = gx ... (1)
    # => nb = (gx - ax * na) / bx

    if (gx - ax * na) % bx != 0:
        return 0

    nb = (gx - ax * na) // bx

    if nb < 0:
        return 0

    return 3 * na + nb


def work(caseList):
    ans = 0
    for case in caseList:
        ans += calc(*case)
    print(ans)


if __name__ == "__main__":
    work(read())
