#!/usr/bin/env python

def read():
    numList = map(int, raw_input().split(','))
    boardList = []
    
    try:
        while 1:
            raw_input()
            toPush = []
            for i in range(5):
                toPush.append(map(int, raw_input().split()))
            boardList.append(toPush)
    except EOFError:
        pass
   
    return numList, boardList


def getScore(board, numList):
    # Calculate score
    score = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] not in numList:
                score += board[i][j]
    score *= numList[-1]
    
    # Check bingo
    for r in range(5):
        isOK = True
        for c in range(5):
            if board[r][c] not in numList:
                isOK = False
        if isOK:
            return score

    for c in range(5):
        isOK = True
        for r in range(5):
            if board[r][c] not in numList:
                isOK = False
        if isOK:
            return score

    return score if isOK else -1


    
def work((numList, boardList)):
    for nPick in range(1, len(numList)):
        for board in boardList:
            score = getScore(board, numList[:nPick])
            if score > 0:
                print score
                return


if __name__ == "__main__":
    work(read())
