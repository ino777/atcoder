def is_valid(i, j, S, T):
    # 不時着地点の判定
    if S[i][j] == '#':
        return False
    # 移動経路上の判定
    for c in T:
        if c == 'L':
            j -= 1
        elif c == 'R':
            j += 1
        elif c == 'U':
            i -= 1
        elif c == 'D':
            i += 1
        if S[i][j] == '#':
            return False
    return True

def main():
    H, W, N = map(int, input().split())
    T = input()
    S = [input() for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if is_valid(i, j, S, T):
                count += 1
    print(count)
print(main())
