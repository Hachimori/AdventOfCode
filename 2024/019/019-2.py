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


def rec(idx, dp, target, patterns):
    if idx == len(target):
        return 1

    if dp[idx] != -1:
        return dp[idx]

    ret = 0
    for pattern in patterns:
        if target[idx:].startswith(pattern):
            ret += rec(idx + len(pattern), dp, target, patterns)

    dp[idx] = ret
    return ret


def work(patterns, targets):
    cnt = 0
    for target in targets:
        dp = [-1 for _ in range(len(target))]
        cnt += rec(0, dp, target, patterns)
    print(cnt)


if __name__ == "__main__":
    work(*read())
