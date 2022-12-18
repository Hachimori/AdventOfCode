#!/usr/bin/env python

def read():
    ret = set([])
    while 1:
        try:
            line = raw_input()
            ret.add(tuple(map(int, line.split(','))))
        except EOFError:
            break
    return ret


def work(xyzSet):
    cnt = 0
    for (x, y, z) in xyzSet:
        dx = [0, 1, 0, -1, 0, 0]
        dy = [-1, 0, 1, 0, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]
        for i in range(6):
            cnt += (x + dx[i], y + dy[i], z + dz[i]) not in xyzSet
    print cnt


if __name__ == "__main__":
    work(read())
