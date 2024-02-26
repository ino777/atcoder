N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for a, b in zip(A, B):
    diff += abs(a-b)

ok = abs(K - diff) % 2 == 0 and K >= diff
if ok:
    print('Yes')
else:
    print('No')