#!/usr/bin/env python

def read():
    board = []
    try:
        while 1:
            board.append(list(raw_input()))
    except EOFError:
        pass
    return board


def flip(pattern):
    nextPattern = []
    for i in range(len(pattern)):
        nextPattern.append(pattern[i][::-1])
    return nextPattern

        
def rotate(pattern):
    nextPattern = [['*' for c in range(len(pattern))] for r in range(len(pattern[0]))]
    
    for r in range(len(pattern)):
        for c in range(len(pattern[0])):
            nextPattern[c][len(pattern) - r - 1] = pattern[r][c]

    return nextPattern
            

def work(board):
    pattern = [
        "                  # ", \
        "#    ##    ##    ###", \
        " #  #  #  #  #  #   "  \
    ]

    sz = len(board)
    
    used = [[False for i in range(sz)] for j in range(sz)]
    
    for fl in range(2):
        pattern = flip(pattern)
        for rot in range(4):
            pattern = rotate(pattern)

            for r in range(sz - len(pattern) + 1):
                for c in range(sz - len(pattern[0]) + 1):
                    isMatch = True
                    for rr in range(len(pattern)):
                        for cc in range(len(pattern[0])):
                            if pattern[rr][cc] == '#' and board[r + rr][c + cc] == '.':
                                isMatch = False

                    if isMatch:
                        for rr in range(len(pattern)):
                            for cc in range(len(pattern[0])):
                                if pattern[rr][cc] == '#':
                                    used[r + rr][c + cc] = True
                                

    cnt = 0
    for i in range(sz):
        for j in range(sz):
            if used[i][j] == False and board[i][j] == '#':
                cnt += 1
    print cnt
                                    


if __name__ == "__main__":
    work(read())
