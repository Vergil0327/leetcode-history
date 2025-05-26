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
    
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        
        lca = LCA(n+1, edges, 1)
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n+1)
        def dfs(node, prev, depth):
            for nxt in graph[node]:
                if nxt != prev:
                    depth[nxt] = depth[node] + 1
                    dfs(nxt, node, depth)
        dfs(1, -1, depth)


        res = []
        for u, v in queries:
            if u == v:
                res.append(0)
                continue
            depth_lca = depth[lca.get_lca(u, v)]
            path = depth[u]-depth_lca + depth[v]-depth_lca
            res.append(pow(2, path-1, 1000000007))
        return res