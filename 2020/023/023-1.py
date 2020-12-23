#!/usr/bin/env python

def read():
    return map(int, list(raw_input()))


def work(vList):
    nMove = 100
    for i in range(nMove):
        destVal = (vList[0] + 9) % 10
            
        while 1:
            if destVal in vList[1:4] or destVal not in vList[4:]:
                destVal = (destVal + 9) % 10
                continue
            destIdx = vList[4:].index(destVal) + 5
            break

        vList = vList[:destIdx] + vList[1:4] + vList[destIdx:]
        del vList[1:4]
        vList = vList[1:] + [vList[0]]

    idx = vList.index(1)
    result = vList[idx:] + vList[:idx]
    print "".join(map(str, result[1:]))


if __name__ == "__main__":
    work(read())
