N, M, K = map(int, input().split())

n = set([k*N for k in range(1, 2*K+1)])
m = set([k*M for k in range(1, 2*K+1)])

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

lcm = N*M/gcd(N, M)
lcm_nm = set([k*lcm for k in range(1, 2*K+1)])

s = (n | m) - lcm_nm
print(sorted(list(s))[K-1])

