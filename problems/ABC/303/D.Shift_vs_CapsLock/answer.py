X, Y, Z = map(int, input().split())
S = input()

# dp[i][c]
dp = [[0 for _ in range(2)] for _ in range(len(S))]

for i in range(len(S)):
    s = S[i]
    if i==0:
        if s == 'a':
            dp[0][0] = X
            dp[0][1] = Z + Y
        elif s == 'A':
            dp[0][0] = Y
            dp[0][1] = Z + X
    else:
        if s == 'a':
            dp[i][0] = min(dp[i-1][0] + X, dp[i-1][1] + Z + X)
            dp[i][1] = min(dp[i-1][0] + Z + Y, dp[i-1][1] + Y)
        elif s == 'A':
            dp[i][0] = min(dp[i-1][0] + Y, dp[i-1][1] + Z + Y)
            dp[i][1] = min(dp[i-1][0] + Z + X, dp[i-1][1] + X)


print(min(*dp[-1]))