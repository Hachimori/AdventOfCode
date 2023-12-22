#!/usr/bin/env python

import graphviz

def read():
    name2nexList = {}
    name2rev2pulse = {}
    name2isFF = {}
    name2isCnj = {}

    nameSet = set(['broadcaster'])

    try:
        while 1:
            name, nexListStr = raw_input().split("->")

            if name[0] == '%':
                name = name[1:].strip()
                name2isFF[name] = True
                name2isCnj[name] = False
            elif name[0] == '&':
                name = name[1:].strip()
                name2isFF[name] = False
                name2isCnj[name] = True
            else:
                name = name.strip()

            nexList = nexListStr.split(',')

            name2nexList[name] = []
            nameSet.add(name)
            for nex in nexList:
                n = nex.strip()
                name2nexList[name].append(n)

                if n not in name2rev2pulse:
                    name2rev2pulse[n] = {}
                name2rev2pulse[n][name] = False
                nameSet.add(n)

    except EOFError:
        pass

    return name2nexList, name2rev2pulse, name2isFF, name2isCnj, nameSet


def doit(name2nexList, name2rev2pulse, name2isFF, name2isCnj, name2isOn):
    nexQ = [('broadcaster', 'button', False)]

    sentName = set([])

    while nexQ:
        Q = nexQ
        nexQ = []

        while Q:
            cur, prev, isHighPulse = Q[0]
            del Q[0]

            sendPulse = False

            if name2isFF[cur]:
                if isHighPulse:
                    continue
                name2isOn[cur] = not name2isOn[cur]
                sendPulse = name2isOn[cur]
            elif name2isCnj[cur]:
                name2rev2pulse[cur][prev] = isHighPulse
                isRevAllOn = all(name2rev2pulse[cur].values())
                sendPulse = not isRevAllOn
            else:
                # Broadcaster
                sendPulse = False

            if cur in ('vp', 'dc', 'cq', 'rv') and sendPulse:
                sentName.add(cur)

            for nex in name2nexList[cur]:
                nexQ.append((nex, cur, sendPulse))

    return sentName


def drawGraph(name2nexList, name2isCnj, nameSet):
    f = graphviz.Digraph()

    for name in nameSet:
        f.node(name, shape="doublecircle" if name2isCnj[name] else "circle")

    for (name, nexList) in name2nexList.iteritems():
        for nex in nexList:
            f.edge(name, nex)

    f.view()


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def work((name2nexList, name2rev2pulse, name2isFF, name2isCnj, nameSet)):
    '''
    print name2nexList
    print name2rev2pulse
    print name2isFF
    print name2isCnj
    print nameSet
    '''

    name2isOn = {}

    for name in nameSet:
        name2isOn[name] = False
        if name not in name2nexList:
            name2nexList[name] = []
        if name not in name2rev2pulse:
            name2rev2pulse[name] = {}
        if name not in name2isFF:
            name2isFF[name] = False
        if name not in name2isCnj:
            name2isCnj[name] = False

    # drawGraph(name2nexList, name2isCnj, nameSet)

    """
    nPress = 0
    for i in range(100000):
        nPress += 1
        sentName = doit(name2nexList, name2rev2pulse, name2isFF, name2isCnj, name2isOn)

        if sentName:
            print nPress, sentName
    """

    ans = 1
    v = [3847, 3797, 3877, 4051]
    for vv in v:
        ans = lcm(ans, vv)
    print ans


if __name__ == "__main__":
    work(read())
