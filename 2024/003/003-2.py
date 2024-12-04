#!/usr/bin/env python3

import re

def read():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    return lines


isDo = True

def calc(line):
    global isDo

    ret = 0
    while True:
        m = re.search(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", line)
        if m is None:
            break
        if m.group(0) == "do()":
            isDo = True
        elif m.group(0) == "don't()":
            isDo = False
        elif isDo:
            ret += int(m.group(2)) * int(m.group(3))
        line = line[m.end():]
    return ret


def work(lines):
    ans = 0
    for line in lines:
        ans += calc(line)
    print(ans)


if __name__ == "__main__":
    work(read())
