N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

L = []

# 隣接リスト生成
vertex = {i+1: [] for i in range(N)}
for e in edges:
    u, v = e[0], e[1]
    vertex[u].append(v)
    vertex[v].append(u)

def f(p, q):
    k = len(vertex[p])
    L.append(k)

    # 次数が2以上の頂点を探す
    for i in vertex[p]:
        if i == q:
            continue
        if len(vertex[i]) == 2:
            next_q = [v for v in vertex[i] if v != p][0]
            # 次の星の中心点
            next_p = [v for v in vertex[next_q] if v != i][0]
            f(next_p, next_q)

# 適当な端を見つける
q = [v for v in vertex.keys() if len(vertex[v]) == 1][0]
# 星の中心点
p = vertex[q][0]

f(p, q)

L.sort()
print(" ".join(map(str, L)))