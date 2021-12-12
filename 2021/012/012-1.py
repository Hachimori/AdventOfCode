#!/usr/bin/env python

def read():
    edgeList = []

    try:
        while 1:
            edgeList.append(raw_input().split('-'))
    except EOFError:
        pass

    return edgeList


cnt = 0

def rec(cur, visited, edgeList):
    global cnt
    
    if cur == "end":
        cnt += 1
        return

    for (a, b) in edgeList:
        if a != cur and b != cur: continue

        nex = b if a == cur else a 
        
        if nex.islower() and nex not in visited:
            visited.add(nex)
            rec(nex, visited, edgeList)
            visited.remove(nex)
        elif nex.isupper():
            rec(nex, visited, edgeList)
    

def work(edgeList):
    rec("start", set({"start"}), edgeList)
    print cnt


if __name__ == "__main__":
    work(read())
