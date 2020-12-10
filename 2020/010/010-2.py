#!/usr/bin/env python

def read():
    vList = []
    try:
        while 1:
            vList.append(int(raw_input()))
    except EOFError:
        pass
    return vList


def work(vList):
    vList.append(0)
    vList.sort()
    vList.append(vList[-1] + 3)
    
    dp = [0 for _ in range(len(vList))]
    dp[0] = 1
    
    for i in range(len(dp)):
        for j in range(1, 4):
            if i + j < len(dp) and vList[i + j] - vList[i] <= 3:
                dp[i + j] += dp[i]
    
    print dp[-1]

    
if __name__ == "__main__":
    work(read())
