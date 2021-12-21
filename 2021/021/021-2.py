#!/usr/bin/env python

def read():
    posList = []
    posList.append(int(raw_input().split()[-1]))
    posList.append(int(raw_input().split()[-1]))
    return posList


def rec(aTurn, aPos, aScore, bPos, bScore, dp, aCnt):
    if aScore >= 21 or bScore >= 21:
        return aCnt == (aScore >= 21)

    if dp[aTurn][aPos][aScore][bPos][bScore] != -1:
        return dp[aTurn][aPos][aScore][bPos][bScore]

    total = 0
    for nMove1 in range(1, 4):
        for nMove2 in range(1, 4):
            for nMove3 in range(1, 4):
                if aTurn:
                    nexApos = (aPos + nMove1 + nMove2 + nMove3) % 10
                    nexAscore = aScore + (10 if nexApos == 0 else nexApos)
                    nexBpos = bPos
                    nexBscore = bScore
                else:
                    nexApos = aPos
                    nexAscore = aScore
                    nexBpos = (bPos + nMove1 + nMove2 + nMove3) % 10
                    nexBscore = bScore + (10 if nexBpos == 0 else nexBpos)
                total += rec(not aTurn, nexApos, nexAscore, nexBpos, nexBscore, dp, aCnt)
        
    dp[aTurn][aPos][aScore][bPos][bScore] = total
    return total
    
    
def work(posList):
    dp = [[[[[-1 for m in range(21)] for l in range(10)] for k in range(21)] for j in range(10)] for i in range(2)]
    aWin = rec(True, posList[0] % 10, 0, posList[1] % 10, 0, dp, True)
    
    dp = [[[[[-1 for m in range(21)] for l in range(10)] for k in range(21)] for j in range(10)] for i in range(2)]
    bWin = rec(True, posList[0] % 10, 0, posList[1] % 10, 0, dp, False)

    print max(aWin, bWin)


if __name__ == "__main__":
    work(read())
