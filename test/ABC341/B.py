N = int(input())
A = list(map(int, input().split()))
ST = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    count = A[i] // ST[i][0]
    pay = count * ST[i][0]
    acq = count * ST[i][1]
    A[i] -= pay
    A[i+1] += acq
print(A[-1])