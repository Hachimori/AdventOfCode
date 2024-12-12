#!/usr/bin/env python3

def read():
    return list(map(int, input().split()))


def rec(curStep, value, dp):
    if curStep == 75:
        return 1

    if value in dp[curStep]:
        return dp[curStep][value]

    ret = 0
    if value == 0:
        ret = rec(curStep + 1, 1, dp)
    elif len(str(value)) % 2 == 0:
        leng = len(str(value))
        a = rec(curStep + 1, int(str(value)[:leng//2]), dp)
        b = rec(curStep + 1, int(str(value)[leng//2:]), dp)
        ret = a + b
    else:
        ret = rec(curStep + 1, value * 2024, dp)

    dp[curStep][value] = ret
    return ret


def work(vList):
    # dp[curStep][value] := how many stones
    dp = [{} for i in range(76)]
    ans = 0

    for v in vList:
        ans += rec(0, v, dp)
    print(ans)


if __name__ == "__main__":
    work(read())
