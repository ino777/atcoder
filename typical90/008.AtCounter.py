"""
動的計画法
dp[i][j] = i番目までの文字でatcoderのj番目までの組み合わせができる通り数

1. i番目がatcoderのいずれでもない場合
dp[i+1][j] += dp[i][j]
2. i番目がatcoerのj番目の文字の場合
dp[i+1][j+1] += dp[i][j]
"""
N = int(input())
S = input()

keyword = 'atcoder'
l = len(keyword)

dp = [[0]*(l+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(l+1):
        if j < l and S[i] == keyword[j]:
            dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % (10**9+7)
        dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % (10**9+7)

print(dp[N][l])