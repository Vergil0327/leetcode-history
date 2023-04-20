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

# Other Solution

後來發現其實一開始的想法，求出整個dp[node1][node2] = cost是可行的
這題其實就是graph theory裡的Floyd algo.

只要沒有negative cycle
透過O(n^3)可以求出整個圖任意兩點間的最短距離

我們一樣定義dp[i][j]為: `the shortest path from i to j`

然後透過三層循環遍歷所有的點
最外層想成是我們要加入的點
裡面兩層則是我們要求的任意兩點間的最短距離
那狀態轉移其實就是這行:

```py
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
```

我們持續加入k這個點來看能不能更優化i到j的最短距離, 那這樣`def shortestPath`就能以O(1時間完成)

初始化則是O(N^3)

那`def addEdge(self, edge: List[int]) -> None:`也跟初始化類似
我們就利用O(N^2)時間來更新新加入的這個edge能不能有所優化