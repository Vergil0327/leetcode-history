class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Union-Find
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        for i, q in enumerate(queries):
            q.append(i)
        q = sorted(queries, key=lambda x:x[2])
        edgeList.sort(key=lambda x:x[2])

        res = [False] * len(queries)
        i = 0
        for u, v, limit, idx in q:
            while i < len(edgeList) and edgeList[i][2] < limit:
                a, b = edgeList[i][0], edgeList[i][1]
                union(a, b)
                i += 1

            pu, pv = find(u), find(v)
            if pu == pv:
                res[idx] = True
        return res