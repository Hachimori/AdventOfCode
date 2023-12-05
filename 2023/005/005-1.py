#!/usr/bin/env python

def read():
    seeds = map(int, raw_input().split(':')[1].split())
    raw_input()

    mappingList = []
    try:
        while 1:
            raw_input()
            mapping = []
            while 1:
                line = raw_input()
                if len(line) == 0:
                    break
                dst, src, leng = map(int, line.split())
                mapping.append((dst, src, leng))
            mappingList.append(mapping)
    except EOFError:
        pass

    return seeds, mappingList


def rec(curr, mappingIdx, mappingList):
    if mappingIdx == len(mappingList):
        return curr

    for (dst, src, leng) in mappingList[mappingIdx]:
        if src <= curr < src + leng:
            return rec(dst + curr - src, mappingIdx + 1, mappingList)

    return rec(curr, mappingIdx + 1, mappingList)


def work((seeds, mappingList)):
    ans = 10 ** 100
    for seed in seeds:
        ans = min(ans, rec(seed, 0, mappingList))
    print ans


if __name__ == "__main__":
    work(read())
