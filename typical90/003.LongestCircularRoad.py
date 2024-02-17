"""
グラフの2頂点間の最大値(木の直径)
1. 適当な頂点uを選ぶ
2. uから最も遠い頂点vを求める
3. vから最も遠い頂点wを求める
このときのv-wの長さが木の直径となる
"""
N = int(input())

vertex = [[] for _ in range(N)]

for _ in range(N-1):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    vertex[A].append(B)
    vertex[B].append(A)


def f(u):
    dist = [-1] * N
    dist[u] = 0

    # スタック
    st = [u]
    while st:
        v = st.pop()
        for next_v in vertex[v]:
            if dist[next_v] == -1:
                st.append(next_v)
                dist[next_v] = dist[v] + 1
    return dist


u = 0
v = max(enumerate(f(u)), key=lambda x: x[1])[0]
w, d = map(int, max(enumerate(f(v)), key=lambda x: x[1]))
print(d+1)

