N = int(input())
A = list(map(int, input().split()))

# 起床時刻までの累計睡眠時間
S = [0]*N
for i in range(len(S)):
    if i == 0:
        S[i] == A[0]
    elif i % 2 == 0:
        S[i] = S[i-1] + A[i] - A[i-1]
    elif i % 2 == 1:
        S[i] = S[i-1]

Q = int(input())
lr = [list(map(int, input().split())) for _ in range(Q)]

for l, r in lr:
    lleft, lright = 0, N-1
    while True:
        lmid = (lleft + lright)//2
        if A[lmid] <= l <= A[lmid+1]:
            break
        if l < A[lmid]:
            lright = lmid
        elif l > A[lmid]:
            lleft = lmid
    rleft, rright = 0, N-1
    while True:
        rmid = (rleft + rright)//2
        if A[rmid] <= r <= A[rmid+1]:
            break
        if r < A[rmid]:
            rright = rmid
        elif r > A[rmid]:
            rleft = rmid

    if lmid % 2 == 0 and rmid % 2 == 0:
        print(S[rmid] - S[lmid])
    elif lmid % 2 == 0 and rmid % 2 == 1:
        print(S[rmid] - S[lmid] + (r - A[rmid]))
    elif lmid % 2 == 1 and rmid % 2 == 0:
        print(S[rmid] - S[lmid+1] + (A[lmid+1] - l))
    elif lmid % 2 == 1 and rmid % 2 == 1:
        print(S[rmid] - S[lmid+1] + (A[lmid+1] - l) + (r - A[rmid]))


