# Intuition

一開始是想到利用bellman-ford來維護一個dp table
以`src`作為出發點，抵達`dest`的最低cost為dp[src][dest]
定義dp[src][dest] = cost
這樣就可以用O(1)時間求出shortest path

所以這樣在新增edge時我們就要更新這個table
當時想法是遍歷每個節點作為出發點, 然後底下就是bellman-ford來更新dp table
但這樣會超時, 因為我們必須遍歷每個node作為起點, 然後再遍歷`n-1`次來更新dp以src作為出發點時的dp table

如下所示
```py
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.dp = dp = [[inf] * n for _ in range(n)]
        self.edges = edges
        
        for i in range(n):
            dp[i][i] = 0
            for _ in range(n-1):
                tmp = []
                for i in range(len(dp)):
                    tmp.append(dp[i].copy())
                
                for u, v, cost in edges:
                    if dp[u][u] != inf:
                        dp[u][v] = min(dp[u][v], tmp[u][u] + cost)
        for i in range(n):
            dp[i] = defaultdict(lambda: inf)
            dp[i][i] = 0

            for _ in range(n):
                tmp = dp[i].copy()
                for u, v, cost in edges:
                    if dp[i][u] != inf:
                        tmp[v] = min(tmp[v], dp[i][u] + cost)
                dp[i] = tmp


    def addEdge(self, edge: List[int]) -> None:
        dp = self.dp
        n = self.n
        edges = self.edges
        edges.append(edge)
        
        for i in range(n):
            for _ in range(n):
                tmp = dp[i].copy()
                for u, v, cost in edges:
                    if dp[i][u] != inf:
                        tmp[v] = min(tmp[v], dp[i][u] + cost)
                dp[i] = tmp
                    

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dp[node1][node2] if self.dp[node1][node2] != inf else -1
        
```

由於此題數據量不大，並且權重 `cost` 為正值, 因此我們可以改用dijkstra來求`shortestPath`
然後在`addEdge`的部分, 用O(1)時間更新adjacency list `graph` 即可

# Complexity

- time complexity

for shortest path:

$O(V + ElogE)$

since edges = V * (V-1) at most, $O(V + ElogE)$ = $O(V + Elog(V^2))$ = $O(V + Elog(V))$