class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in connections:
            pu, pv = find(u), find(v)
            if pu == pv: continue

            if rank[pu] <= rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pv]

        connectedComponents = set()
        for i in range(n):
            connectedComponents.add(find(i))
        return len(connectedComponents)-1