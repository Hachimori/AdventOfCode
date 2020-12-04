#!/usr/bin/env python


def read():
    dataList = []

    try:
        concatLine = ""
        while 1:
            line = raw_input()
            if len(line) == 0:
                toPush = [word.split(':') for word in concatLine.split()]
                dataList.append(toPush)
                concatLine = ""
            else:
                concatLine += ' ' + line
    except EOFError:
        pass
    
    return dataList


def work(dataList):
    cnt = 0
    for data in dataList:
        nElement = 0
        for element in data:
            if element[0] in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
                nElement += 1
        cnt += nElement == 7

    print cnt


if __name__ == "__main__":
    work(read())
