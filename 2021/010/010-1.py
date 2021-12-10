#!/usr/bin/env python

def read():
    lineList = []

    try:
        while 1:
            lineList.append(raw_input())
    except EOFError:
        pass

    return lineList


def work(lineList):
    total = 0

    for line in lineList:
        stack = []
        for ch in line:
            if (not stack or stack[-1] != '(') and ch == ')':
                total += 3
                break
            elif (not stack or stack[-1] != '[') and ch == ']':
                total += 57
                break;
            elif (not stack or stack[-1] != '{') and ch == '}':
                total += 1197
                break;
            elif (not stack or stack[-1] != '<') and ch == '>':
                total += 25137
                break;
            elif ch in '([{<':
                stack.append(ch)
            else:
                del stack[-1]


    print total


if __name__ == "__main__":
    work(read())
