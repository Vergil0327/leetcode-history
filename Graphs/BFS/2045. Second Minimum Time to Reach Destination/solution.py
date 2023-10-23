class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([[0, 1]])

        visited = [0]*(n+1)
        dist = [-inf]*(n+1)
        dist[1] = 0
        visited[1] = 1
        while queue:
            t, node = queue.popleft()

            v, m = divmod(t, change)
            is_green = v%2 == 0
            if is_green:
                t = t+time
            else:
                wait = change - m
                t = t+wait+time

            for nei in graph[node]:
                if visited[nei] < 2 and dist[nei] < t:
                    visited[nei] += 1
                    dist[nei] = t
                    queue.append([t, nei])

                    if nei == n and visited[nei] == 2:
                        return t
        return -1
