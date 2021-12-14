#!/usr/bin/env python

def read():
    init = raw_input()
    raw_input()

    ruleList = []
    try:
        while 1:
            pair, toInsert = raw_input().split(' -> ')
            ruleList.append((pair, toInsert))
    except EOFError:
        pass

    return init, ruleList


def work((init, ruleList)):
    pair2generatedPairs = {}
    for (pair, toInsert) in ruleList:
        pair2generatedPairs[pair] = (pair[0] + toInsert, toInsert + pair[1])

    pair2cnt = {}
    for i in range(len(init) - 1):
        pair = init[i : i + 2]
        if pair not in pair2cnt:
            pair2cnt[pair] = 0
        pair2cnt[pair] += 1

    for _ in range(10):
        nexPair2cnt = {}
        for (pair, cnt) in pair2cnt.items():
            for generatedPair in pair2generatedPairs[pair]:
                if generatedPair not in nexPair2cnt:
                    nexPair2cnt[generatedPair] = 0
                nexPair2cnt[generatedPair] += cnt
        pair2cnt = nexPair2cnt

    ch2cnt = {}
    for (pair, cnt) in pair2cnt.items():
        if pair[0] not in ch2cnt:
            ch2cnt[pair[0]] = 0
        ch2cnt[pair[0]] += cnt

    ch2cnt[init[-1]] += 1
        
    print max(ch2cnt.values()) - min(ch2cnt.values())


if __name__ == "__main__":
    work(read())
