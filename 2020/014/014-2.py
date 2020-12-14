#!/usr/bin/env python
import re


def read():
    qList = []
    try:
        while 1:
            sList = raw_input().split()
            if sList[0] == "mask":
                qList.append(sList[2])
            else:
                # mem[1234]
                match = re.search(r"mem\[(\d+)\]", sList[0])
                address = int(match.group(1))

                value = int(sList[2])
                qList.append([address, value])
    except EOFError:
        pass
    return qList


def rec(idx, mask, appliedMask):
    if not appliedMask:
        return 1 << mask[idx:].count('X')

    if idx == len(mask):
        return 0
    
    ret = 0
    
    zeroList = [m for m in appliedMask if m[idx] == '0']
    oneList = [m for m in appliedMask if m[idx] == '1']
    xList = [m for m in appliedMask if m[idx] == 'X']
    
    if mask[idx] == 'X':
        if zeroList or oneList:
            ret += rec(idx + 1, mask, sum([zeroList, xList], []))
            ret += rec(idx + 1, mask, sum([oneList, xList], []))
        else:
            ret += 2 * rec(idx + 1, mask, xList)
    else:
        ret += rec(idx + 1, mask, sum([zeroList if mask[idx] == '0' else oneList, xList], []))
    
    return ret


def work(qList):
    mask = ""
    maskValueList = []

    for q in qList:
        if type(q) is str:
            mask = q
        else:
            address, value = q

            toPush = ""
            nThBit = 35
            for idx in range(len(mask)):
                if mask[idx] == '0':
                    toPush += '1' if (1 << nThBit) & address else '0'
                elif mask[idx] == '1':
                    toPush += '1'
                elif mask[idx] == 'X':
                    toPush += 'X'
                nThBit -= 1

            maskValueList.append((toPush, value))

    total = 0
    appliedMask = []
    for (mask, value) in maskValueList[::-1]:
        total += value * rec(0, mask, appliedMask)
        appliedMask.append(mask)
    print total

    
if __name__ == "__main__":
    work(read())
