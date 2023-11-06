class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node, prev):
            cur = values[node]
            subtree = 0
            for nei in graph[node]:
                if nei == prev: continue
                subtree += dfs(nei, node)
            
            return min(cur, subtree) if subtree != 0 else cur
        
        return sum(values) - dfs(0, -1)
