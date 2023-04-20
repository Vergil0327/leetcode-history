class Graph:

    def __init__(self, n: int, edges: List[List[int]]):        
        self.graph = graph = defaultdict(list)
        for u, v, c in edges:
            graph[u].append([v, c])


    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])
                    

    def shortestPath(self, node1: int, node2: int) -> int:
        minH = [[0, node1]]
        graph = self.graph
        
        visited = set()
        while minH:
            cost, curr = heapq.heappop(minH)
            if curr == node2: return cost
            
            if curr in visited: continue
            visited.add(curr)
            
            for nei, c in graph[curr]:
                heapq.heappush(minH, [cost+c, nei])
        return -1

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n

        self.dp = dp = [[inf]*n for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i] = 0

        for u, v, cost in edges:
            dp[u][v] = cost

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    def addEdge(self, edge: List[int]) -> None:
        dp = self.dp
        for i in range(self.n):
            for j in range(self.n):
                u, v, cost = edge
                dp[i][j] = min(dp[i][j], dp[i][u] + cost + dp[v][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.dp[node1][node2] == inf: return -1
        return self.dp[node1][node2]