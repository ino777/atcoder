N = int(input())

def is_valid(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

for bit in range((1<<N)):
    S = ''

    for i in range(N-1, -1, -1):
        if not (bit & 1<<i):
            S += '('
        else:
            S += ')'

    if is_valid(S):
        print(S)
