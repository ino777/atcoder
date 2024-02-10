import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

box = {}
for i in range(N):
    box[i] = A[i]

for i in range(M):
    C = 0
    b_i = B[i]
    tmp = box[b_i]
    box[b_i] = 0

    x, y = math.floor(tmp/N), math.ceil(tmp/N)
    z = tmp % N
    for c in range(1, N+1):
        next_i = (b_i + c) % N
        if c <= z:
            box[next_i] += y
        else:
            if x == 0:
                break
            box[next_i] += x
        
print(" ".join(map(str, box.values())))