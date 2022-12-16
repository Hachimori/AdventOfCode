#!/usr/bin/env python

def read():
    # ret[node] := (flow rate, adjacent nodes)
    ret = {}
    while 1:
        try:
            line = raw_input()
            sanitized = "".join([ch if ch.isupper() or ch.isdigit() else ' ' for ch in line][1:])
            sanitizedElements = sanitized.split()
            ret[sanitizedElements[0]] = (int(sanitizedElements[1]), sanitizedElements[2:])
        except EOFError:
            break
    return ret


def rec(remain, cur, opened, dp, node2rateAdjNodes):
    if remain == 0:
        return 0

    if (remain, cur, tuple(opened)) in dp:
        return dp[(remain, cur, tuple(opened))]
    
    ret = 0

    rate, adjNodes = node2rateAdjNodes[cur]
    
    # Open cur
    if cur not in opened and rate > 0:
        opened.add(cur)
        ret = max(ret, rec(remain - 1, cur, opened, dp, node2rateAdjNodes) + (remain - 1) * rate);
        opened.remove(cur)

    # Go to adjacent nodes
    for nex in adjNodes:
        ret = max(ret, rec(remain - 1, nex, opened, dp, node2rateAdjNodes));

    dp[(remain, cur, tuple(opened))] = ret
    
    return ret
    

def work(node2rateAdjNodes):
    # dp[remaining minutes, current node, opened nodes] := maximum value
    dp = {}
    print rec(30, 'AA', set([]), dp, node2rateAdjNodes)
    
    


if __name__ == "__main__":
    work(read())
