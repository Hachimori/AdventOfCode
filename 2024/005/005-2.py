#!/usr/bin/env python3

def read():
    pairs = []
    while True:
        line = input()
        if line == '':
            break
        a, b = map(int, line.split('|'))
        pairs.append((a, b))

    data = []
    try:
        while True:
            line = input()
            vList = list(map(int, line.split(',')))
            data.append(vList)
    except EOFError:
        pass

    return pairs, data


def work(pairs, data):
    constraintSet = set()
    for a, b in pairs:
        constraintSet.add((a, b))

    total = 0

    for vList in data:
        toAdd = False
        for i in range(len(vList)):
            for j in range(i + 1, len(vList)):
                if (vList[j], vList[i]) in constraintSet:
                    vList[i], vList[j] = vList[j], vList[i]
                    toAdd = True
        if toAdd:
            total += vList[len(vList) // 2]

    print(total)


if __name__ == "__main__":
    work(*read())
