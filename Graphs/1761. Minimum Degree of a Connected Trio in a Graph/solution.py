class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        indegrees = [0]*(n+1)
        for u, v in edges:
            indegrees[u] += 1
            indegrees[v] += 1
            graph[u].add(v)
            graph[v].add(u)

        res = inf
        for u, v in edges:
            cur = indegrees[u]+indegrees[v]-6
            for node in range(1, n+1):
                if node in graph[u] and node in graph[v]:
                    res = min(res, cur+indegrees[node])
        return res if res != inf else -1

# Optimization
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        indegrees = [0]*(n+1)
        for u, v in edges:
            indegrees[u] += 1
            indegrees[v] += 1
            graph[u].add(v)
            graph[v].add(u)

        nodes = sorted([deg, node] for node, deg in enumerate(indegrees))

        res = inf
        for u, v in edges:
            cur = indegrees[u]+indegrees[v]-6
            for _, node in nodes:
                if node in graph[u] and node in graph[v]:
                    res = min(res, cur+indegrees[node])
                    break
        return res if res != inf else -1
