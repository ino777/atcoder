"""
計算機では実数が近似的に扱われていることに注意する
整数の世界でなら誤差の影響はないので、logを使わずに大小比較する
"""

a, b, c = map(int, input().split())

ok = a < c**b

if ok:
    print('Yes')
else:
    print('No')
