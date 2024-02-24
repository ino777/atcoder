N = int(input())
A = list(map(int, input().split()))

import math

def is_square(n):
    return int(math.sqrt(n))**2 == n


def prime(n):
    res = []
    for p in range(2, n):
        if p*p > n:
            break
        if n % p != 0:
            continue
        e = 0
        while n%p==0:
            e += 1
            n //= p
        res.append((p, e))
    if n != 1:
        res.append((n, 1))
    prod = 1
    for p, e in res:
        if e % 2 == 1:
            prod *= p
    return prod

not_square = []
for a in A:
    not_square.append(prime(a))

from collections import defaultdict
memo = defaultdict(int)
for a in not_square:
    memo[a] += 1

count = 0
for k, v in memo.items():
    if k == 0:
        count += N*(N-1)//2 - (N-v)*(N-v-1)//2
    else:
        count += v*(v-1)//2
print(count)