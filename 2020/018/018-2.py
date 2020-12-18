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
    
    while '+' in elements:
        idx = elements.index('+')
        result = int(elements[idx - 1]) + int(elements[idx + 1])
        del elements[idx-1:idx+2]
        elements.insert(idx - 1, str(result))
    
    ret = 1
    for element in elements:
        if element != '*':
            ret *= int(element)
    
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
