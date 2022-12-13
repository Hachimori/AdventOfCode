#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            a = eval(raw_input())
            b = eval(raw_input())
            ret.append((a, b))
            raw_input()
        except EOFError:
            break
    return ret


def myCmp(a, b):
    if (a != 0 and not a) and (b != 0 and not b):
        return 0

    if a != 0 and not a:
        return -1

    if b != 0 and not b:
        return +1

    if type(a) == int and type(b) == int:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return +1

    if type(a) == list and type(b) == list:
        for i in range(max(len(a), len(b))):
            if i == len(a):
                return -1
            elif i == len(b):
                return +1
            
            t = myCmp(a[i], b[i])
            if t != 0:
                return t
        return 0

    if type(a) == int and type(b) == list:
        return myCmp([a], b)
    
    if type(a) == list and type(b) == int:
        return myCmp(a, [b])

    print "???"
    return 2
    

def work(abList):
    ans = 0
    
    for (idx, (a, b)) in enumerate(abList):
        if myCmp(a, b) <= 0:
            ans += idx + 1
        
    print ans


if __name__ == "__main__":
    work(read())
