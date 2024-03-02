A, B = map(int, input().split())

add = A + B

for n in range(10):
    if n != add:
        print(n)
        break