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


def rec(avail, availLeng, mappingIdx, mappingList):
    if mappingIdx == len(mappingList):
        return avail

    minV = 10 ** 100
    for (dst, src, leng) in mappingList[mappingIdx]:
        if src + leng - 1 < avail:
            # src----src+leng
            #                  avail------avail+availLeng
            pass

        elif avail + availLeng - 1 < src:
            #                                                 src-----src+leng
            #                  avail------avail+availLeng
            pass

        else:
            # src--------------------src+leng
            #                  avail------avail+availLeng
            #
            # or,
            #
            #                      src--src+leng
            #                  avail------avail+availLeng
            #
            # or,
            #
            #                      src------------------------src+leng
            #                  avail------avail+availLeng
            # or,
            #
            # src---------------------------------------------src+leng
            #                  avail------avail+availLeng
            a = max(avail, src)
            l = min(src + leng, avail + availLeng) - a
            minV = min(minV, rec(dst + a - src, l, mappingIdx + 1, mappingList))

    return minV


def work((seeds, mappingList)):
    # Simplify mapping
    for mapping in mappingList:
        # Order by src
        mapping.sort(key=lambda x: x[1])

        toAdd = []
        current = 0
        for (_, src, leng) in mapping:
            if current < src:
                toAdd.append((current, current, src - current))
            current = src + leng
        mapping.extend(toAdd)
        mapping.append((current, current, 10 ** 100))

    ans = 10 ** 100
    for idx in range(len(seeds))[::2]:
        ans = min(ans, rec(seeds[idx], seeds[idx + 1], 0, mappingList))
    print ans


if __name__ == "__main__":
    work(read())
