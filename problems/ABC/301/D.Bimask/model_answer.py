S = list(reversed(input()))
N = int(input())

# Sのうち1のみを加味した値(?は0と仮定)
s = 0
for i in range(len(S)):
    s |= (S[i] == '1') << i

if s > N:
    print(-1)
else:
    for i in reversed(range(len(S))):
        # 各?対して
        if S[i] == '?':
            # tmpは?を1としたときの値
            tmp = s | 1 << i
            if tmp <= N:
                # tmpがNを越えてなければ採用
                s = tmp
    print(s)