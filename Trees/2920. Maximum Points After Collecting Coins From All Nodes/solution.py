class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # coins[i] <= 10000
        MX = ceil(log2(10000))
        
        @cache
        def dfs(node, prev, t):
            if t >= MX: return 0
            cur = coins[node] >> t
            

            op1 = cur-k
            for nei in graph[node]:
                if nei == prev: continue
                op1 += dfs(nei, node, t)

            op2 = cur >> 1
            for nei in graph[node]:
                if nei == prev: continue
                op2 += dfs(nei, node, t+1)
            return max(op1, op2)
        return dfs(0, -1, 0)