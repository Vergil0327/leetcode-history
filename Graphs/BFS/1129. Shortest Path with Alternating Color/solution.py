class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append([v, RED])
        for u, v in blueEdges:
            graph[u].append([v, BLUE])

        res = [inf] * n
        res[0] = 0

        queue = deque([(0, RED), (0, BLUE)])
        visited = set([(0, RED), (0, BLUE)])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                curr, color = queue.popleft()
                res[curr] = min(res[curr], steps)

                for nei, edgeColor in graph[curr]:
                    if edgeColor == color: continue
                    if (nei, 1-color) in visited: continue
                    visited.add((nei, 1-color))
                    queue.append((nei, 1-color))
            steps += 1
        
        return [dist if dist != inf else -1 for dist in res]