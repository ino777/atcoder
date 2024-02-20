"""
グラフ上の2点が連結しているかを問う問題は、Union-Findを使う!
"""

H, W = map(int, input().split())
Q = int(input())


class DSU:
    def __init__(self, n):
        self._n = n
        # n+1なら白
        # 負なら自身がリーダーで、絶対値がサイズを表す
        # 正なら親のa
        self.parent_or_size = [n+1]*n
    
    def add(self, a):
        self.parent_or_size[a] = -1

    def leader(self, a):
        if self.parent_or_size[a] < 0:
            return a
        return self.leader(self.parent_or_size[a])
    
    def merge(self, a, b):
        if self.parent_or_size[a] == self._n+1 or self.parent_or_size[b] == self._n+1:
            return
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return
        if x > y:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
    
    def verify(self, a, b):
        if self.parent_or_size[a] == self._n+1 or self.parent_or_size[b] == self._n+1:
            return False
        x = self.leader(a)
        y = self.leader(b)
        return x == y


dsu = DSU(H*W)

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = q[1]-1, q[2]-1
        a = r*W+c
        dsu.add(a)

        if r >= 1:
            up = (r-1)*W+c
            dsu.merge(a, up)
        if r <= H-2:
            down = (r+1)*W+c
            dsu.merge(a, down)
        if c >= 1:
            left = r*W+c-1
            dsu.merge(a, left)
        if c <= W-2:
            right = r*W+c+1
            dsu.merge(a, right)

    elif q[0] == 2:
        ra, ca, rb, cb = q[1]-1, q[2]-1, q[3]-1, q[4]-1
        a = ra*W+ca
        b = rb*W+cb
        ok = dsu.verify(a, b)
        if ok:
            print('Yes')
        else:
            print('No')