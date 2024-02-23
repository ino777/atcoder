"""
nCkの逆元による計算
n!はnが大きいとオーバーフローしてしまうので、計算結果はmodをとる
足し算、引き算、掛け算はそのままmodを取ればいいが、割り算はそのままmodをとると計算結果がおかしくなる
よって、逆元を使う
【参考】
https://ikatakos.com/pot/programming_algorithm/number_theory/mod_combination

フェルマーの小定理
a^(-1) = a^(M-2) (mod M)
pythonであれば、pow(a, M-2, M)で計算できる

コンビネーションnCkの計算は
nCr = n! * k!^(-1) * (n-k)!^(-1)
"""

N = int(input())

MOD = 10**9+7

f = [0]*(N+1)
f[0] = 1
for n in range(1, N+1):
    f[n] = f[n-1]*n % MOD

finv = [0]*(N+1)
fn = f[N]
fninv = pow(fn, MOD-2, MOD)
finv[N] = fninv
for n in range(N, 0, -1):
    finv[n-1] = finv[n]*n % MOD

def comb(n, k):
    return f[n]*finv[k]*finv[n-k]

for k in range(1, N+1):
    ans = 0
    n = N
    i = 1
    while n >= i:
        ans += comb(n, i)
        i += 1
        n -= k-1
    print(ans % MOD)