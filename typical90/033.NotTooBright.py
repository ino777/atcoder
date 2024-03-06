H, W = map(int, input().split())

if H == 1 and W == 1:
    ans = 1
elif H == 1:
    ans = W
elif W == 1:
    ans = H
else:
    ans = ((H+1)//2) * ((W+1)//2)

print(ans)