#!/usr/bin/env python

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


def doit(name2nexList, name2rev2pulse, name2isFF, name2isCnj, name2isOn, name2loCnt, name2hiCnt):
    nexQ = [('broadcaster', 'button', False)]

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

            if sendPulse:
                name2hiCnt[cur] += len(name2nexList[cur])
            else:
                name2loCnt[cur] += len(name2nexList[cur])

            for nex in name2nexList[cur]:
                nexQ.append((nex, cur, sendPulse))


def work((name2nexList, name2rev2pulse, name2isFF, name2isCnj, nameSet)):
    '''
    print name2nexList
    print name2rev2pulse
    print name2isFF
    print name2isCnj
    print nameSet
    '''

    name2isOn = {}
    name2loCnt = {}
    name2hiCnt = {}

    for name in nameSet:
        name2isOn[name] = False
        name2loCnt[name] = 0
        name2hiCnt[name] = 0
        if name not in name2nexList:
            name2nexList[name] = []
        if name not in name2rev2pulse:
            name2rev2pulse[name] = {}
        if name not in name2isFF:
            name2isFF[name] = False
        if name not in name2isCnj:
            name2isCnj[name] = False

    nPush = 1000
    for _ in range(nPush):
        doit(name2nexList, name2rev2pulse, name2isFF, name2isCnj, name2isOn, name2loCnt, name2hiCnt)

    #print name2isOn
    #print name2nexList
    #print name2rev2pulse
    #print name2loCnt
    #print name2hiCnt

    loSum = nPush
    hiSum = 0
    for name in name2loCnt.iterkeys():
        #if name == "broadcaster":
        #    continue
        loSum += name2loCnt[name]
        hiSum += name2hiCnt[name]
    print loSum * hiSum


if __name__ == "__main__":
    work(read())
