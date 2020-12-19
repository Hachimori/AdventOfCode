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


def work((rule, messageList)):
    generatedMessage = dfs(0, rule)
    print sum(message in generatedMessage for message in messageList)
    


if __name__ == "__main__":
    work(read())
