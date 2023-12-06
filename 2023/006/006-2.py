#!/usr/bin/env python

"""
Environment:
  - MacBook Pro
  - 2.6 GHz 6core Intel Core i7
  - 16 GB 2400 MHz DDR4


Run result:
$ time ./006-2.py < input
34655848

real	0m3.692s
user	0m3.257s
sys	0m0.426s
"""

def read():
    time =  int("".join(raw_input().split()[1:]))
    distance = int("".join(raw_input().split()[1:]))
    return time, distance


def calc(time, distance):
    cnt = 0
    for t in range(time):
        cnt += t * (time - t) > distance
    return cnt


def work((time, distance)):
    print calc(time, distance)


if __name__ == "__main__":
    work(read())
