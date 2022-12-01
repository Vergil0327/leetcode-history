# Kruskal
class Solution:
    def connectCities(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x:x[2])

        parent = [i for i in range(n+1)] # city from 1 to N
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            parent[py] = px
        
        res = 0
        cnt = 0
        for u, v, cost in connections:
            if find(u) != find(v):
                union(u, v)
                res += cost
                cnt += 1

            if cnt == n-1:
                return res

        return -1
