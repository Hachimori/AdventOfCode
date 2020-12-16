#!/usr/bin/env python

import re


def read():
    rangeList = []
    while 1:
        line = raw_input()
        if not line:
            break
        
        mList = [m for m in re.finditer(r"(\d+)-(\d+)", line)]

        toPush = []
        for m in mList:
            toPush.append((int(m.group(1)), int(m.group(2))))
        rangeList.append(toPush)

    fieldList = []
    raw_input()
    fieldList.append(map(int, raw_input().split(',')))
    raw_input()

    raw_input()
    while 1:
        line = raw_input()
        if not line:
            break
        fieldList.append(map(int, line.split(',')))
        
    return rangeList, fieldList


def rec(idx, history, usedColumn, dp, rangeList, fieldList):
    if idx == len(usedColumn):
        ans = 1
        for i in range(6):
            ans *= fieldList[0][history[i]]
        print ans
        return True
    
    if tuple(usedColumn) in dp:
        return False
    
    dp.add(tuple(usedColumn))

    for column in range(len(fieldList[0])):
        if usedColumn[column]:
            continue

        isOk = True
        for field in fieldList:
            if not ((rangeList[idx][0][0] <= field[column] <= rangeList[idx][0][1]) or \
                    (rangeList[idx][1][0] <= field[column] <= rangeList[idx][1][1])):
                isOk = False

        if not isOk:
            continue
                 
        usedColumn[column] = True
        
        if rec(idx + 1, history + [column], usedColumn, dp, rangeList, fieldList):
            return True
        
        usedColumn[column] = False
        
    return False
    

def work((rangeList, fieldList)):
    filtered = []
    for field in fieldList:
        isOk = True
        for column in field:
            if not any(ranges[0][0] <= column <= ranges[0][1] or ranges[1][0] <= column <= ranges[1][1] for ranges in rangeList):
                isOk = False
        if isOk:
            filtered.append(field)
                       

    fieldList = filtered
    
    dp = set([])
    usedColumn = [False for _ in rangeList]

    rec(0, [], usedColumn, dp, rangeList, fieldList)

    
if __name__ == "__main__":
    work(read())
