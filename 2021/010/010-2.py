#!/usr/bin/env python

def read():
    lineList = []

    try:
        while 1:
            lineList.append(raw_input())
    except EOFError:
        pass

    return lineList


def calcScore(line):
    stack = []
    for ch in line:
        if (not stack or stack[-1] != '(') and ch == ')':
            return 0
        elif (not stack or stack[-1] != '[') and ch == ']':
            return 0
        elif (not stack or stack[-1] != '{') and ch == '}':
            return 0
        elif (not stack or stack[-1] != '<') and ch == '>':
            return 0
        elif ch in '([{<':
            stack.append(ch)
        else:
            del stack[-1]

    ret = 0
    for ch in reversed(stack):
        ret *= 5
        if ch == '(':
            ret += 1
        elif ch == '[':
            ret += 2
        elif ch == '{':
            ret += 3
        elif ch == '<':
            ret += 4
    
    return ret


def work(lineList):
    scoreList = []

    for line in lineList:
        score = calcScore(line)
        if score > 0:
            scoreList.append(score)

    scoreList.sort()
    
    print scoreList[len(scoreList) / 2]


if __name__ == "__main__":
    work(read())
