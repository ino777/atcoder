N, M = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
xy = [list(map(int, input().split())) for _ in range(K)]
Q = int(input())
pq = [list(map(int, input().split())) for _ in range(Q)]

class DSU:
    def __init__(self, n):
        self._n = N
        # < 0 なら自身がリーダーでありグループのサイズを表す
        # <= 0 ならリーダーを表す
        # 最初はすべての要素がリーダーであり、グループのサイズが1
        self.parent_or_size = [-1]*n
    
    def leader(self, a):
        if self.parent_or_size[a] < 0:
            return a
        return self.leader(self.parent_or_size[a])
    
    def merge(self, a, b):
        al, bl = self.leader(a), self.leader(b)
        if al == bl:
            return al
        if al > bl:
            al, bl = bl, al
        self.parent_or_size[al] += self.parent_or_size[bl]
        self.parent_or_size[bl] = al
        return al

    def size(self, a):
        if self.parent_or_size[a] < 0:
            return - self.parent_or_size[a]
        return self.size(self.leader(a))
    

dsu = DSU(N)
for u, v in uv:
    dsu.merge(u-1, v-1)

pairs = set()
for x, y in xy:
    xl, yl = dsu.leader(x-1), dsu.leader(y-1)
    pairs.add((min(xl, yl), max(xl, yl)))

for p, q in pq:
    pl, ql = dsu.leader(p-1), dsu.leader(q-1)
    if (min(pl, ql), max(pl, ql)) in pairs:
        print('No')
    else:
        print('Yes')