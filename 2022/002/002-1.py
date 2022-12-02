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
        oppId, selfId = ch2id(oppCh), ch2id(selfCh)
        
        score += [1, 2, 3][selfId]

        if (oppId + 1) % 3 == selfId:
            score += 6
        elif oppId == selfId:
            score += 3
        else:
            score += 0

    print score
        
        


if __name__ == "__main__":
    work(read())
