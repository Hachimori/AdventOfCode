#!/usr/bin/env python

import copy


def read():
    sList = []
    
    try:
        while 1:
            sList.append(raw_input())
    except EOFError:
        pass

    return sList
            

def get(isMostCommon, sList):
    ret = 0
    
    for i in range(len(sList[0])):
        cnt = [0, 0]
        
        for j in range(len(sList)):
            cnt[int(sList[j][i])] += 1

        mostCommonBit = 1 if cnt[1] >= cnt[0] else 0
        leastCommonBit = not mostCommonBit

        if isMostCommon or len(sList) == 1:
            ret |= mostCommonBit << (len(sList[0]) - i - 1)
            sList = [s for s in sList if int(s[i]) == mostCommonBit]
        else:
            ret |= leastCommonBit << (len(sList[0]) - i - 1)
            sList = [s for s in sList if int(s[i]) == leastCommonBit]

    return ret


def work(sList):
    O2 = get(True, copy.deepcopy(sList))
    CO2 = get(False, copy.deepcopy(sList))
    
    print O2 * CO2


if __name__ == "__main__":
    work(read())
