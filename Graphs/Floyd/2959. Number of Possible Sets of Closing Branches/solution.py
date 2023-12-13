class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:        
        res = 0
        for state in range(1<<n):
            adj = [[inf]*n for _ in range(n)]
            for i in range(n):
                if (state>>i)&1: continue
                adj[i][i] = 0

            for u, v, w in roads:
                if (state>>u)&1 or (state>>v)&1: continue
                adj[u][v] = min(adj[u][v], w)
                adj[v][u] = min(adj[v][u], w)
                
            for mid in range(n):
                for src in range(n):
                    for dst in range(n):
                        adj[src][dst] = min(adj[src][dst], adj[src][mid]+adj[mid][dst])

            valid = True
            for src in range(n):
                for dst in range(n):
                    if (state>>src)&1 or (state>>dst)&1: continue
                    if adj[src][dst] > maxDistance:
                        valid = False
                        break

                if not valid: break

            res += int(valid)
        return res
