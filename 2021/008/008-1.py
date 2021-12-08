#!/usr/bin/env python

def read():
    patternOutputList = []
    
    try:
        while 1:
            s1, s2 = raw_input().split('|')
            patternOutputList.append((s1.split(), s2.split()))
    except EOFError:
        pass

    return patternOutputList


def work(patternOutputList):
    ans = 0
    
    for (pattern, output) in patternOutputList:
        ans += sum([1 for word in output if len(word) in [2, 3, 4, 7]])

    print ans


if __name__ == "__main__":
    work(read())
