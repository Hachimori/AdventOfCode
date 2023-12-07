#!/usr/bin/env python

def read():
    handBidList = []
    try:
        while 1:
            elements = raw_input().split()
            handBidList.append((elements[0], int(elements[1])))
    except EOFError:
        pass
    return handBidList


def vList2score(vList):
    ret = 0
    for v in vList:
        ret = ret * 20 + v
    return ret


def calcWithJvalue(hand, jValue):
    VALUE_COUNT = len("#J23456789TQKA")

    # convert to value
    vList = []
    toCmpVList = []
    for ch in hand:
        if ch == 'J':
            vList.append(jValue)
        else:
            vList.append("#J23456789TQKA".index(ch))
        toCmpVList.append("#J23456789TQKA".index(ch))

    # Five of a kind
    for v in range(VALUE_COUNT):
        if vList.count(v) == 5:
            return 20**15 + vList2score(toCmpVList)

    # Four of a kind
    for v1 in range(VALUE_COUNT):
        for v2 in range(VALUE_COUNT):
            if vList.count(v1) == 4 and vList.count(v2) == 1:
                return 20**14 + vList2score(toCmpVList)

    # Full house
    for v1 in range(VALUE_COUNT):
        for v2 in range(VALUE_COUNT):
            if vList.count(v1) == 3 and vList.count(v2) == 2:
                return 20**13 + vList2score(toCmpVList)

    # Three of a kind
    for v in range(VALUE_COUNT):
        if vList.count(v) == 3:
            return 20 ** 12 + vList2score(toCmpVList)

    # Two pair
    for v1 in range(VALUE_COUNT):
        for v2 in range(v1 + 1, VALUE_COUNT):
            if vList.count(v1) == 2 and vList.count(v2) == 2:
                return 20 ** 11 + vList2score(toCmpVList)

    # One pair
    for v in range(VALUE_COUNT):
        if vList.count(v) == 2:
            return 20 ** 10 + vList2score(toCmpVList)

    # High card
    return vList2score(toCmpVList)


def calc((hand, _)):
    maxV = 0
    for jValue in range(14):
        maxV = max(maxV, calcWithJvalue(hand, jValue))
    return maxV


def work(handBidList):
    handBidList.sort(key=lambda handBid: calc(handBid))

    ans = 0
    for idx, (hand, bid) in enumerate(handBidList):
        ans += (idx + 1) * bid
    print ans


if __name__ == "__main__":
    work(read())
