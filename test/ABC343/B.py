N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for row in A:
    line = []
    for i, c in enumerate(row):
        if c == 1:
            line.append(i+1)
    print(' '.join(map(str, line)))
