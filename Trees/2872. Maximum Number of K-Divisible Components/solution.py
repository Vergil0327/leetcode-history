class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        for i in range(n):
            values[i] %= k
        
        @cache
        def dfs(node, prev):
            cur = values[node]
            split = 0
            for nei in graph[node]:
                if nei == prev: continue
                tot, cnt = dfs(nei, node)
                cur += tot
                split += cnt
                
            cur %= k
            if cur == 0:
                split += 1
            
            return cur, split            
        _, res = dfs(0, -1)
        return res
    
