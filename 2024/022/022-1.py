#!/usr/bin/env python3

def read():
    vList = []
    while True:
        try:
            vList.append(int(input()))
        except EOFError:
            break
    return vList


def calc(v):
    MOD = 16777216
    LOOP = 2000
    for i in range(LOOP):
        v = ((v * 64) ^ v) % MOD
        v = ((v // 32) ^ v) % MOD
        v = ((v * 2048) ^ v) % MOD
    return v


def work(vList):
    ans = 0
    for v in vList:
        ans += calc(v)
    print(ans)


if __name__ == "__main__":
    work(read())
