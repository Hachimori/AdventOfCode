#!/usr/bin/env python

def read():
    return map(int, raw_input().split(','))


def work(vList):
    ave = sum(vList) // len(vList)
    
    ans = 10 ** 18
    for d in range(2):
        pt = ave + d
        cost = 0
        for v in vList:
            n = abs(v - pt)
            cost += n * (n + 1) // 2
        ans = min(ans, cost)
        
    print ans


if __name__ == "__main__":
    work(read())
