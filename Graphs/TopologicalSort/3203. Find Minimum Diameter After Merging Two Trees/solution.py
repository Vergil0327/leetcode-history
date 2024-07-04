class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def topologicalSort(edges) -> int:
            """
            return distance from leaf to center node
            """
            n = len(edges)
            graph = defaultdict(list)
            indeg = [0] * (n+1)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                indeg[u] += 1
                indeg[v] += 1

            queue = deque()
            for node, deg in enumerate(indeg):
                if deg == 1: # leaf
                    queue.append([0, node])

            longest1 =longest2 = 0 
            seen = set()
            dist = defaultdict(int)
            while queue:
                lastRound = (len(seen) == n+1-2) or (len(seen) == n+1-1)
                if lastRound:
                    for _ in range(len(queue)):
                        d, node = queue.popleft()
                        if node in seen: continue
                        if d > longest1:
                            longest2 = longest1
                            longest1 = d
                        elif d > longest2:
                            longest2 = d

                        dist[node] = d
                    break

                for _ in range(len(queue)):
                    d, node = queue.popleft()
                    if node in seen: continue
                    seen.add(node)

                    for nxt in graph[node]:
                        indeg[nxt] -= 1
                        if indeg[nxt] <= 1:
                            queue.append([d+1, nxt])

            if not dist: return 0, 0

            if len(dist) == 1:
                return list(dist.values())[0], longest1+longest2
            else:
                distances = list(dist.values())
                return max(distances)+1, longest1+longest2+1

        d1, diameter1 = topologicalSort(edges1)
        d2, diameter2 = topologicalSort(edges2)

        return max(diameter1, diameter2, d1 + d2 + 1)