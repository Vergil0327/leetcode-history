# Intuition

首先最短路徑 -> 想到BFS
再來就想到我們可以用`visited[row][col] = minimum_time`來記錄我們拜訪每個位置的時間

由於只有時間至少是moveTime[rol][col]的情況才能抵達該位置, 所以我們在進行BFS的時候:

更新visited[row][col]時, 必須至少是moveTime[row][col], 因此min(visited[cur_row][cur_col]+1, moveTime[row][col]+1)兩者取小:

`visited[row][col] = min(visited[row][col], max(visited[r][c], moveTime[row][col])+1)`

整體框架如下:

```py
visited[0][0] = 0
while queue:
    for _ in range(len(queue)):
        r, c = queue.popleft()

        for dr, dc in dirs:
            row, col = r+dr, c+dc
            if row<0 or row>=m or col<0 or col>=n: continue
            if visited[row][col] <= visited[r][c]+1: continue
            visited[row][col] = min(visited[row][col], max(visited[r][c], moveTime[row][col])+1)
            queue.append([row, col])

return visited[m-1][n-1]
```