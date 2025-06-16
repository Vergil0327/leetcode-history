class LCA:
    def __init__(self, n, edges, root=0):
        self.n = n
        self.log_n = n.bit_length()
        self.depth = [0] * n
        self.weight = [0] * n
        self.up = [[-1] * self.log_n for _ in range(n)]

        # Build adjacency list
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u].append([v,w])
            self.graph[v].append([u,w])

        # Run preprocessing
        self.dfs(root, -1, 0)
        self.build_up_table()

    def dfs(self, node, parent, d):
        # Set immediate parent (2^0 parent)
        self.up[node][0] = parent
        self.weight[node] = d

        # Update depth and traverse children
        for child, wei in self.graph[node]:
            if child != parent:
                self.depth[child] = self.depth[node] + 1
                self.dfs(child, node, d+wei)

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
            x = self.get_kth_ancestor(u, mid)
            
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
            

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lca = LCA(n, edges)

        res = []
        for u, v in queries:
            res.append(lca.find_median(u, v))
        return res
