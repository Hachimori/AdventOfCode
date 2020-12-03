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


def dfs(cur, adj, ans):
    if cur not in adj:
        return

    ans[0] += len(adj[cur])
    for nex in adj[cur]:
        dfs(nex, adj, ans)
        
        
ans = [0]
for key in adj.keys():
    dfs(key, adj, ans)


print ans[0]
