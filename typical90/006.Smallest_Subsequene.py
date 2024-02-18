N, K = map(int, input().split())
S = input()

ans = ''
i = 0
while len(ans) < K:
    i = i + min(enumerate(S[i:N-K+len(ans)+1]), key=lambda x: x[1])[0]
    ans += S[i]
    i += 1

print(ans)