#!/usr/bin/env python

def read():
    lines = []
    try:
        while 1:
            lines.append(raw_input())
    except EOFError:
        pass
    return lines


def work(lines):
    color2limit = {"red": 12, "green": 13, "blue": 14}
    ans = 0

    for line in lines:
        game = line.split(':')[0]
        rounds = line.split(':')[1].split(';')

        isOk = True
        for round in rounds:
            for cntColor in round.split(','):
                cnt = int(cntColor.split()[0])
                color = cntColor.split()[1]
                if cnt > color2limit[color]:
                    isOk = False

        if isOk:
            ans += int(game.split()[1])

    print ans


if __name__ == "__main__":
    work(read())
