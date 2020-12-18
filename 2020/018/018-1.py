#!/usr/bin/env python
import re


def read():
    sList = []
    try:
        while 1:
            sList.append(raw_input())
    except EOFError:
        pass
    return sList


def calc(s):
    elements = s.split()
    ret = int(elements[0])
    
    for i in range(1, len(elements), 2):
        if elements[i] == '+':
            ret += int(elements[i + 1])
        else:
            ret *= int(elements[i + 1])
    
    return ret


def work(sList):
    total = 0
    
    for s in sList:
        
        while 1:
            m = re.search(r"\((\d+ (\+|\*) )+\d+\)", s)
            
            if not m:
                total += calc(s)
                break
            
            s = s.replace(m.group(0), str(calc(m.group(0)[1:-1])), 1)
    
    print total

    
if __name__ == "__main__":
    work(read())
