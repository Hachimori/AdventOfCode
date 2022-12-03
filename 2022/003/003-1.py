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
    
    for line in lines:
        a, b = line[:len(line)/2], line[len(line)/2:]

        for ch in a:
            if ch in b:
                ans += ch2priority(ch)
                break

    print ans


if __name__ == "__main__":
    work(read())
