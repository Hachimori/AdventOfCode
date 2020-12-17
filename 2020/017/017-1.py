#!/usr/bin/env python

def read():
    init = []
    try:
        while 1:
            init.append(raw_input())
    except EOFError:
        pass
    return init


def work(init):
    SZ = 15
    board = {}
    
    for x in range(-SZ, SZ):
        for y in range(-SZ, SZ):
            for z in range(-SZ, SZ):
                board[(x, y, z)] = False

    for x in range(len(init)):
        for y in range(len(init[x])):
            board[(x, y, 0)] = init[x][y] == '#'

    for loop in range(6):
        nextBoard = {}

        for x in range(-SZ, SZ):
            for y in range(-SZ, SZ):
                for z in range(-SZ, SZ):
                    cntActive = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                if dx == dy == dz == 0:
                                    continue
                                nx = x + dx
                                ny = y + dy
                                nz = z + dz
                                if (nx, ny, nz) in board and board[(nx, ny, nz)]:
                                    cntActive += 1
                    
                    if board[(x, y, z)]:
                        nextBoard[(x, y, z)] = 2 <= cntActive <= 3
                    else:
                        nextBoard[(x, y, z)] = cntActive == 3

        board = nextBoard

    print sum(board.values())


if __name__ == "__main__":
    work(read())
