#!/usr/bin/env python


# adj[created type] := (# of created type), [(# of type1, type1), (# of type2 , type2), ..., (# of created type, created type)]
adj = {}


def read():
    while 1:
        try:
            s = raw_input()
        except:
            break

        for ch in ",=>":
            s = s.replace(ch, '')

        sList = s.split()

        toPush = []
        for i in range(0, len(sList) - 2, 2):
            toPush.append((int(sList[i]), sList[i + 1]))

        if sList[-1] in adj:
            print "Produced chemical has duplicates: sList[-1]"
            break

        adj[sList[-1]] = (int(sList[-2]), toPush)

    if "ORE" in adj:
        print "There's a formula for producing ORE"
    adj["ORE"] = (-1, [])


def dfs(curr, visited, order):
    visited.add(curr)
    for (_, nex) in adj[curr][1]:
        if nex in visited: continue
        dfs(nex, visited, order)
    order.append(curr)

    
def isOk(nFuelNeed):
    order = []
    visited = set([])
    dfs("FUEL", visited, order)

    type2needCount = {"FUEL": nFuelNeed}
    for createType in order[::-1]:
        createdCount, edge = adj[createType]

        executeCount = (type2needCount[createType] + createdCount - 1) / createdCount

        for (nNeed, needType) in edge:
            if needType not in type2needCount:
                type2needCount[needType] = 0
            type2needCount[needType] += nNeed * executeCount

    return type2needCount["ORE"] <= 1000000000000


def work():
    ok = 1
    ng = 100000000000
    while ok + 1 < ng:
        mid = (ng + ok) / 2
            
        if isOk(mid):
            ok = mid
        else:
            ng = mid
    print ok


read()
work()
