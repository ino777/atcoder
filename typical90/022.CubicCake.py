A, B, C = map(int, input().split())
A, B, C = sorted([A, B, C])


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)

g = gcd(A, gcd(B, C))

print(A//g-1 + B//g-1 + C//g-1)