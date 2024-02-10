import math

N = int(input())

kokuban = {}
kokuban[N] = 1

cost = 0
while len(kokuban) > 0:
    x = list(kokuban.keys())[0]
    count = kokuban[x]
    del kokuban[x]
    a, b = math.floor(x/2), math.ceil(x/2)
    if a >= 2:
        kokuban[a] = kokuban[a] + count if kokuban.get(a) else count
    if b >= 2:
        kokuban[b] = kokuban[b] + count if kokuban.get(b) else count
    cost += x*count

print(cost)

