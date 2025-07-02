# Intuition

invalid conditions:

1. if it is impossible to connect all nodes, return -1.
2. if it has cycle

therefore, we connect all the `must` edges first to check if they has cycle or not

```py
parent = list(range(n))
rank = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py: return False

    if rank[px] < rank[py]:
        px, py = py, px

    parent[py] = px
    rank[px] += rank[py]
    return True

used_edges = 0
res = inf
for u, v, s, must in edges:
    if must:
        if not union(u, v): # has cycle after we connect all the `must` edges
            return -1
        used_edges += 1
        res = min(res, s)
```

after that, let's consider those `not must` edges:

greedily union larger stability edges

```py
edges.sort(key=lambda e: -e[2])
weights = []
for u, v, s, must in edges:
    if must == 0:
        if union(u, v):
            used_edges += 1
            weights.append(s)
```

since we want maximum stability and stablility is the minimum one among all used edges, we should upgrade those smaller stability edges

```py
for i in range(min(k, len(weights))):
    weights[~i] *= 2 # upgrade reversely
```

finally, let's check if we connect all the nodes using `n-1` edges:

```py
if used_edges != n-1: return -1
```

if so, the maximum stability is `min(res, max(weight))`