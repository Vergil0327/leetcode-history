# Intuition

AND這項操作的特性是會越AND越小, 那既然我們要找minimum cost of a walk又不限定如何走
我們可以greedily去想, 我們就將起點跟終點相連的所有vertices都走過一遍, 全都AND再一起得到的值肯定會最小

所以首先想到的就是利用union-find將相連的connected component都AND在一起, 順便計算cost
然後在遍歷query[i]一遍:
- 如果起點跟終點是同一點, cost = 0
- 如果起點跟終點是connected的, 那就返回他們的cost[parent]
- 如果不是connected, 那就返回-1

所以一開始先遍歷edges賦予每個節點cost

```py
cost = [0]*n
for u, v, w in edges:
    cost[u] = w
    cost[v] = w
```

再來把每個相連節點union再一起, 並計算cost

```py
parent = list(range(n))
rank = [1]*n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y, w):
    px, py = find(x), find(y)

    cost[py] &= w
    cost[px] &= w
    
    if px == py: return

    if rank[px] <= rank[py]:
        parent[px] = py
        rank[py] += rank[px]
        cost[py] &= cost[px]
    else:
        parent[py] = px
        rank[px] += rank[py]
        cost[px] &= cost[py]

for u, v, w in edges:
    union(u, v, w)
```

最終在判斷query[i]是三種狀況的哪一種即可

```py
res = []
for u, v in query
    pu, pv = find(u), find(v)

    if u == v:
        res.append(0)
        continue

    if pu == pv:
        res.append(cost[pu])
    else:
        res.append(-1)
return res
```

# Complexity

- time complexity: $O(query.length * alpha(n))$ where *alpha* is extremely slow-growing inverse Ackermann function

- space complexity: $O(n)$