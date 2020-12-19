#!/usr/bin/env python

import itertools


def read():
    rule = {}
    while 1:
        s = raw_input()
        if not s: break

        base, subruleStr = s.split(':')
        subruleList = [s.split() for s in subruleStr.split('|')]

        for i in range(len(subruleList)):
            if subruleList[i][0].startswith('"'): continue
            subruleList[i] = map(int, subruleList[i])
        
        rule[int(base)] = subruleList

    messageList = []
    while 1:
        s = raw_input()
        if not s: break
        messageList.append(s)

    return rule, messageList


def dfs(cur, rule):
    subruleList = rule[cur]
    if len(subruleList) == 1 and type(subruleList[0][0]) == str:
        return subruleList[0][0][1]

    ret = []
    for subrule in subruleList:
        resultList = [dfs(nex, rule) for nex in subrule]
        ret.extend("".join(prod) for prod in itertools.product(*resultList))
        
    return ret


def isValid(message, m42, m31):
    lenM42 = len(m42[0])
    cntM42 = 0
    while (any(message.startswith(s) for s in m42)):
        message = message[lenM42:]
        cntM42 += 1
    
    lenM31 = len(m31[0])
    cntM31 = 0
    while (any(message.startswith(s) for s in m31)):
        message = message[lenM31:]
        cntM31 += 1

    return len(message) == 0 and 0 < cntM31 < cntM42


def work((rule, messageList)):
    m42 = dfs(42, rule)
    m31 = dfs(31, rule)

    print sum(isValid(message, m42, m31) for message in messageList)


if __name__ == "__main__":
    work(read())
