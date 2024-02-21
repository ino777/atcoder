N, M = map(int, input().split())

graph = [{} for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    graph[A-1][B-1] = C
    graph[B-1][A-1] = C

ou = [-1]*N
re = [-1]*N

from collections import deque

stack = deque([0])
ou[0] = 0
# 幅優先探索
while stack:
    v = stack.popleft()
    nex = list(graph[v].keys())

    # 訪問済みを先に回す
    fr = []
    bk = []
    for e in nex:
        if re[e] == -1:
            bk.append(e)
        else:
            fr.append(e)
    nex = fr + bk

    for e in nex:
        if ou[e] == -1:
            stack.append(e)
            ou[e] = ou[v] + graph[v][e]
        else:
            ou[v] = min(ou[v], ou[e]+graph[e][v])
            ou[e] = min(ou[e], ou[v]+graph[v][e])


stack = deque([N-1])
re[N-1] = 0
while stack:
    v = stack.popleft()
    nex = list(graph[v].keys())

    # 訪問済みを先に回す
    fr = []
    bk = []
    for e in nex:
        if re[e] == -1:
            bk.append(e)
        else:
            fr.append(e)
    nex = fr + bk

    for e in nex:
        if re[e] == -1:
            stack.append(e)
            re[e] = re[v] + graph[v][e]
        else:
            re[v] = min(re[v], re[e]+graph[e][v])
            re[e] = min(re[e], re[v]+graph[v][e])


for k in range(N):
    print(ou[k]+re[k])