"""
二分探索してくれる便利なライブラリ

bisect.bisect_left
bisect_left(A, b) = b < A[i]となる最小のiを返す
"""

from bisect import bisect_left

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
for _ in range(Q):
    b = int(input())

    j = bisect_left(A, b)
    if j == 0:
        print(abs(b-A[j]))
    elif j < N:
        print(min(abs(b-A[j]), abs(b-A[j-1])))
    elif j == N:
        print(abs(b-A[j-1]))
