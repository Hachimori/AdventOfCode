#!/usr/bin/env python3

def read():
    vList = []
    while True:
        try:
            vList.append(int(input()))
        except EOFError:
            break
    return vList


def calc(v, seq2total):
    seq2v = {}
    seq = []
    MOD = 16777216
    LOOP = 2000

    pre = -1000
    for i in range(LOOP):
        v = ((v * 64) ^ v) % MOD
        v = ((v // 32) ^ v) % MOD
        v = ((v * 2048) ^ v) % MOD
        diff = v % 10 - pre

        seq.append(diff)

        if len(seq) == 5:
            seq = seq[1:]

        if i >= 4 and tuple(seq) not in seq2v:
            seq2v[tuple(seq)] = v % 10

        pre = v % 10

    for [seq, v] in seq2v.items():
        if tuple(seq) not in seq2total:
            seq2total[tuple(seq)] = 0
        seq2total[tuple(seq)] += v



def work(vList):
    seq2total = {}
    for v in vList:
        calc(v, seq2total)

    maxV = 0
    for [seq, total] in seq2total.items():
        maxV = max(maxV, total)
    print(maxV)


if __name__ == "__main__":
    work(read())
