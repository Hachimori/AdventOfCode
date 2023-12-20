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

                # (x or m or a or s, > or < number, flow or R or A)
                ruleList.append((ruleStr[0], ruleStr[1:colonIdx], ruleStr[colonIdx+1:]))
            else:
                # flow or R or A
                ruleList.append(ruleStr)

        flow2ruleList[flow] = ruleList

    part2valList = []
    while 1:
        line = raw_input()
        if not line:
            break
        part2val = {}
        for partStr in line[1:-1].split(','):
            part2val[partStr[0]] = int(partStr[2:])
        part2valList.append(part2val)

    return flow2ruleList, part2valList


def isAccept(part2val, flow2ruleList):
    flow = 'in'
    while flow != 'A' and flow != 'R':
        for rule in flow2ruleList[flow]:
            if type(rule) is str:
                flow = rule
                break
            elif eval('part2val[\'%s\']%s' % (rule[0], rule[1])):
                flow = rule[2]
                break
    return flow == 'A'


def work((flow2ruleList, part2valList)):
    ans = 0
    for part2val in part2valList:
        if isAccept(part2val, flow2ruleList):
            for (_, val) in part2val.iteritems():
                ans += val
    print ans


if __name__ == "__main__":
    work(read())
