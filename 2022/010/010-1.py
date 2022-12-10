#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            op = raw_input().split()
            if len(op) == 2:
                ret.append([op[0], int(op[1])])
            else:
                ret.append([op[0]])
        except EOFError:
            break
    return ret


def isCalcCycle(cycle):
    return cycle in [20, 60, 100, 140, 180, 220]


def work(lines):
    X = 1
    cycle = 1
    ans = 0
    
    for line in lines:
        if line[0] == 'noop':
            cycle += 1
            if isCalcCycle(cycle):
                ans += cycle * X
        else:
            cycle += 1
            if isCalcCycle(cycle):
                ans += cycle * X
            X += line[1]
            cycle += 1
            if isCalcCycle(cycle):
                ans += cycle * X
            
    print ans


if __name__ == "__main__":
    work(read())
