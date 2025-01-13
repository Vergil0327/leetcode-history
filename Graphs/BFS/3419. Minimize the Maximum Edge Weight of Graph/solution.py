class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:            
        graph = defaultdict(lambda: defaultdict(lambda: inf))
        for u, v, w in edges:
            graph[v][u] = min(graph[v][u], w)

        def check(wei):
            queue = deque([0])
            visited = set()

            while queue:
                node = queue.popleft()
                if node in visited: continue
                visited.add(node)

                for nxt in graph[node]:
                    if graph[node][nxt] > wei: continue
                    queue.append(nxt)

            return len(visited) == n

        # search space
        l, r = 1, 1_000_001

        while l < r:
            m = l + (r-l)//2
            if check(m):
                r = m
            else:
                l = m+1
        return l if l < 1_000_001 else -1