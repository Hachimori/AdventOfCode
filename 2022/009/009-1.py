#!/usr/bin/env python

def read():
    ret = []
    while 1:
        try:
            ch, v = raw_input().split()
            ret.append((ch, int(v)))
        except EOFError:
            break
    return ret


def work(data):
    visited = set([(0, 0)])
    hr, hc = 0, 0
    tr, tc = 0, 0
    
    for (ch, v) in data:
        dr, dc = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}[ch]

        for i in range(v):
            hr += dr
            hc += dc

            if abs(hr - tr) == 2 or abs(hc - tc) == 2:
                if hr != tr:
                    tr += +1 if tr < hr else -1
                if hc != tc:
                    tc += +1 if tc < hc else -1

                visited.add((tr, tc))
            
    print len(visited)


if __name__ == "__main__":
    work(read())
