#!/usr/bin/env python

def read():
    s = [ch if ch in '0123456789-' else ' ' for ch in raw_input()]
    return map(int, ''.join(s).split())


def work((x1, x2, y1, y2)):
    maxY = 0
    
    for initVY in range(1000):
        vy = initVY
        maxYcandi = 0
        curY = 0
        while not (vy < 0 and curY < y1):
            curY += vy
            vy -= 1
            maxYcandi = max(maxYcandi, curY)
            if y1 <= curY <= y2:
                maxY = maxYcandi

    print maxY


if __name__ == "__main__":
    work(read())
