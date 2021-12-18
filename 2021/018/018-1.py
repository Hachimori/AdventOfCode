#!/usr/bin/env python


def getSnailfishNumber(s):
    ret = []
    for ch in s:
        if ch in '[]':
            ret.append(ch)
        elif ch.isdigit():
            ret.append(int(ch))
    return ret


def read():
    snailfishNumberList = []
    
    try:
        while True:
            s = raw_input()
            snailfishNumberList.append(getSnailfishNumber(s))
    except EOFError:
        pass

    return snailfishNumberList


def processExplosion(snailfishNumber):
    depth = 0

    for idx in range(len(snailfishNumber)):
        if snailfishNumber[idx] == '[':
            depth += 1
        elif snailfishNumber[idx] == ']':
            depth -= 1

        if depth == 5:
            left = idx
            while left >= 0:
                if type(snailfishNumber[left]) == int:
                    snailfishNumber[left] += snailfishNumber[idx + 1]
                    break
                left -= 1

            right = idx + 4
            while right < len(snailfishNumber):
                if type(snailfishNumber[right]) == int:
                    snailfishNumber[right] += snailfishNumber[idx + 2]
                    break
                right += 1
            
            snailfishNumber[idx:idx+4] = [0]
            
            return True
    
    return False


def processSplit(snailfishNumber):
    for idx in range(len(snailfishNumber)):
        if type(snailfishNumber[idx]) == int and snailfishNumber[idx] >= 10:
            v1 = snailfishNumber[idx] / 2
            v2 = (snailfishNumber[idx] + 1) / 2
            del snailfishNumber[idx]

            for elem in ['[', v1, v2, ']']:
                snailfishNumber.insert(idx, elem)
                idx += 1
            
            return True
    
    return False

    
def process(snailfishNumber):
    while True:
        if not processExplosion(snailfishNumber) and not processSplit(snailfishNumber):
            break


def calcMagnitude(snailfishNumber):
    stack = []
    for elem in snailfishNumber:
        if elem == '[' or type(elem) == int:
            stack.append(elem)
        else:
            t = 3 * stack[-2] + 2 * stack[-1]
            del stack[-3:]
            stack.append(t)
    
    return stack[0]


def work(snailfishNumberList):
    cur = snailfishNumberList[0]
    
    for snailfishNumber in snailfishNumberList[1:]:
        cur = ['['] + cur + snailfishNumber + [']']
        process(cur)

    print calcMagnitude(cur)


if __name__ == "__main__":
    work(read())
