#!/usr/bin/env python
#
# Runtime is 0m29.104s
# Environment:
#   - 2.6 GHz 6 core intel Core i7
#   - 16 GB 2400 MHz DDR4 RAM


def read():
    opList = []

    try:
        while 1:
            onOff, xyzStr = raw_input().split()
            for ch in 'xyz=.,':
                xyzStr = xyzStr.replace(ch, ' ')
            opList.append((onOff, map(int, map(int, xyzStr.split()))))
    except EOFError:
        pass
        
    return opList


def work(opList):
    cnt = 0
    
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                isOn = False
                for (onOff, (x1, x2, y1, y2, z1, z2)) in opList:
                    if not (x1 <= x <= x2): continue
                    if not (y1 <= y <= y2): continue
                    if not (z1 <= z <= z2): continue
                    isOn = onOff == 'on'

                cnt += isOn
    
    print cnt


if __name__ == "__main__":
    work(read())
