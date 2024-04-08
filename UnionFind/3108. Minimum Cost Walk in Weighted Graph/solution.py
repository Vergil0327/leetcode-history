class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        cost = [0]*n
        for u, v, w in edges:
            cost[u] = w
            cost[v] = w

        parent = list(range(n))
        rank = [1]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y, w):
            px, py = find(x), find(y)

            cost[py] &= w
            cost[px] &= w
            
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
                cost[py] &= cost[px]
            else:
                parent[py] = px
                rank[px] += rank[py]
                cost[px] &= cost[py]

        for u, v, w in edges:
            union(u, v, w)

        res = []
        for u, v in query:
            pu, pv = find(u), find(v)

            if u == v:
                res.append(0)
                continue

            if pu == pv:
                res.append(cost[pu])
            else:
                res.append(-1)
        return res
