class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1

        queue = deque()
        for node, deg in enumerate(indeg):
            if deg == 0:
                queue.append(node)

        res = [set() for _ in range(n)]
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for nxt in graph[node]:
                    res[nxt].add(node)
                    res[nxt] |= res[node]

                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        queue.append(nxt)
        return [sorted(SET) for SET in res]
