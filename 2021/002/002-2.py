#!/usr/bin/env python

def read():
    cmdValList = []
    
    try:
        while 1:
            cmd, val = raw_input().split()
            cmdValList.append((cmd, int(val)))
    except EOFError:
        pass
    
    return cmdValList


def work(cmdValList):
    pos = 0
    depth = 0
    aim = 0

    for (cmd, val) in cmdValList:
        if cmd == "forward":
            pos += val
            depth += aim * val
        elif cmd == "up":
            aim -= val
        else:
            aim += val

    print pos * depth


if __name__ == "__main__":
    work(read())
