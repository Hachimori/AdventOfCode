#!/usr/bin/env python

# Referred following solution:
#   https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kepo1bk/?utm_source=reddit&utm_medium=web2x&context=3

from scipy.optimize import fsolve

x = []
y = []
z = []
vx = []
vy = []
vz = []

def read():
    try:
        while 1:
            ptStr, vecStr = raw_input().split("@")
            xx, yy, zz = map(int, ptStr.split(","))
            vxx, vyy, vzz = map(int, vecStr.split(","))
            x.append(xx)
            y.append(yy)
            z.append(zz)
            vx.append(vxx)
            vy.append(vyy)
            vz.append(vzz)
    except EOFError:
        pass


def func((x0, y0, z0, vx0, vy0, vz0)):
    eq = []
    for i in range(1, 4):
        eq.append((y0 - y[i]) * (vx[i] - vx0) + (x0 - x[i]) * (vy0 - vy[i]))
        eq.append((z0 - z[i]) * (vx[i] - vx0) + (x0 - x[i]) * (vz0 - vz[i]))
    return eq


def work():
    x0, y0, z0, vx0, vy0, vz0 = fsolve(func, [x[0], y[0], z[0], vx[0], vy[0], vz[0]])
    print x0 + y0 + z0


if __name__ == "__main__":
    read()
    work()
