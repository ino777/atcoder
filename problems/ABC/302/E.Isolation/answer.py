N, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

vertex = {}
for i in range(1,N+1):
   vertex[i] = {}

count = N
for q in query:
    order = q[0]
    if order == 1:
        u, v = q[1], q[2]
        if len(vertex[u]) == 0 and len(vertex[v]) == 0:
            # u, v両方孤独頂点なら-2
            count -= 2
        elif len(vertex[u]) != 0 and len(vertex[v]) != 0:
            # u, v両方孤独頂点でなければ増減なし
            pass
        else:
            # u,v片方が孤独頂点でなければ-1
            count -= 1
        vertex[u][v] = True
        vertex[v][u] = True

    else:
        v = q[1]
        us = vertex[v].keys()
        for u in us:
            del vertex[u][v]
        vertex[v] = {}
        if len(us) != 0:
            # vが孤独頂点になるので+1
            count += 1
        # usの中で辺削除後に孤独頂点にになる分+
        for u in us:
            if len(vertex[u]) == 0:
                count += 1
            
    print(count)

