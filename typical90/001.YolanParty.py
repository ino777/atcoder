# 最小の最大問題は二分探索

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

left, right = 0, L
while left + 1 < right:
    mid = (left + right) // 2
    count = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= mid:
            count += 1
            pre = A[i]
    if L - pre >= mid:
        count += 1

    if count >= K + 1:
        left = mid
    elif count < K + 1:
        right = mid

print(left)