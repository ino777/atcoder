S = input()

s0 = S[0]
s1 = S[1]
s2 = S[2]

ans = ''
if s0 != s1 and s0 != s2:
    ans = 1
else:
    for i, c in enumerate(S):
        if c != s0:
            ans = i + 1
            break
print(ans)
