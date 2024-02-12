N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

max_s = -1

while True:
    if len(A)*len(B) == 0:
        break
    max_a = A[-1]
    max_b = B[-1]

    if abs(max_a - max_b) <= D:
        max_s = max_a+max_b
        break
    
    if max_a > max_b:
        A.pop()
    else:
        B.pop()

print(max_s)