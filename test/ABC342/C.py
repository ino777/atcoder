N = int(input())
S = list(input())
Q = int(input())

import copy

memo = {}
for i, c in enumerate(S):
    if memo.get(c) is None:
        memo[c] = set()
    memo[c].add(i)


for _ in range(Q):
    c, d = map(str, input().split())
    if memo.get(c) is None:
        continue
    if c == d:
        continue
    
    if memo.get(d) is not None:
        memo[d] |= memo[c]
    else:
        memo[d] = memo[c]
    del memo[c]

result = ['']*N
for k, v in memo.items():
    for i in v:
        result[i] = k
print("".join(result))


