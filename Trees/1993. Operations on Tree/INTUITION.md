# Intuition

we can store `lock` and `lockBy` information of each node in hashmap,
then we can lock/unlcok in O(1) time.

- lock



```py
if vault[node]["lock"]: return False

vault[node]["lock"] = True
vault[node]["lockBy"] = user
```

- unlock

```py
if not lock: return False
if vault[node]["lockBy"] != user: return False

vault[node]["lock"] = False
vault[node]["lockBy"] = -1
```

- upgrade

**if already locked, we can't upgrade**
if vault[node]["lock"]: return

**check ancestors**

if we use a hashmap to store each node's ancestors, then we can traverse hashmap and check every ancestor.

curr = parent[node]
while parent[curr] != -1:
    if vault[curr]["lock"]: return False
    curr = parent[curr]

**check descendant**

if we use 1-indexed to represent node, we can find its descendants by:
- node<<1
- (node<<1)|1

we can use BFS/DFS to explore all the descendants
