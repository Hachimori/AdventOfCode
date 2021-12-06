#!/usr/bin/env python

def read():
    return map(int, raw_input().split(','))


def work(vList):
    v2cnt = [0 for _ in range(9)]

    for v in vList:
        v2cnt[v] += 1

    for day in range(256):
        nextV2cnt = [0 for _ in range(9)]
        for i in range(9):
            if i == 0:
                nextV2cnt[8] += v2cnt[0]
                nextV2cnt[6] += v2cnt[0]
            else:
                nextV2cnt[i - 1] += v2cnt[i]
        v2cnt = nextV2cnt
    
    print sum(v2cnt)


if __name__ == "__main__":
    work(read())
