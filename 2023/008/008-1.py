#!/usr/bin/env python

def read():
    steps = raw_input()
    raw_input()
    mapping = {}
    try:
        while 1:
            line = raw_input()
            alphaLine = ''.join(ch if ch.isalpha() else ' ' for ch in line)
            elements = alphaLine.split()
            mapping[elements[0]] = elements[1:]
    except EOFError:
        pass
    return steps, mapping


def work((steps, mapping)):
    idx = 0
    curr = "AAA"
    while curr != "ZZZ":
        curr = mapping[curr][0 if steps[idx % len(steps)] == 'L' else 1]
        idx += 1
    print idx


if __name__ == "__main__":
    work(read())
