class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x:x[2])

        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False

            if px < py:
                px, py = py, px

            parent[py] = px
            return True

        connected = n
        res = 0
        for u, v, w in edges:
            if connected == k: break
            if union(u, v):
                res = max(res, w)
                connected -= 1
            else:
                res = max(res, w)
        return res
        