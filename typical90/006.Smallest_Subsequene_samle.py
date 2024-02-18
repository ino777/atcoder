"""
辞書順最小のものを求める→貪欲法

next_c[i][c] = 文字列Sのi文字目以降で文字cが登場する最小の添え字
を準備することで、計算量の削減
"""
N, K = map(int, input().split())
S = input()
next_c = [[N]*26 for _ in range(N)]

for i in range(N-1, -1, -1):
    for j in range(26):
        if i < N -1:
            next_c[i][j] = next_c[i+1][j]
        if S[i] == chr(ord('a')+j):
            next_c[i][j] = i
print(next_c)

res = ''
l = -1
for i in range(K):
    for j in range(26):
        k = next_c[l+1][j]
        print(next_c[l+1], k)
        if N - k >= K - i:
            res += chr(ord('a')+j)
            j = k
            break
print(res)