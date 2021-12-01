#!/usr/bin/env python

def read():
    vList = []
    
    try:
        while 1:
            vList.append(int(raw_input()))
    except EOFError:
        pass
    
    return vList


def work(vList):
    ans = 0
    
    for i in range(1, len(vList)):
        ans += vList[i] > vList[i - 1]
        
    print ans 


if __name__ == "__main__":
    work(read())
