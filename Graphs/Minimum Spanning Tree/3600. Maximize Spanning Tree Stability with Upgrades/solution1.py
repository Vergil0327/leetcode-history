class Solution:
    def maxStability(self, n, edges, k):
        # union-find
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

        # Kruskal (spanning tree algorithm)
        used_edges = 0
        res = inf
        for u, v, s, must in edges:
            if must:
                if not union(u, v): # has cycle after we connect all the `must` edges
                    return -1
                used_edges += 1
                res = min(res, s)
        
        edges.sort(key=lambda e: -e[2])
        weights = []
        for u, v, s, must in edges:
            if must == 0:
                if union(u, v):
                    used_edges += 1
                    weights.append(s)

        for i in range(min(k, len(weights))):
            weights[~i] *= 2

        if used_edges != n - 1:
            return -1
        return min((res, *weights))
