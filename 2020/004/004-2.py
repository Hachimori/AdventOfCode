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
            if element[0] == "byr" and 1920 <= int(element[1]) <= 2002 or \
              element[0] == "iyr" and 2010 <= int(element[1]) <= 2020 or \
              element[0] == "eyr" and 2020 <= int(element[1]) <= 2030 or \
              element[0] == "hgt" and ( \
                element[1].endswith("cm") and 150 <= int(element[1][:-2]) <= 193 or \
                element[1].endswith("in") and 59 <= int(element[1][:-2]) <= 76 \
                ) or \
              element[0] == "hcl" and element[1][0] == '#' and all([ch.isdigit() or 'a' <= ch <= 'f' for ch in element[1][1:]]) and len(element[1]) == 7 or \
              element[0] == "ecl" and element[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] or \
              element[0] == "pid" and element[1].isdigit() and len(element[1]) == 9:
                nElement += 1
        
        cnt += nElement == 7
    print cnt


if __name__ == "__main__":
    work(read())
