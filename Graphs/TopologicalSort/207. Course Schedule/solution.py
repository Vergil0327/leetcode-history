# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
            
        visited = set()
        seen = set()
        def dfs(node):
            if node in seen: return False
            if node in visited: return True
            visited.add(node)
            
            seen.add(node)
            for nei in graph[node]:
                if not dfs(nei): return False
            seen.remove(node)
            
            return True
        
        for src, _ in prerequisites:
            if not dfs(src): return False
        return True

# BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
            
        queue = deque()
        for node, deg in enumerate(indegrees):
            if deg == 0:
                queue.append(node)
                
        order = []
        while queue:
            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                
                order.append(node)   
                for nei in graph[node]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 0:
                        queue.append(nei)

        return len(order) == numCourses