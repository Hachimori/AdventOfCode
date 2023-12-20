#!/usr/bin/env python

def read():
    flow2ruleList = {}
    while 1:
        line = raw_input()
        if not line:
            break

        flow, ruleListStr = line.split('{')

        ruleList = []
        for ruleStr in ruleListStr[:-1].split(','):
            if ruleStr.find(':') != -1:
                # rule
                colonIdx = ruleStr.find(':')

                # (x or m or a or s, > or <, number, flow or R or A)
                ruleList.append((ruleStr[0], ruleStr[1], int(ruleStr[2:colonIdx]), ruleStr[colonIdx+1:]))
            else:
                # flow or R or A
                ruleList.append(ruleStr)

        flow2ruleList[flow] = ruleList

    return flow2ruleList


def rec(flow, xMin, xMax, mMin, mMax, aMin, aMax, sMin, sMax, flow2ruleList):
    if flow == 'A':
        return max(0, xMax - xMin + 1) * max(0, mMax - mMin + 1) * max(0, aMax - aMin + 1) * max(0, sMax - sMin + 1)

    if flow == 'R':
        return 0

    ret = 0
    for rule in flow2ruleList[flow]:
        if type(rule) is str:
            ret += rec(rule, xMin, xMax, mMin, mMax, aMin, aMax, sMin, sMax, flow2ruleList)
        else:
            if rule[0] == 'x' and rule[1] == '<':
                ret += rec(rule[3], xMin, min(xMax, rule[2] - 1), mMin, mMax, aMin, aMax, sMin, sMax, flow2ruleList)
                xMin = max(xMin, rule[2])
            elif rule[0] == 'x' and rule[1] == '>':
                ret += rec(rule[3], max(xMin, rule[2] + 1), xMax, mMin, mMax, aMin, aMax, sMin, sMax, flow2ruleList)
                xMax = min(xMax, rule[2])
            elif rule[0] == 'm' and rule[1] == '<':
                ret += rec(rule[3], xMin, xMax, mMin, min(mMax, rule[2] - 1), aMin, aMax, sMin, sMax, flow2ruleList)
                mMin = max(mMin, rule[2])
            elif rule[0] == 'm' and rule[1] == '>':
                ret += rec(rule[3], xMin, xMax, max(mMin, rule[2] + 1), mMax, aMin, aMax, sMin, sMax, flow2ruleList)
                mMax = min(mMax, rule[2])
            elif rule[0] == 'a' and rule[1] == '<':
                ret += rec(rule[3], xMin, xMax, mMin, mMax, aMin, min(aMax, rule[2] - 1), sMin, sMax, flow2ruleList)
                aMin = max(aMin, rule[2])
            elif rule[0] == 'a' and rule[1] == '>':
                ret += rec(rule[3], xMin, xMax, mMin, mMax, max(aMin, rule[2] + 1), aMax, sMin, sMax, flow2ruleList)
                aMax = min(aMax, rule[2])
            elif rule[0] == 's' and rule[1] == '<':
                ret += rec(rule[3], xMin, xMax, mMin, mMax, aMin, aMax, sMin, min(sMax, rule[2] - 1), flow2ruleList)
                sMin = max(sMin, rule[2])
            elif rule[0] == 's' and rule[1] == '>':
                ret += rec(rule[3], xMin, xMax, mMin, mMax, aMin, aMax, max(sMin, rule[2] + 1), sMax, flow2ruleList)
                sMax = min(sMax, rule[2])
    return ret


def work(flow2ruleList):
    print rec('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000, flow2ruleList)


if __name__ == "__main__":
    work(read())
