# Intuition

先求出每個點到最近thief的距離作為他們的權重
=> 可以以每個thief作為起點, 然後用BFS求出其他點到thief的距離
=> 我們可以記錄在一個dist array裡, dist[row][col]代表(row, col)到最近thief的距離, 也就是(row, col)的max safeness factor

由於safeness factor是整條路徑裡的最小權重
所以對於從(r, c)移動到(row, col), 當前path的權重變化為 weight = min(weight, dist[row][col])

那這樣這題就能轉換成帶有safeness factor權重的graph problem
要求出從(0, 0) -> (m-1, n-1)的最大權重的一條路徑
=> 我們可以用dijkstra找出這條路徑 (BFS + max heap)

# Other Solution - BFS + Binary Search

high level should be:

```py
l, r = 0, dist[0][0]
while l < r:
    mid = r - (r-l)//2

    if BFS(mid):
        l = mid
    else:
        r = mid-1
return l
```

我們用binary search來猜最高權重, 然後再用BFS來確認當前`mid`能不能走到(m-1, n-1)