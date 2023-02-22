from collections import defaultdict, deque
from typing import List

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        distMatrix = [[0]*n for _ in range(n)]
        def dfs(root, node, parent, dist):
            for nei in graph[node]:
                if nei == parent: continue
                distMatrix[root][nei] = dist+1
                dfs(root, nei, node, dist+1)
        for node in range(n):
            dfs(node, node, node, 0)

        res = []
        for start, end, node in query:
            # BFS
            queue = deque([start])
            minDist = float('inf')
            closestNode = None
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if distMatrix[node][curr] < minDist:
                        minDist = distMatrix[node][curr]
                        closestNode = curr
                    if curr == end: break

                    for nei in graph[curr]:
                        if distMatrix[nei][end] + 1 == distMatrix[curr][end]:
                            queue.append(nei)
            res.append(closestNode)
        
        return res
