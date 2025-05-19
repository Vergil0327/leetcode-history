"""
Binary Lifting for Lowest Common Ancestor (LCA)
Binary lifting is an efficient technique to find the lowest common ancestor (LCA) of two nodes in a tree with O(log n) query time after O(n log n) preprocessing. Here's how to implement it:

The Approach

Precompute an "up table" where up[node][j] represents the 2^j-th ancestor of node
Use this table to efficiently "binary jump" up the tree when finding the LCA

Implementation Steps

Preprocessing:

Calculate the depth of each node
Build the binary lifting table up[node][j]


LCA Query:

Ensure both nodes are at the same depth by moving the deeper node upward
Binary jump both nodes upward together until finding their LCA



Let me provide a detailed implementation in Python::
"""

class LCA:
    def __init__(self, n, edges, root=0):
        self.n = n
        self.log_n = n.bit_length()
        self.depth = [0] * n
        self.up = [[-1] * self.log_n for _ in range(n)]
        
        # Build adjacency list
        self.graph = [[] for _ in range(n)]
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        # Run preprocessing
        self.dfs(root, -1)
        self.build_up_table()
    
    def dfs(self, node, parent):
        # Set immediate parent (2^0 parent)
        self.up[node][0] = parent
        
        # Update depth and traverse children
        for child in self.graph[node]:
            if child != parent:
                self.depth[child] = self.depth[node] + 1
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