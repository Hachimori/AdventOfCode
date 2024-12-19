#!/usr/bin/env python3


def read():
    patterns = input().split(', ')

    input()

    targets = []
    while True:
        try:
            targets.append(input())
        except EOFError:
            break

    return patterns, targets


def isOkRec(idx, visited, target, patterns):
    if idx == len(target):
        return True

    visited[idx] = True

    for pattern in patterns:
        if idx + len(pattern) < len(target) and visited[idx + len(pattern)]:
            continue
        if target[idx:].startswith(pattern):
            if isOkRec(idx + len(pattern), visited, target, patterns):
                return True

    return False


def work(patterns, targets):
    cnt = 0
    for target in targets:
        visited = [False for _ in range(len(target))]
        cnt += isOkRec(0, visited, target, patterns)
    print(cnt)


if __name__ == "__main__":
    work(*read())
