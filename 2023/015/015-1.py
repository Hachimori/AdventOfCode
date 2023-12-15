#!/usr/bin/env python

def read():
    return raw_input().split(',')


def calc(s):
    ret = 0
    for ch in s:
        ret = (ret + ord(ch)) * 17 % 256
    return ret


def work(sList):
    ans = 0
    for s in sList:
        ans += calc(s)
    print ans


if __name__ == "__main__":
    work(read())
