class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def countPairs(n):
            return n * (n-1) // 2

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv: continue

            if rank[pu] <= rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pu]
        
        groups = set()
        for i in range(n):
            groups.add(find(i))

        return countPairs(n) - sum(countPairs(rank[group]) for group in groups)