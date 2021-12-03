#!/usr/bin/env python

def read():
    sList = []
    
    try:
        while 1:
            sList.append(raw_input())
    except EOFError:
        pass

    return sList
            


def work(sList):
    gamma = 0
    epsilon = 0
    
    for i in range(len(sList[0])):
        cnt = [0, 0]
        for j in range(len(sList)):
            cnt[int(sList[j][i])] += 1

        mostCommonBit = 0 if cnt[0] > cnt[1] else 1
        leastCommonBit = not mostCommonBit
        
        gamma |= mostCommonBit << (len(sList[0]) - i - 1)
        epsilon |= leastCommonBit << (len(sList[0]) - i - 1)

    print gamma * epsilon


if __name__ == "__main__":
    work(read())
