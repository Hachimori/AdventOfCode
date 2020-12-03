#!/usr/bin/env python

adj = {}
while 1:
    try:
        s = raw_input()
    except:
        break

    a, b = s.split(')')
    
    if a in adj:
        adj[a].add(b)
    else:
        adj[a] = set([b])
        
    if b in adj:
        adj[b].add(a)
    else:
        adj[b] = set([a])


def dfs(cur, pre, adj):
    if cur == "SAN":
        return 0
    
    for nex in adj[cur]:
        if nex == pre:
            continue
        
        ret = dfs(nex, cur, adj)
        
        if ret >= 0:
            return ret + 1
    
    return -1
        
        
print dfs("YOU", "", adj) - 2

