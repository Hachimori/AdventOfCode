#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            ret.append(raw_input())
        except EOFError:
            break
    return ret


def ch2baseTen(ch):
    if ch == '=':
        return -2
    elif ch == '-':
        return -1
    else:
        return int(ch)


def val2baseTen(val):
    base10 = 0
    for ch in val:
        base10 = 5 * base10 + ch2baseTen(ch)
    return base10


def baseTen2val(base10):
    ret = ''
    while base10:
        rem = base10 % 5
        if rem <= 2:
            ret += chr(ord('0') + rem)
            carry = 0
        else:
            ret += '=' if rem == 3 else '-'
            carry = 1
        base10 /= 5
        base10 += carry
    return ret[::-1]


def work(valList):
    ans = 0
    for val in valList:
        ans += val2baseTen(val)
    print baseTen2val(ans)


if __name__ == "__main__":
    work(read())
