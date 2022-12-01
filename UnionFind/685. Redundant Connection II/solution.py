class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        
        candidates = []
        for u, v in edges:
            if parent[v] != v:
                candidates.append([u, v])
                candidates.append([parent[v], v])
                break
            else:
                parent[v] = u
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return False
            
            parent[pv] = pu
            return True

        if not candidates:
            parent = [i for i in range(n+1)]
            for u, v in edges:
                if find(u) != find(v):
                    union(u, v)
                else:
                    return [u, v]
        else:
            parent = [i for i in range(n+1)]
            for u, v in edges:
                if (u,v) == tuple(candidates[0]): # try remove candidates[0]
                    continue
                if find(u) != find(v):
                    union(u, v)
                else:
                    return candidates[1]
            return candidates[0]