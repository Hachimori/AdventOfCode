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


def execute(opValList):
    visited = [False for i in range(len(opValList))]
    idx = 0
    acc = 0
    
    while idx < len(visited):
        if not (0 <= idx < len(visited)):
            # Index out of range
            return
        if visited[idx]:
            # Infinity loop
            return
        
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

    print acc


def work(opValList):
    for i in range(len(opValList)):
        op, val = opValList[i]
        if op == "nop":
            opValList[i] = ("jmp", val)
        elif op == "jmp":
            opValList[i] = ("nop", val)
        else:
            continue
        
        execute(opValList)
        
        opValList[i] = (op, val)


if __name__ == "__main__":
    work(read())
