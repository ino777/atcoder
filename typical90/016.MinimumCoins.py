"""
全探索 10^8オーダー
CPythonよりPyPyのほうが早いことがあるので、このように全探索でO(10^8)で解けそうならPyPyにして試すべし!
"""
N = int(input())
A, B, C = sorted(map(int, input().split()), reverse=True)

max_num = 9999

ans = max_num
for x in range(max_num+1):
    max_y = (N-A*x)//B
    for y in range(max_y+1):
        tmp = A*x + B*y
        if (N-tmp) % C != 0 or tmp > N:
            continue
        z = (N-tmp)//C
        ans = min(ans, x+y+z)
print(ans)