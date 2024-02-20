N = int(input())

one = [0]*(N+1)
two = [0]*(N+1)

for i in range(1, N+1):
    c, p = map(int, input().split())
    one[i] += one[i-1]
    two[i] += two[i-1]
    if c == 1:
        one[i] += p
    elif c == 2:
        two[i] += p

Q = int(input())

for j in range(Q):
    l, r = map(int,input().split())
    print(one[r] - one[l-1], two[r] - two[l-1])

