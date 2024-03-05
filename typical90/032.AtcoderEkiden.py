N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())

d = [set() for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    d[X].add(Y)
    d[Y].add(X)

from itertools import permutations

p = permutations(range(N), N)


cand = []
for v in p:
    ok = True
    for i in range(len(v)-1):
        if v[i+1] in d[v[i]]:
            ok = False
            break
    if ok:
        cand.append(v)

ans = 10**18
for c in cand:
    tmp = 0
    for i in range(N):
        tmp += A[c[i]][i]
    ans = min(tmp, ans)

if ans >= 10**18:
    print(-1)
else:
    print(ans)