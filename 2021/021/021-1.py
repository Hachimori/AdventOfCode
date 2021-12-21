#!/usr/bin/env python

def read():
    posList = []
    posList.append(int(raw_input().split()[-1]))
    posList.append(int(raw_input().split()[-1]))
    return posList


def work(posList):
    nRoll = 0
    scoreList = [0, 0]

    while 1:
        turn = nRoll % 2
        for _ in range(3):
            nMove = (nRoll + 1) % 10
            nRoll += 1

            posList[turn] = (posList[turn] + nMove) % 10
            if posList[turn] == 0:
                posList[turn] = 10

        scoreList[turn] += posList[turn]
        
        if scoreList[turn] >= 1000:
            print nRoll * scoreList[not turn]
            break


if __name__ == "__main__":
    work(read())
