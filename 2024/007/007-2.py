#!/usr/bin/env python3

def read():
    equationList = []
    try:
        while True:
            line = input()
            line = line.replace(":", " ")
            equationList.append(list(map(int, line.split())))
    except EOFError:
        pass
    return equationList


def isOk(idx, cur, target, vList):
    if idx == len(vList):
        return cur == target

    if isOk(idx + 1, cur + vList[idx], target, vList):
        return True

    if isOk(idx + 1, cur * vList[idx], target, vList):
        return True

    if isOk(idx + 1, int(str(cur) + str(vList[idx])), target, vList):
        return True

    return False


def work(equationList):
    ans = 0
    for equation in equationList:
        target, vList = equation[0], equation[1:]
        if isOk(1, vList[0], target, vList):
            ans += target
    print(ans)


if __name__ == "__main__":
    work(read())
