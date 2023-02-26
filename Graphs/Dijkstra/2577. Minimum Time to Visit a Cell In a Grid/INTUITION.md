# Intuition

首先從example看來，無法抵達終點的情況只有一開始就動彈不得的情況，不然我們都可以透過反覆來回來讓秒數增加然後繼續前進

```
# only edge case we can't reach destination
if grid[0][1] > 1 and grid[1][0] > 1: return -1
```

再來想，由於要求最短路徑，那肯定是朝著BFS去想
直接用BFS會ＴＬＥ，那代表我們可能要用更高效的方式去找出抵達終點的最短時間

最短路徑，沒有負數權重，我們可以試著朝著Dijkstra來想

dijkstra基本框架為:

```py
while queue:
    weight, r, c = heapq.heappop(queue)    
    for dr, dc in dirs:
        row, col = r+dr, c+dc
        if row < 0 or row >= m or col < 0 or col >= n: continue
        if (row, col) in visited: continue
        visited.add((row, col))
        
         # implement logic here...
        heapq.heappush(queue, (weight, row, col))
```

首先我們用min heap來儲存: `[reached_time, row, col]`，盡可能往最少抵達時間的地方走

- 再來如果抵達`(row, col)`時的時間，也就是`current_time+1`大於等於`grid[row][col]`的話，代表抵達`(row, col)`的時間為`current_time+1`
  ```
  if grid[row][col] <= time+1:
      heapq.heappush(queue, (time+1, row, col))
  ```
- 但如果 `current_time+1 < grid[row][col]`的話，就的表我們需要來回走動來讓時間流逝了

我們可以用兩個簡單的例子來看, `ex.1` & `ex.2`

```
ex.1
[[0,9,9],
 [1,2,5]]

0->1, time = 1
1->2, time = 2
for 2->5: duration = 5-2 = 3, start back and forth
2->1, time = 3
1->2, time = 4

2->5, time = 5
```
```
ex.2
[[0,9,9],
 [1,2,4]]

0->1, time = 1
1->2, time = 2
for 2->4: duration = 4-2 = 2, start back and forth
2->1, time = 3
1->2, time = 4

2->4, time = 5
```

1. 當`grid[row][col]`與`current_time`的差為奇數時，我們來回走動後可以剛好在抵達`(row, col)`時，時間為`grid[row][col]`，也就是:
    ```
    back_and_forth = grid[row][col]-current_time
    if back_and_forth%2==1:
        reach_time = time+back_and_forth
    ```

2. 當`grid[row][col]`與`current_time`的差為偶數時，我們來回走動後會在回到原地後才能前往`(row, col)`，因此會需要多走一步，此時抵達`grid[row][col]`的時間就是:
 
    ```
    back_and_forth = grid[row][col]-current_time
    if back_and_forth%2 == 0:
        reach_time = time+back_and_forth+1
    ```
總和以上結果可得:

```py
if grid[row][col] <= time+1:
    heapq.heappush(queue, (time+1, row, col))
else:
    backForth = grid[row][col] - time
    if backForth%2 == 0:
        backForth += 1
    heapq.heappush(queue, (time+backForth, row, col))
```