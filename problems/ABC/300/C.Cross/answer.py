# https://atcoder.jp/contests/abc300/tasks/abc300_c

H, W = map(int, input().split())
C = []
for _ in range(H):
    row = input()
    C.append(row)
N = min(H, W)
S = []


def is_batsu(a, b, n):
    if C[a][b] != '#':
        return False
    # 場外になるなら終わり
    if a-n < 0 or a+n >= H or b-n < 0 or b+n >= W:
        return False 
    for d in range(1, n+1):
        br = C[a+d][b+d]
        bl = C[a+d][b-d]
        tr = C[a-d][b+d]
        tl = C[a-d][b-d]
        if br != '#' or bl != '#' or tr != '#' or tl != '#':
            return False


    # .の判定
    if 0 <= a-n-1 and a+n+1 < H and 0 <= b-n-1 and b+n+1 < W and C[a+n+1][b+n+1] == '#' and C[a+n+1][b-n-1] == '#' and C[a-n-1][b+n+1] == '#' and C[a-n-1][b-n-1] == '#':
        return False
    return True


for n in range(1, N+1):
    count = 0
    for i in range(H):
        for j in range(W):
            if is_batsu(i, j, n):
                count += 1
    S.append(count)

print(" ".join(map(str, S)))


