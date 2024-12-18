#!/usr/bin/env python3

def read():
    dummy = int(input().split()[2])
    dummy = int(input().split()[2])
    dummy = int(input().split()[2])
    input()
    vList = list(map(int, input().split()[1].split(",")))
    return vList


def rec(ans, idx, vList):
    if idx < 0:
        print(ans)
        return True

    for bCandi in range(8):
        B = bCandi
        B ^= 5
        C = ((ans * 8 + bCandi) >> B) % 8
        B ^= 6
        if B ^ C == vList[idx] and rec(ans * 8 + bCandi, idx - 1, vList):
            return True

    return False


def work(vList):
    rec(0, len(vList) - 1, vList)


if __name__ == "__main__":
    work(read())
