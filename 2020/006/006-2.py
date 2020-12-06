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
        for ch in sList[0]:
            if all([ch in s for s in sList]):
                cnt += 1
    print cnt


if __name__ == "__main__":
    work(read())
