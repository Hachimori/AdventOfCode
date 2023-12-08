#!/usr/bin/env python

def read():
    steps = raw_input()
    raw_input()
    mapping = {}
    try:
        while 1:
            line = raw_input()
            alphaLine = ''.join(ch if ch.isalnum() else ' ' for ch in line)
            elements = alphaLine.split()
            mapping[elements[0]] = elements[1:]
    except EOFError:
        pass
    return steps, mapping


def isOk(currList):
    for curr in currList:
        if not curr.endswith('Z'):
            return False
    return True


def calc(curr, steps, mapping):
    idx = 0
    while not curr.endswith('Z'):
        curr = mapping[curr][0 if steps[idx % len(steps)] == 'L' else 1]
        idx += 1
    return idx


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b


def work((steps, mapping)):
    currList = []
    for pos in mapping.keys():
        if pos.endswith('A'):
            currList.append(pos)

    cycleList = []
    for curr in currList:
        cycleList.append(calc(curr, steps, mapping))

    ans = 1
    for cycle in cycleList:
        ans = lcm(ans, cycle)
    print ans


if __name__ == "__main__":
    work(read())
