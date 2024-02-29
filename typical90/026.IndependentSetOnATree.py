N = int(input())
graph = [[] for _ in range(N)]

for i in range(N-1):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    graph[A].append(B)
    graph[B].append(A)

st = [0]
dist = [-1]*N
dist[0] = 0

while len(st) > 0:
    v = st.pop()
    nex = graph[v]
    
    for u in nex:
        if dist[u] == -1:
            dist[u] = dist[v]+1
            st.append(u)

odd = 0
even = 0
for d in dist:
    if d % 2 == 1:
        odd += 1
    else:
        even += 1

ans = []
i = 0
while len(ans) < N//2:
    d = dist[i]
    if odd >= even and d % 2 == 1:
        ans.append(i+1)
    elif odd < even and d % 2 == 0:
        ans.append(i+1)
    i += 1
print(" ".join(map(str, ans)))