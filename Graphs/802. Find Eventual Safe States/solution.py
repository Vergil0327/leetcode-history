class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        res = []
        cycle = set()

        @lru_cache(None)
        def dfs(node):

            allTermination = True
            for nei in graph[node]:
                if nei in cycle: return False
                cycle.add(nei)
                allTermination = allTermination and dfs(nei)
                cycle.remove(nei)

            if allTermination:
                res.append(node)
            return allTermination

        for node in range(len(graph)):
            cycle.add(node)
            dfs(node)
            cycle.remove(node)
        return sorted(res)
