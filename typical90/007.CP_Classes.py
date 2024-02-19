N = int(input())
A = sorted([-10**9] + list(map(int, input().split())) + [2*10**9+1])
Q = int(input())

for j in range(Q):
    b = int(input())

    left, right = 0, N + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if A[mid] <= b < A[mid+1]:
            break
        if b < A[mid]:
            right = mid
        elif b >= A[mid+1]:
            left = mid
    
    if abs(b - A[mid]) < abs(A[mid+1] - b):
        print(abs(b-A[mid]))
    else:
        print(abs(A[mid+1] - b))

