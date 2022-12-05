#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            elements = raw_input().split()
            ret.append(map(int, elements[1::2]))
        except EOFError:
            break
    return ret


def work(operations):
    stack = []
    stack.append(list('ZJG'))
    stack.append(list('QLRPWFVC'))
    stack.append(list('FPMCLGR'))
    stack.append(list('LFBWPHM'))
    stack.append(list('GCFSVQ'))
    stack.append(list('WHJZMQTL'))
    stack.append(list('HFSBV'))
    stack.append(list('FJZS'))
    stack.append(list('MCDPFHBT'))

    for (n, src, dst) in operations:
        src -= 1
        dst -= 1
        stack[dst] += stack[src][-n::][::-1]
        del stack[src][-n:]
        
    ans = ''
    for s in stack:
        ans += s[-1]
    print ans


if __name__ == "__main__":
    work(read())
