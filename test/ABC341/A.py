N = int(input())

ans = ''
for i in range(2*N+1):
    ans += '0' if i % 2 == 1 else '1'
print(ans)