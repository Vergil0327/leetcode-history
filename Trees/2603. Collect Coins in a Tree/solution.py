class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        graph = defaultdict(set)
        indegree = [0] * n
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            indegree[u] += 1
            indegree[v] += 1

        for node in range(n):
            while indegree[node] == 1 and coins[node] == 0:
                indegree[node] = 0

                parent = graph[node].pop()
                graph[parent].remove(node)
                indegree[parent] -= 1
                node = parent

        queue = deque()
        for node in range(n):
            if indegree[node] == 1:
                queue.append(node)

        step = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                indegree[node] = 0

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        graph[nei].remove(node)
                        queue.append(nei)
            step += 1
            if step == 2: break
        
        requiredNodes = [node for node, deg in enumerate(indegree) if deg >= 1]
        if len(requiredNodes) <= 1: return 0
        return (len(requiredNodes)-1) * 2