# Intuition

在一棵樹裡, 要計算任意兩點的距離首先想到Binary Lifting + Lowest Common Ancestor (LCA)

計算方式為:
the distance from `u` to `v` = (root to u) + (root to v) - 2 * (root to LCA of u and v)

而LCA可以套用模板:
```py
class LCA:
    def __init__(self, n, edges, root=0):
        self.n = n
        self.log_n = n.bit_length()
        self.depth = [0] * n
        self.up = [[-1] * self.log_n for _ in range(n)]

        # Build adjacency list
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u].append([v, w])
            self.graph[v].append([u, w])

        # Run preprocessing
        self.dfs(root, -1)
        self.build_up_table()

    def dfs(self, node, parent):
        # Set immediate parent (2^0 parent)
        self.up[node][0] = parent

        # Update depth and traverse children
        for child, wei in self.graph[node]:
            if child != parent:
                self.depth[child] = self.depth[node] + wei
                self.dfs(child, node)

    def build_up_table(self):
        # Build binary lifting table
        for j in range(1, self.log_n):
            for i in range(self.n):
                if self.up[i][j-1] != -1:
                    self.up[i][j] = self.up[self.up[i][j-1]][j-1]
    def get_lca(self, a, b):
            # Ensure a is deeper than b
            if self.depth[a] < self.depth[b]:
                a, b = b, a

            # Bring nodes to the same depth
            depth_diff = self.depth[a] - self.depth[b]
            for j in range(self.log_n):
                if depth_diff & (1 << j):
                    a = self.up[a][j]

            # If b was the ancestor of a
            if a == b:
                return a

            # Binary lift both nodes until finding LCA
            for j in range(self.log_n - 1, -1, -1):
                if self.up[a][j] != self.up[b][j]:
                    a = self.up[a][j]
                    b = self.up[b][j]
            return self.up[a][0]  # Return the parent of either node
```

那麼對於任意`u -> v`, 可以快速找出lowest common ancestor

但我們要找的是u到v之間, 第一個accumulated weights 大於等於median的節點`x`
所以不只記錄深度到`self.depth[node]`, 在dfs的同時, 也記錄每個節點的accumulated weight到`self.weight[node]`

而`u -> v`之間的total weight: `Total Path Cost = self.weight[u] + self.weight[v] - 2*self.weight[lca]`

那麼剩下就是透過binary search去找出目標節點x:

1. If costs[u] > costs[v], straightforward binary search between the depths of u and lca to find a node whose cost is greater than or equal to halfCost and move down away from LCA
    - median node會落在[u, lca]

```
lca
| |
x |
| v
|
u
```

2. If costs[u] < costs[v], then find a node from v whose cost is less than or equal to halfCost and move up towards LCA
    - median node會落在[lca, v]

```
lca
| |
u |
  x
  |
  v
```

```py
def get_kth_ancestor(self, node, k):
    for j in range(32):
        if k & (1 << j):
            node = self.up[node][j]
            if node == -1:
                break
    return node
        
def find_between(self, u, lca, halfCost, less):
    low, high = 0, self.depth[u]-self.depth[lca]
    
    ans = u
    
    while low <= high:
        mid = (low + high)//2
        x = self.get_kth_ancestor(u, mid) # median node
        
        if less == 0:
            if self.weight[u] - self.weight[x] >= halfCost:
                ans = x
                high = mid - 1
            else:
                low = mid + 1
        else:
            if self.weight[u] - self.weight[x] <= halfCost:
                ans = x
                low = mid + 1
            else:
                high = mid - 1
        
    return ans

def find_median(self, u, v):
    lca = self.get_lca(u, v)
    totalCost = self.weight[u] + self.weight[v] - 2*self.weight[lca]

    if self.weight[u] == self.weight[v]:
        return lca

    if self.weight[u] > self.weight[v]:
        return self.find_between(u, lca, totalCost / 2, 0)
        
    return self.find_between(v, lca, totalCost / 2, 1)
```