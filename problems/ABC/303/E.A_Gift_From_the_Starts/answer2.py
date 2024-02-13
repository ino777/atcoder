N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]


# 隣接リスト生成
vertex = {i+1: [] for i in range(N)}
for e in edges:
    u, v = e[0], e[1]
    vertex[u].append(v)
    vertex[v].append(u)

count = [0] * N
for k, v in vertex.items():
    count[len(v)] += 1
