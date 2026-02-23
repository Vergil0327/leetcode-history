"""
ex. see 3841. Palindromic Path Queries in a Tree

HLD is "templateable" because the core logic of decomposing the tree remains identical regardless of the problem. Only the underlying data structure (the Fenwick Tree or Segment Tree) and the merge logic (XOR, Sum, Max, Min) change.

In a template, you separate the Tree logic (jumping chains) from the Data logic (calculating values).

The "Universal" HLD Template (Python)
This template is structured to be easily adapted. I have separated the update and query logic so you can swap them out.


How to adapt this for different queries

The beauty of HLD is that once query_path is written, you almost never touch it. You only modify the update and query_range functions.

1. To handle "Sum of values on path
- Data Structure: Change the BIT or Segment Tree to handle addition.
- Logic: ```pythonInside query_path:res += self.query_range(...)Inside update:self.bit[idx] += val

2. To handle "Maximum value on path"
- Data Structure: Must use a Segment Tree (Fenwick Trees don't handle max well for range queries).
- Logic:Python# Inside query_path:
res = max(res, self.query_range(...))

3. To handle "Update entire path" (e.g., add 5 to every node from $u$ to $v$)
- Data Structure: Use a Segment Tree with Lazy Propagation.
- Logic: You create a update_path(u, v, val) function that mirrors query_path, but calls seg_tree.range_update instead of seg_tree.query.
"""

class HLD:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.parent = [-1] * n
        self.depth = [0] * n
        self.heavy = [-1] * n
        self.size = [1] * n
        self.head = [0] * n
        self.pos = [0] * n
        self.cur_pos = 0
        
        # 1. First DFS to find sizes and heavy children
        self._dfs_sz(0, -1, 0)
        # 2. Second DFS to decompose into chains
        self._dfs_hld(0, 0)
        
        # 3. The Data Structure (Fenwick Tree here)
        self.bit = [0] * (n + 1)

    def _dfs_sz(self, u, p, d):
        self.parent[u] = p
        self.depth[u] = d
        max_s = 0
        for v in self.adj[u]:
            if v != p:
                sz = self._dfs_sz(v, u, d + 1)
                self.size[u] += sz
                if sz > max_s:
                    max_s = sz
                    self.heavy[u] = v
        return self.size[u]

    def _dfs_hld(self, u, h):
        self.head[u] = h
        self.pos[u] = self.cur_pos
        self.cur_pos += 1
        if self.heavy[u] != -1:
            self._dfs_hld(self.heavy[u], h)
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self._dfs_hld(v, v)

    # --- Data Structure Methods (The "Modular" part) ---
    def update_point(self, u, val):
        idx = self.pos[u] + 1
        while idx <= self.n:
            self.bit[idx] ^= val # Change XOR to + for Sum
            idx += idx & (-idx)

    def _query_bit(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res ^= self.bit[idx] # Change XOR to + for Sum
            idx -= idx & (-idx)
        return res

    def query_range(self, l, r):
        if l > r: l, r = r, l
        return self._query_bit(r) ^ self._query_bit(l - 1)

    # --- HLD Path Traversal (The "Template" logic) ---
    def query_path(self, u, v):
        res = 0
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                res ^= self.query_range(self.pos[self.head[u]], self.pos[u])
                u = self.parent[self.head[u]]
            else:
                res ^= self.query_range(self.pos[self.head[v]], self.pos[v])
                v = self.parent[self.head[v]]
        res ^= self.query_range(self.pos[u], self.pos[v])
        return res
