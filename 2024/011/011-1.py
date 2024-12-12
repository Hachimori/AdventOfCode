#!/usr/bin/env python3

def read():
    return list(map(int, input().split()))


def work(vList):
    for loop in range(25):
        nex = []
        for v in vList:
            if v == 0:
                nex.append(1)
            elif len(str(v)) % 2 == 0:
                leng = len(str(v))
                nex.append(int(str(v)[:leng//2]))
                nex.append(int(str(v)[leng//2:]))
            else:
                nex.append(v * 2024)
        vList = nex

    print(len(vList))


if __name__ == "__main__":
    work(read())
