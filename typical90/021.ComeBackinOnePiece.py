"""
強連結成分分解(SCC)

2回dfsする
"""

import sys

sys.setrecursionlimit(200000)

N, M = map(int, input().split())

g = [set() for _ in range(N)]
rg = [set() for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    g[A].add(B)
    rg[B].add(A)

used = [False]*N
order = []
def dfs(v):
    used[v] = True
    for u in g[v]:
        if not used[u]:
            dfs(u)
    order.append(v)
for i in range(N):
    if not used[i]:
        dfs(i)

group = [[] for _ in range(N)]
used = [False]*N
def rdfs(v, i):
    used[v] = True
    for u in rg[v]:
        if not used[u]:
            rdfs(u, i)
    group[i].append(v)

i = 0
for s in reversed(order):
    if not used[s]:
        rdfs(s, i)
        i += 1

count = 0
for c in group:
    n = len(c)
    if n > 1:
        count += n*(n-1)//2
print(count)