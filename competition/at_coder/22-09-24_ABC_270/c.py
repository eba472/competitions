n, x, y = [int(s) for s in input().split()]

edges = {}
for _ in range(1, n):
    i, j = [int(s) for s in input().split()]

    if i in edges:
        edges[i].append(j)
    else:
        edges[i] = [j]

    if j in edges:
        edges[j].append(i)
    else:
        edges[j] = [i]


def find(n, x, y, edges):
    bfs = [(x, [x], -1)]
    while bfs:
        curr, curr_path, parent = bfs.pop()
        for p in edges[curr]:
            if p != parent:
                if p == y:
                    return curr_path + [p]
                bfs.append((p, curr_path + [p], curr))


res = find(n, x, y, edges)
print(" ".join([str(i) for i in res]))
