# DFS (visited + seen)
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre) # crs -> pre, so the order will be pre -> crs since we use post-order traversal to find order
            
        visited = set()
        seen = set()
        order = [] # it can be reverse order or in order based on how we define the direction for each edge
        def dfs(node):
            if node in seen: return False
            if node in visited: return True
            visited.add(node)
            
            seen.add(node)
            for nei in graph[node]:
                if not dfs(nei): return False
            order.append(node)
            seen.remove(node)
            return True
        
        # it can be incomplete graph with disconnected node, so we need to traversal all the graph to get topological order
        # ex. n = 1 and edges = []
        # for crs, _ in prerequisites: # ! wrong
        for crs in range(n):
            if not dfs(crs): return []
        
        return order

# BFS (queue + indegrees)
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegs = [0] * n
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegs[crs] += 1

        queue = deque()
        for node, deg in enumerate(indegs):
            if deg == 0:
                queue.append(node)

        order = []
        while queue:
            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                order.append(node)

                for nei in graph[node]:
                    indegs[nei] -= 1
                    if indegs[nei] == 0:
                        queue.append(nei)
        return order if len(order) == n else []