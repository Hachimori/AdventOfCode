#!/usr/bin/env python


def read():
    lines = []
    while 1:
        try:
            lines.append(raw_input())
        except EOFError:
            break
    return lines


def ch2priority(ch):
    if ch.islower():
        return ord(ch) - ord('a') + 1
    else:
        return ord(ch) - ord('A') + 27


def work(lines):
    ans = 0
    
    for idx in range(0, len(lines), 3):
        lineA, lineB, lineC = lines[idx], lines[idx + 1], lines[idx + 2]

        for ch in lineA:
            if ch in lineB and ch in lineC:
                ans += ch2priority(ch)
                break

    print ans


if __name__ == "__main__":
    work(read())
