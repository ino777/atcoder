H, W = map(int, input().split())

A=[list(map(int, input().split())) for _ in range(H)]

columns = []
for j in range(W):
    columns.append(sum([A[i][j] for i in range(H)]))


for i in range(H):
    rowsum = sum(A[i])
    print(" ".join(map(str, [rowsum+columns[j]-A[i][j] for j in range(W)])))