#!/usr/bin/env python

BUF = 1000

def read():
    adj = [[] for _ in range(BUF)] # adj[id] = [(id1, num1), (id2, num2), ...]
    color2id = {}
    
    try:
        while 1:
            elements = raw_input().split()

            def add2dict(s):
                if s not in color2id:
                    sz = len(color2id)
                    color2id[s] = sz

            add2dict(" ".join(elements[:2]))
            myId = color2id[" ".join(elements[:2])]
            
            for idx in range(3, len(elements)):
                if not elements[idx].startswith("bag"):
                    continue
                if " ".join(elements[idx - 2 : idx]) == "no other":
                    continue
                
                add2dict(" ".join(elements[idx - 2 : idx]))
                
                oppId = color2id[" ".join(elements[idx - 2 : idx])]
                adj[myId].append((oppId, int(elements[idx - 3])))
    except EOFError:
        pass

    return adj, color2id


def dfs(curr, adj, goal):
    if curr == goal:
        return True
    for (next, cnt) in adj[curr]:
        if dfs(next, adj, goal):
            return True
    return False


def work((adj, color2id)):
    cnt = 0
    for idx in range(len(color2id)):
        if idx == color2id["shiny gold"]:
            continue
        cnt += dfs(idx, adj, color2id["shiny gold"])
    print cnt


if __name__ == "__main__":
    work(read())
