W, H = map(int, input().split())
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
# 0, a1, a2, ..., aA
a_list = [0] + list(map(int, input().split())) + [W]
B = int(input())
# 0, b1, b2, ...., bB
b_list = [0] + list(map(int, input().split())) + [H]
# 444 444

# ゼロではない区画(a, b)
not_zero = set()

# dict[(a, b)] = count
table = {}

for point in points:
    p, q = point
    # 二分探索でp, qがどこの区画にいるかを求める
    i_left, i_right = 0, A
    while i_left <= i_right:
        i = i_left + (i_right - i_left) // 2
        if a_list[i] < p < a_list[i+1]:
            break
        elif p < a_list[i]:
            i_right = i - 1
            continue
        elif a_list[i+1] < p:
            i_left = i + 1
            continue
    j_left, j_right = 0, B
    while j_left <= j_right:
        j = j_left + (j_right - j_left) // 2
        if b_list[j] < q < b_list[j+1]:
            break
        elif q < b_list[j]:
            j_right = j - 1
            continue
        elif b_list[j+1] < q:
            j_left = j + 1
            continue
    a, b = a_list[i], b_list[j]
    table[(a, b)] = table[(a, b)] + 1 if table.get((a, b)) else 1
    not_zero.add((a, b))

min_count = min(table.values()) if len(not_zero) == (A+1)*(B+1) else 0
max_count = max(table.values())
print(min_count, max_count)
