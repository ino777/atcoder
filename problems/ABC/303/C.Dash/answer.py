N, M, H, K = map(int, input().split())
S = input()
items = [list(map(int, input().split())) for _ in range(M)]

def gen_key(x, y):
    return f'{x}_{y}'

item_table = {}
for item in items:
    key = gen_key(*item)
    item_table[key] = item


# 座標(x, y)
pos = [0, 0]
# 体力
hp = H

ok = True

for c in S:
    hp -= 1
    if c == 'R':
        pos[0] += 1
    elif c == 'L':
        pos[0] -= 1
    elif c == 'U':
        pos[1] += 1
    else:
        pos[1] -= 1
    
    if hp < 0:
        ok = False
        break

    key = gen_key(*pos)
    if item_table.get(key) and hp < K:
        del item_table[key]
        hp = K

if ok:
    print('Yes')
else:
    print('No')