N = int(input())
P = list(map(int, input().split()))


Q = int(input())

for _ in range(Q):
    A, B = map(int, input().split())
    ai = P.index(A)
    bi = P.index(B)
    if ai < bi:
        print(A)
    else:
        print(B)
