# Intuition - Dijkstra algorithm

[explain by @HuifengGuan](https://www.youtube.com/live/xUijWmULpzA?si=miqlPaPmV1tZhSDq)

如果火抵達(m-1,n-1)需要`t`天, 那我們反向往回推
想法是我們人從(m-1, n-1)終點往回走到(0,0)

這樣往回走的過程中, 下個位置我們最晚抵達天數至少為`t-1`天, 這樣才能在第`t`天抵達現在位置
但別忘了, 我們抵達往回走的下個位置時, 也必須比火還早到
所以例如:我們從(m-1,n-1)走回(m-2, n-1)時, 最晚除了可以是`t-1`天以外, 也必須比`fire[m-2][n-1]`還早
所以這時抵達(m-2, n-1)的權重為**min(t-1, fire[m-2][n-1]-1)**, 代表我們最晚必須在`min(t-1, fire[m-2][n-1]-1)`這時候抵達

等到我們一路回推到(0,0)時, 就知道我們最晚出發的時間`t`是多少了

因此在反推回去的時候, 我們其實是在求每條邊有不同權重的最短路徑 => Dijkstra
而我們的目標是能等待越久再出發越好, 所以是BFS + max heap的dijkstra

核心代碼如下:

```py
visited = [[0]*n for _ in range(m)]
maxHeap = [[-fire[m-1][n-1], m-1, n-1]] # priorty queue[i] = [t,row,col]: the last day `t` to reach (row,col)

while maxHeap:
    t, r, c = heapq.heappop(maxHeap)
    if visited[r][c]: continue
    visited[r][c] = 1
    if r == 0 and c == 0: return -t

    for dr, dc in dirs:
        row, col = r+dr, c+dc
        if row<0 or row >= m or col < 0 or col >= n: continue
        if grid[row][col] == 2: continue # wall
        if visited[row][col]: continue # visited
        
        heapq.heappush(maxHeap, [-min(-t-1, fire[row][col]-1), row, col])
return -1
```