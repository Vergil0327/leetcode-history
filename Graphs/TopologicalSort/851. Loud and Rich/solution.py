class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        
        indeg = [0] * n
        graph = defaultdict(list)
        for u, v in richer:
            graph[u].append(v)
            indeg[v] += 1

        queue = deque()
        for node, deg in enumerate(indeg):
            if deg == 0:
                queue.append(node)

        res = list(range(n))
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for nxt in graph[node]:
                    if quiet[res[node]] < quiet[res[nxt]]:
                        res[nxt] = res[node]

                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        queue.append(nxt)
        
        return res
