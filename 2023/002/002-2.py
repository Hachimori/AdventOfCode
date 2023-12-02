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
    ans = 0

    for line in lines:
        game = line.split(':')[0]
        rounds = line.split(':')[1].split(';')

        color2maxCnt = {"red": 0, "green": 0, "blue": 0}
        for round in rounds:
            for cntColor in round.split(','):
                cnt = int(cntColor.split()[0])
                color = cntColor.split()[1]
                color2maxCnt[color] = max(cnt, color2maxCnt[color])
        ans += color2maxCnt["red"] * color2maxCnt["green"] * color2maxCnt["blue"]

    print ans


if __name__ == "__main__":
    work(read())
