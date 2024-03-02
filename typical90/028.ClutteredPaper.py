"""
二次元いもす法
長方形領域に+1の加算をする方法

- ステップ1
(lx, ly), (rx, ry)に+1
(lx, ry), (lx, ry)に-1

0  0  0  0  0  0  0
0 -1  0  0  0  1  0
0  0  0  0  0  0  0
0  1  0  0  0 -1  0
0  0  0  0  0  0  0

- ステップ2
横方向に累積和をとる

0  0  0  0  0  0  0
0 -1 -1 -1 -1  0  0
0  0  0  0  0  0  0
0  1  1  1  1  0  0
0  0  0  0  0  0  0

- ステップ3
縦方向に累積和をとる

0  0  0  0  0  0  0
0  0  0  0  0  0  0
0  1  1  1  1  0  0
0  1  1  1  1  0  0
0  0  0  0  0  0  0

"""
N = int(input())

MAX_X = 1000
MAX_Y = 1000

g = [[0]*(MAX_X+1) for _ in range(MAX_Y+1)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())

    g[ly][lx] += 1
    g[ry][rx] += 1
    g[ry][lx] += -1
    g[ly][rx] += -1


# 横方向に累積和
for y in range(MAX_Y+1):
    for x in range(MAX_X):
        g[y][x+1] += g[y][x]

# 縦方向に累積和
for x in range(MAX_X+1):
    for y in range(MAX_Y):
        g[y+1][x] += g[y][x]

A = [0]*(N+1)
for row in g:
    for c in row:
        A[c] += 1



for k in range(1, N+1):
    print(A[k])