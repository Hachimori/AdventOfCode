#!/usr/bin/env python


def calc(_vList, inputList):
    vList = {}
    for i in range(len(_vList)):
        vList[i] = _vList[i]
    
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
            b = getAddress(0)
            nInstruction = 2
            vList[b] = ord(inputList[0]) # input
            del inputList[0]
        elif a == 4:
            b = getValue(0)
            nInstruction = 2
            # print 'output:', b # output b
            output.append(b)
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

    return output



vList = map(int, raw_input().split(','))

inputList = []

# If A is hole, then jump
inputList.extend("NOT A J\n")

# If B is hole, and D is not hole, then jump
inputList.extend("NOT B T\n")
inputList.extend("AND D T\n")
inputList.extend("OR T J\n")

# If C is hole, but A, B, D are not, then jump
inputList.extend("NOT C T\n")
inputList.extend("AND A T\n")
inputList.extend("AND B T\n")
inputList.extend("AND D T\n")
inputList.extend("OR T J\n")


# Finish
inputList.extend("WALK\n")
output = calc(vList, inputList)

print "".join(map(chr, output[:-1]))
print output[-1]
