# slow
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n==1 and not graph[0]: return 0
        
        def BFS(start):
            queue = deque([(start, 1<<start)]) # node, visited_state
            length = 1
            visited = set()
            while queue:
                for _ in range(len(queue)):
                    node, state = queue.popleft()
                    if (node, state) in visited: continue
                    visited.add((node, state))
                    for nei in graph[node]:
                        nxt = state | (1<<nei)
                        if nxt == ((1<<n)-1): return length
                        queue.append((nei, nxt))
                length += 1
            return length

        return min(BFS(node) for node in range(n))

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n==1 and not graph[0]: return 0 # empty graph

        queue = deque() # node, visited_state
        for i in range(n):
            queue.append((i, 1<<i))

        length = 1
        visited = set()
        while queue:
            for _ in range(len(queue)):
                node, state = queue.popleft()
                if (node, state) in visited: continue
                visited.add((node, state))

                for nei in graph[node]:
                    nxt = state | (1<<nei)
                    if nxt == ((1<<n)-1): return length
                    queue.append((nei, nxt))
            length += 1
        return length