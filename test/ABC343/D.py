N, T = map(int, input().split())
s = [0]*N

d = {0: N}
l = 1

for _ in range(T):
    A, B = map(int, input().split())
    A = A - 1
    tmp = s[A]
    s[A] += B
    d[tmp] -= 1
    if d[tmp] == 0:
        del d[tmp]
        l -= 1
    if d.get(s[A]) is None:
        d[s[A]] = 1
        l += 1
    else:
        d[s[A]] += 1
    print(l)