H, W, N = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

# 長方形
S = [(H, W)]

ok = True

for i in range(N):
    a = 2**A[i]
    # 判定する
    k = -1
    for j, s in enumerate(S):
        if a <= s[0] and a <= s[1]:
            k = j
            break
    # 入るものが見つからなければbreak
    if k == -1:
        ok = False
        break
    
    s = S[j]

    # 長方形を分ける（できるだけ大きい辺が残るように）
    S.pop(k)
    if s[0] - a > s[1] - a:
        S.append((s[0]-a, s[1]))
        S.append((a, s[1]-a))
    else:
        S.append((s[0], s[1]-a))
        S.append((s[0]-a, a))


if ok:
    print('Yes')
else:
    print('No')