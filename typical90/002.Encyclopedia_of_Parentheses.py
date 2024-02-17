N = int(input())

memo = {}

def f(n):
    if n % 2 == 1:
        return set()
    if n == 2:
        return set(['()'])
    result = set()

    # ( f(n-2) )
    fn_2 = memo[n-2] if memo.get(n-2) else f(n-2)
    for s in fn_2:
        result.add('(' + s +')')

    # f(i) + f(n-i), f(n-i) + f(i)
    i = n - 2
    while i >= n//2:
        f_i = memo[i] if memo.get(i) else f(i)
        f_n_i = memo[n-i] if memo.get(n-i) else f(n-i)
        for s1 in f_i:
            for s2 in f_n_i:
                result.add(s1 + s2)
                result.add(s2 + s1)
        i -= 2
    memo[n] = result
    return result

ans = f(N)
ans = sorted(list(ans))
for s in ans:
    print(s)
