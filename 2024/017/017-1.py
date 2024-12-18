#!/usr/bin/env python3

def read():
    A = int(input().split()[2])
    B = int(input().split()[2])
    C = int(input().split()[2])
    input()
    vList = list(map(int, input().split()[1].split(",")))
    return (A, B, C, vList)


def work(A, B, C, vList):
    output = []

    cur = 0
    while cur < len(vList):
        def calcCombo(v):
            if 0 <= v <= 3:
                return v
            elif v == 4:
                return A
            elif v == 5:
                return B
            elif v == 6:
                return C
            elif v == 7:
                print("Invalid opcode")
                return -1

        opcode = vList[cur]
        combo = calcCombo(vList[cur + 1])
        literal = vList[cur + 1]

        if opcode == 0:
            # adv
            A = A // (2 ** combo)

        elif opcode == 1:
            # bxl
            B = B ^ literal

        elif opcode == 2:
            # bst
            B = combo % 8

        elif opcode == 3:
            # jnz
            if A == 0:
                pass
            else:
                cur = literal - 2

        elif opcode == 4:
            # bxc
            B = B ^ C

        elif opcode == 5:
            # out
            output.append(combo % 8)

        elif opcode == 6:
            # bdv
            B = A // (2 ** combo)

        elif opcode == 7:
            # cdv
            C = A // (2 ** combo)

        cur += 2

    print(','.join(map(str, output)))


if __name__ == "__main__":
    work(*read())
