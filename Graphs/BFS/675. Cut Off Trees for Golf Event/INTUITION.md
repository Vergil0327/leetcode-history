# Intuition

由於我們砍樹的順序是固定的，必須由矮到高的砍伐，因此我們可以用minHeap儲存全部的數，然後一一找出我們當前要砍的樹是哪一顆

利用 O(mnlog(mn)) 的時間儲存順序
```
m, n = len(forest), len(forest[0])
minHeap = []
for i in range(m):
    for j in range(n):
        if forest[i][j] > 1:
            heapq.heappush(minHeap, forest[i][j])
```

那既然是要找出最短路徑，那我們可以利用BFS，每當砍完一顆後，便重新BFS搜索下一個目標的最短路徑
等到我們全部砍完，返回我們走過的所有步數即可

# Complexity

- time complexity:
$$O(mn * (log(mn) + mn))$$

- space complexity:

$$O(mn)$$