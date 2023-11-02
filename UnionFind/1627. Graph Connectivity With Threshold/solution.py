class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def connected(x, y):
            return find(x) == find(y)

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        for city in range(1, n+1):
            if city > threshold:
                for i in range(2, n//city+1):
                    union(city, city*i)
            
        res = []
        for x, y in queries:
            if connected(x, y):
                res.append(True)
            else:
                res.append(False)
        return res
