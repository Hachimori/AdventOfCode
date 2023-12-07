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


def ch2value(ch):
    return "#23456789TJQKA".index(ch)


def vList2score(vList):
    ret = 0
    for v in vList:
        ret = ret * 20 + v
    return ret


def calc((hand, _)):
    VALUE_COUNT = len("#23456789TJQKA")
    vList = map(ch2value, hand)

    # Five of a kind
    for v in range(VALUE_COUNT):
        if vList.count(v) == 5:
            return 20**15 + vList2score(vList)

    # Four of a kind
    for v1 in range(VALUE_COUNT):
        for v2 in range(VALUE_COUNT):
            if vList.count(v1) == 4 and vList.count(v2) == 1:
                return 20**14 + vList2score(vList)

    # Full house
    for v1 in range(VALUE_COUNT):
        for v2 in range(VALUE_COUNT):
            if vList.count(v1) == 3 and vList.count(v2) == 2:
                return 20**13 + vList2score(vList)

    # Three of a kind
    for v in range(VALUE_COUNT):
        if vList.count(v) == 3:
            return 20 ** 12 + vList2score(vList)

    # Two pair
    for v1 in range(VALUE_COUNT):
        for v2 in range(v1 + 1, VALUE_COUNT):
            if vList.count(v1) == 2 and vList.count(v2) == 2:
                return 20 ** 11 + vList2score(vList)

    # One pair
    for v in range(VALUE_COUNT):
        if vList.count(v) == 2:
            return 20 ** 10 + vList2score(vList)

    # High card
    return vList2score(vList)


def work(handBidList):
    handBidList.sort(key=lambda handBid: calc(handBid))

    ans = 0
    for idx, (hand, bid) in enumerate(handBidList):
        ans += (idx + 1) * bid
    print ans


if __name__ == "__main__":
    work(read())
