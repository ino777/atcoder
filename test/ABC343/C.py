N = int(input())

cand = [i for i in range(int(N**(1/3))+1000)]

def is_kaibun(n):
    s = list(str(n))
    l = len(s)
    for i in range(l):
        if s[i] != s[l-1-i]:
            return False
    return True

ans = 1
for x in cand:
    k = x**3
    if k > N:
        break
    if is_kaibun(k):
        ans = k
print(ans)