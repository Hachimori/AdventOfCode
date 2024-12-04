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


def calc(line):
    ret = 0
    while True:
        m = re.search(r"mul\((\d+),(\d+)\)", line)
        if m is None:
            break
        ret += int(m.group(1)) * int(m.group(2))
        line = line[m.end():]
    return ret


def work(lines):
    ans = 0
    for line in lines:
        ans += calc(line)
    print(ans)


if __name__ == "__main__":
    work(read())
