#!/usr/bin/env python

import sys


def read():
    lines = sys.stdin.readlines()
    return [line.split() for line in lines]


def ch2id(ch):
    if ch in "ABC":
        return "ABC".index(ch)
    else:
        return "XYZ".index(ch)


def work(lines):
    score = 0
    
    for (oppCh, selfCh) in lines:
        oppId, result = ch2id(oppCh), ch2id(selfCh)
        
        score += [0, 3, 6][result]

        selfId = (oppId + [2, 0, 1][result]) % 3

        score += [1, 2, 3][selfId]

    print score
        

if __name__ == "__main__":
    work(read())
