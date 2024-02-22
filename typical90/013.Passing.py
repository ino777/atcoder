"""
ダイクストラ法
"""

N, M = map(int, input().split())

graph = [{} for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    graph[A-1][B-1] = C
    graph[B-1][A-1] = C


import heapq

def dijkstra(n, start):
    dist = [10**9]*n
    dist[start] = 0
    q = [(0, start)]
    while len(q)>0:
        _, v = heapq.heappop(q)

        for nex in graph[v].keys():
            if dist[v] + graph[v][nex] < dist[nex]:
                dist[nex] = dist[v] + graph[v][nex]
                heapq.heappush(q, (dist[nex], nex))
    return dist

ou = dijkstra(N, 0)
re = dijkstra(N, N-1)


for k in range(N):
    print(ou[k]+re[k])