#!/usr/bin/env python

def read():
    return raw_input()


def getHeight(filled):
    for i in range(len(filled) - 1, -1, -1):
        if not any(filled[i]):
            return len(filled) - i - 1
    print "???"
    return -1
    

def printFilled(filled):
    h = getHeight(filled)
    for i in range(len(filled) - 3 - h, len(filled)):
        for j in range(7):
            print '#' if filled[i][j] else '.',
        print ""
    

def dropBlock(block, filled, turn, dirs):
    height = getHeight(filled)

    row, col = len(filled), len(filled[0])
    r, c = len(filled) - height - len(block) - 3, 2

    while 1:
        dc = -1 if dirs[turn[0] % len(dirs)] == '<' else +1
        turn[0] += 1
        
        # blow
        isBlown = True
        for blockR in range(len(block)):
            for blockC in range(len(block[blockR])):
                if block[blockR][blockC] == '.':
                    continue
                if not (0 <= c + blockC + dc < col):
                    isBlown = False
                    continue
                if filled[r + blockR][c + blockC + dc]:
                    isBlown = False

        if isBlown:
            c += dc

        # move down
        isDown = True
        for blockR in range(len(block)):
            for blockC in range(len(block[blockR])):
                if block[blockR][blockC] == '.':
                    continue
                if not (0 <= r + blockR + 1 < row):
                    isDown = False
                    continue
                if filled[r + blockR + 1][c + blockC]:
                    isDown = False
        
        if isDown:
            r += 1
        else:
            # Block stops, process next block
            for blockR in range(len(block)):
                for blockC in range(len(block[blockR])):
                    if block[blockR][blockC] == '.':
                        continue
                    filled[r + blockR][c + blockC] = True
            break

        
def calc(curDrop, curHeight, preDrop, preHeight, turn, filled, blocks, dirs):
    remainDrop = 1000000000000 - curDrop

    totalHeight = curHeight
    totalHeight += remainDrop / (curDrop - preDrop) * (curHeight - preHeight)
    
    remainDrop %= curDrop - preDrop

    curDrop %= len(blocks)
    for _ in range(remainDrop):
        dropBlock(blocks[curDrop], filled, turn, dirs)
        curDrop = (curDrop + 1) % len(blocks)

    totalHeight += getHeight(filled) - curHeight

    return totalHeight
    

def work(dirs):
    blocks = [
        [
            '####'
        ],
        [
            '.#.',
            '###',
            '.#.'
        ],
        [
            '..#',
            '..#',
            '###'
        ],
        [
            '#',
            '#',
            '#',
            '#'
        ],
        [
            '##',
            '##'
        ]
    ]

    filled = [[False for j in range(7)] for i in range(20000)]
    turn = [0]
    nDrop = 0

    turn2nDropHeight = {}

    while 1:
        if nDrop >= 3000 and nDrop % 5 == 0:
            t = turn[0] % len(dirs)
            if t in turn2nDropHeight:
                curDrop, curHeight = nDrop, getHeight(filled)
                preDrop, preHeight = turn2nDropHeight[t]
                print calc(curDrop, curHeight, preDrop, preHeight, turn, filled, blocks, dirs)
                return
            else:
                turn2nDropHeight[t] = (nDrop, getHeight(filled))

        dropBlock(blocks[nDrop % len(blocks)], filled, turn, dirs)
        nDrop += 1


if __name__ == "__main__":
    work(read())
