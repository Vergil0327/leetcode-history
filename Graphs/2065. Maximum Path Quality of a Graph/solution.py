class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(set)
        n = len(values)
        times = [[0] * n for _ in range(n)]
        for u, v, t in edges:
            graph[u].add(v)
            graph[v].add(u)
            times[u][v] = times[v][u] = t

        queue = deque([[0,0]])
        visited = set()
        while queue:
            node, curT = queue.popleft()
            if node in visited: continue
            visited.add(node)
            for nei in graph[node]:
                if (t := curT + 2*times[node][nei]) <= maxTime:
                    queue.append([nei, t])

        for node in range(n):
            if node not in visited:
                for nei in graph[node]:
                    graph[nei].remove(node)
                del graph[node]
        
        ROOT = 0
        def dfs(node, visited, time):
            cur = sum(values[node] for node in visited) if node == ROOT else 0

            for nei in graph[node]:
                if time >= times[node][nei]:
                    cur = max(cur, dfs(nei, visited | {nei}, time - times[node][nei]))
            return cur

        return dfs(ROOT, {ROOT}, maxTime)
