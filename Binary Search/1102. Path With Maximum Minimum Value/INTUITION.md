# Dijkstra

很明顯可看出我們總是盡可能往最大的的分數走即可
利用dijkstra，只是這次改成max heap儲存`-matrix[row][col]`，持續往最大分數走即可

time: (V+E)logv
space: O(V)

# Binary Search

這題還能用binary search來解，這是因為
假如我們存在一個`mid`值，那代表從左上走到右下，沿路上不可以有分數小於`mid`
因此我們可以用BFS來搜尋，避開所有分數小於`mid`的格子
假如最終能走到的話，代表`mid`是個可行解，我們可以繼續提高`mid`

```py
while l < r:
    mid = l + (r-l)//2
    if existPath(mid):
        l = mid
    else
        r = mid-1
return l
```