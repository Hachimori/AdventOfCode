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


def work(qList):
    mask = ""
    address2value = {}

    for q in qList:
        if type(q) is str:
            mask = q
        else:
            address, value = q

            for (idx, ch) in enumerate(mask[::-1]):
                if ch == '0':
                    value &= ~(1 << idx)
                elif ch == '1':
                    value |= (1 << idx)
            
            address2value[address] = value

    
    print sum(value for (address, value) in address2value.items())


if __name__ == "__main__":
    work(read())
