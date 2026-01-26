class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def BFS(node):
            queue = deque([node])
            dist = [-1] * n
            dist[node] = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for nxt in graph[node]:
                        if dist[nxt] == -1:
                            dist[nxt] = dist[node] + 1
                            queue.append(nxt)
            return dist
        dist_x = BFS(x)
        dist_y = BFS(y)
        dist_z = BFS(z)

        res = 0
        for node in range(n):
            dx, dy, dz = dist_x[node], dist_y[node], dist_z[node]

            mx = max(dx, dy, dz)

            # dx^2 + dy^2 = dz^2
            # dx^2 + dy^2 + dz^2 = dz^2 + dz^2
            if dx**2 + dy**2 + dz**2 == 2 * mx**2:
                res += 1
        return res

        