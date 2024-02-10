N = int(input())

from math import isqrt

def Eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False

    for p in range(2, n+1):
        if not is_prime[p]:
            continue
        
        q = p*p
        while q <= n:
            is_prime[q] = False
            q += p
    return is_prime


# 2から√Nまでの素数列挙
sqrt_n = int(isqrt(N))
is_primes = Eratosthenes(sqrt_n)
primes = [i for i, v in enumerate(is_primes) if v]

# n以下の素数
S = list(map(int,is_primes))
for i in range(len(S)-1):
    S[i+1] += S[i]


count = 0
for i in range(len(primes)):
    a = primes[i]
    if a*a*a*a*a >= N:
        break
    for j in range(i+1, len(primes)):
        b = primes[j]
        if a*a*b*b*b >= N:
            break
        D = int(isqrt(N//(a*a*b)))
        # b < c <= D となるcの数を求める
        count += S[D] - S[b]
print(count)