Q = int(input())

queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

A = []

for query in queries:
    if query[0] == 1:
        A.append(query[1])
    else:
        print(A[(-1)*query[1]])
