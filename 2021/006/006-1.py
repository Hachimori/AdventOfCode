#!/usr/bin/env python

def read():
    return map(int, raw_input().split(','))


def work(vList):
    origLen = len(vList)

    for day in range(80):
        curLen = len(vList)
        for i in range(curLen):
            if vList[i] == 0:
                vList.append(8)
                vList[i] = 6
            else:
                vList[i] -= 1
        
    print len(vList)


if __name__ == "__main__":
    work(read())
