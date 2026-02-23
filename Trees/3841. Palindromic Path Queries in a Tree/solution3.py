import sys
# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class HLD:
    def __init__(self, n, adj, initial_s):
        self.n = n
        self.adj = adj
        self.parent = [-1] * n
        self.depth = [0] * n
        self.heavy = [-1] * n
        self.size = [1] * n
        self.head = [0] * n
        self.pos = [0] * n
        self.cur_pos = 0
        
        # Pre-calculate tree structure
        self._dfs_sz(0, -1, 0)
        self._dfs_hld(0, 0)
        
        # Bitmask storage
        self.current_masks = [(1 << (ord(c) - ord('a'))) for c in initial_s]
        self.bit = [0] * (n + 1)
        
        # Initialize Fenwick Tree with starting characters
        for i in range(n):
            self._update_bit(self.pos[i], self.current_masks[i])

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

    def _update_bit(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] ^= val
            idx += idx & (-idx)

    def _query_bit(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res ^= self.bit[idx]
            idx -= idx & (-idx)
        return res

    def update_node(self, u, char):
        new_mask = 1 << (ord(char) - ord('a'))
        # XOR with old mask to remove it, XOR with new mask to add it
        diff = self.current_masks[u] ^ new_mask
        self._update_bit(self.pos[u], diff)
        self.current_masks[u] = new_mask

    def query_path(self, u, v):
        res_mask = 0
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                # Query the range from head of chain to current node
                l, r = self.pos[self.head[u]], self.pos[u]
                res_mask ^= self._query_bit(r) ^ self._query_bit(l - 1)
                u = self.parent[self.head[u]]
            else:
                l, r = self.pos[self.head[v]], self.pos[v]
                res_mask ^= self._query_bit(r) ^ self._query_bit(l - 1)
                v = self.parent[self.head[v]]
        
        # Last segment when they are on the same chain
        l, r = sorted([self.pos[u], self.pos[v]])
        res_mask ^= self._query_bit(r) ^ self._query_bit(l - 1)
        
        # Palindrome check: at most one bit set
        return (res_mask & (res_mask - 1)) == 0

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        hld = HLD(n, adj, s)
        results = []
        
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                hld.update_node(int(parts[1]), parts[2])
            else:
                results.append(hld.query_path(int(parts[1]), int(parts[2])))
                
        return results