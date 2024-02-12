import itertools

N, M = map(int, input().split())
S = [input() for _ in range(N)]

def diff_one(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1
    return count == 1

def main():
    for T in itertools.permutations(S):
        for i in range(N-1):
            if not diff_one(T[i+1], T[i]):
                break
            if i == N-2:
                print('Yes')
                return
    print('No')
main()