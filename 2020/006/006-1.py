#!/usr/bin/env python


def read():
    dataList = []

    try:
        sList = []
        while True:
            s = raw_input()
            if len(s) == 0:
                dataList.append(sList)
                sList = []
            else:
                sList.append(s)
    except EOFError:
        pass
    
    return dataList


def work(dataList):
    cnt = 0

    for sList in dataList:
        chSet = set([])
        for ch in ''.join(sList):
            chSet.add(ch)
        cnt += len(chSet)

    print cnt


if __name__ == "__main__":
    work(read())
