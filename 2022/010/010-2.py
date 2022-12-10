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


def isLit(cycle, spritePos):
    cycle = (cycle - 1) % 40 + 1
    return cycle in [spritePos, spritePos + 1, spritePos + 2]

    
def work(lines):
    s = ''
    
    spritePos = 1
    cycle = 1
    
    for line in lines:
        if line[0] == 'noop':
            s += '#' if isLit(cycle, spritePos) else '.'
            cycle += 1
        else:
            s += '#' if isLit(cycle, spritePos) else '.'
            cycle += 1
            s += '#' if isLit(cycle, spritePos) else '.'
            spritePos += line[1]
            cycle += 1

    for i in range(6):
        print s[i*40:(i+1)*40]


if __name__ == "__main__":
    work(read())
