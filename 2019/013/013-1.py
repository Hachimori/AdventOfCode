#!/usr/bin/env python


def calc(_vList):
    vList = {}
    for i in range(len(_vList)):
        vList[i] = _vList[i]

    rc2id = {}
        
    output = []
    idx = 0
    base = 0
    while True:
        a = vList[idx] % 100
        
        if a not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]:
            print a
            print "???"
            break

        # pos: 0, 1, 2, ...
        def getValue(pos):
            if vList[idx] < 0:
                print vList[idx]
                print "????"
            mode = vList[idx] / 100 / (10 ** pos) % 10
            if mode == 0:
                # address
                if vList[idx + pos + 1] not in vList:
                    vList[vList[idx + pos + 1]] = 0
                return vList[vList[idx + pos + 1]]
            elif mode == 1:
                # value
                return vList[idx + pos + 1]
            elif mode == 2:
                # relative
                if not vList[idx + pos + 1] + base in vList:
                    vList[vList[idx + pos + 1] + base] = 0
                return vList[vList[idx + pos + 1] + base]
        
        # pos: 0, 1, 2, ...
        def getAddress(pos):
            if vList[idx] < 0:
                print vList[idx]
                print "????"
            mode = vList[idx] / 100 / (10 ** pos) % 10
            if mode == 0:
                # address
                return vList[idx + pos + 1]
            elif mode == 1:
                # value
                print "value mode is not available in getAddress()"
                return -1
            elif mode == 2:
                # relative
                if not vList[idx + pos + 1] + base in vList:
                    vList[vList[idx + pos + 1] + base] = 0
                return vList[idx + pos + 1] + base
            
        nInstruction = 0
        
        if a == 1:
            b, c, d = getValue(0), getValue(1), getAddress(2)
            nInstruction = 4
            vList[d] = b + c
        elif a == 2:
            b, c, d = getValue(0), getValue(1), getAddress(2)
            nInstruction = 4
            vList[d] = b * c
        elif a == 3:
            print "Error: Input operation appears."
            break
        elif a == 4:
            b = getValue(0)
            nInstruction = 2
            print 'output:', b # output b
            output.append(b)
            if len(output) % 3 == 0:
                x = output[-3]
                y = output[-2]
                tileId = output[-1]
                rc2id[(y, x)] = tileId
        elif a == 5:
            b = getValue(0)
            if b != 0:
                # idx + nInstruction => getValue(1)
                nInstruction = getValue(1) - idx
            else:
                nInstruction = 3
        elif a == 6:
            b = getValue(0)
            if b == 0:
                # idx + nInstruction => getValue(1)
                nInstruction = getValue(1) - idx
            else:
                nInstruction = 3
        elif a == 7:
            b, c, d = getValue(0), getValue(1), getAddress(2)
            nInstruction = 4
            if b < c:
                vList[d] = 1
            else:
                vList[d] = 0
        elif a == 8:
            b, c, d = getValue(0), getValue(1), getAddress(2)
            nInstruction = 4
            if b == c:
                vList[d] = 1
            else:
                vList[d] = 0
        elif a == 9:
            b = getValue(0)
            nInstruction = 2
            base += b
        else:
            break
        idx += nInstruction
        
    return rc2id


vList = map(int, raw_input().split(','))
rc2id = calc(vList)


minR, minC = rc2id.keys()[0]
maxR, maxC = rc2id.keys()[0]
for (r, c) in rc2id.keys():
    minR = min(minR, r)
    minC = min(minC, c)
    maxR = max(maxR, r)
    maxC = max(maxC, c)

for r in range(minR, maxR + 1):
    line = ''
    for c in range(minC, maxC + 1):
        tileId = 0 if (r, c) not in rc2id else rc2id[(r, c)]
        if tileId == 0:
            line += ' '
        elif tileId == 1:
            line += '#'
        elif tileId == 2:
            line += 'x'
        elif tileId == 3:
            line += '-'
        elif tileId == 4:
            line += 'o'
    print line
print ""

print "# of walls: " + str(sum([tileId == 2 for tileId in rc2id.values()]))
