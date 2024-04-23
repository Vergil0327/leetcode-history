# Intuition
# root should be center of graph => topological sort to find center 
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        graph = defaultdict(list)
        degrees = [0]*n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        queue = deque()
        for node, deg in enumerate(degrees):
            if deg == 1:
                queue.append(node)

        last = queue.copy()
        seen = set()
        while queue:
            last = queue.copy()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in seen:continue
                seen.add(node)

                for nei in graph[node]:
                    if nei in seen: continue
                    degrees[nei] -= 1
                    if degrees[nei] == 1:
                        queue.append(nei)
        return last
