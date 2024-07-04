class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def findDiameter(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            queue = deque([0])
            seen = set()
            farthestNode = -1
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node in seen: continue
                    seen.add(node)

                    for nxt in graph[node]:
                        queue.append(nxt)
                        farthestNode = nxt
            
            queue = deque([farthestNode])
            seen.clear()
            longestPath = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node in seen: continue
                    seen.add(node)

                    for nxt in graph[node]:
                        queue.append(nxt)
                if not queue: break
                longestPath += 1
            return longestPath

        diameter1 = findDiameter(edges1)
        diameter2 = findDiameter(edges2)
        return max(diameter1, diameter2, ceil(diameter1/2)+ceil(diameter2/2)+1)