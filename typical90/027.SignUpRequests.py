N = int(input())

d = {}
for i in range(1, N+1):
    S = input()
    if d.get(S) is None:
        print(i)
    d[S] = True
