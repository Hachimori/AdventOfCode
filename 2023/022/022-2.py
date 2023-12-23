#!/usr/bin/env python

"""
Environment:
  - MacBook Pro
  - 2.6 GHz 6core Intel Core i7
  - 16 GB 2400 MHz DDR4


Run result:
$ time ./022-2.py < input
75358

real	1m11.322s
user	1m10.648s
sys	0m0.307s
"""

import copy

def read():
    pieces = []
    try:
        while 1:
            bgnStr, endStr = raw_input().split('~')
            bgn = map(int, bgnStr.split(','))
            end = map(int, endStr.split(','))
            if bgn > end:
                bgn, end = end, bgn
            pieces.append((bgn, end))
    except EOFError:
        pass
    return pieces


def blocks(piece):
    if piece[0][0] != piece[1][0]:
        d = (1, 0, 0)
    elif piece[0][1] != piece[1][1]:
        d = (0, 1, 0)
    else:
        d = (0, 0, 1)

    cur = [piece[0][0], piece[0][1], piece[0][2]]
    ret = []
    while 1:
        ret.append(tuple(cur))
        if cur == piece[1]:
            break
        for i in range(3):
            cur[i] += d[i]
    return ret


def isVertical(piece):
    return piece[0][2] != piece[1][2]


def isInGround(piece):
    return piece[0][2] == 1


def letFall(pieces):
    xyzSet = set([])
    for piece in pieces:
        for block in blocks(piece):
            xyzSet.add(tuple(block))
    fallSet = set([])

    while 1:
        isFall = False

        for (id, piece) in enumerate(pieces):
            if isInGround(piece):
                continue

            if (
                (isVertical(piece) and tuple([piece[0][0], piece[0][1], piece[0][2] - 1]) not in xyzSet) or
                    (not isVertical(piece) and all([tuple([block[0], block[1], block[2] - 1]) not in xyzSet for block in blocks(piece)]))
            ):

                for block in blocks(piece):
                    xyzSet.remove(tuple(block))
                    xyzSet.add(tuple([block[0], block[1], block[2] - 1]))

                piece[0][2] -= 1
                piece[1][2] -= 1

                isFall = True
                fallSet.add(id)

        if not isFall:
            break

    return fallSet


def work(pieces):
    letFall(pieces)

    ans = 0
    for toRemove in range(len(pieces)):
        newPieces = copy.deepcopy(pieces[:toRemove] + pieces[toRemove+1:])
        ans += len(letFall(newPieces))
    print ans


if __name__ == "__main__":
    work(read())
