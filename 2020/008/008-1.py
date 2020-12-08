#!/usr/bin/env python

def read():
    opValList = []
    try:
        while 1:
            op, val = raw_input().split()
            opValList.append((op, int(val)))
    except EOFError:
        pass
    return opValList


def work(opValList):
    visited = [False for i in range(len(opValList))]
    idx = 0
    acc = 0
    
    while 1:
        if visited[idx]:
            print acc
            break
        visited[idx] = True

        op, val = opValList[idx]

        if op == "acc":
            acc += val
            idx += 1
        elif op == "jmp":
            idx += val
        elif op == "nop":
            idx += 1
        else:
            print "Unknown operator: " + op


if __name__ == "__main__":
    work(read())
