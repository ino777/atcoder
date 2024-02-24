"""
列の操作は区間DP
dp[l][r] = (l, l+1, ..., r 番目までの要素全てを取り除くのに必要なコスト)

- パターン1
l, rの要素が最後に取り除かれる場合
- パターン2
それ以外の場合
"""

N = int(input())
A = list(map(int, input().split()))

dp = [[0]*(2*N) for _ in range(2*N)]

for d in range(1, 2*N, 2):
    for l in range(0, 2*N):
        r = l+d
        if r >= 2*N:
            break

        # パターン1
        p1 = dp[l+1][r-1] + abs(A[l]-A[r])
        # パターン2
        p2 = 10**9
        for k in range(l+1, r-1, 2):
            p2 = min(dp[l][k] + dp[k+1][r], p2)
        dp[l][r] = min(p1, p2)
print(dp[0][2*N-1])

"""
BFSだと計算量が大きすぎる

total = 0
st = [(i, A[:], 0) for i in range(2*N-1)]

total = 10**9
while len(st) > 0:
    i, tmp, cost = st.pop()
    cost += abs(tmp[i]-tmp[i+1])
    tmp = tmp[:i] + tmp[i+2:]
    m = len(tmp)

    if cost >= total:
        continue
    if m == 0:
        total = min(total, cost)

    for j in range(m-1):
        st.append((j, tmp, cost))

print(total)
"""