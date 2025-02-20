# Intuition

從1為起點, 依照規則`1 -> 2 -> 0 -> 2 -> 0 -> ...`往四個對角方向出發, 在任意位置都能再有一次機會朝右轉向90度(也可單純繼續前進)
並持續依照`-> 2 -> 0 -> 2 -> 0 -> ...`規則前進
目的是找出最長的segment

那這看來會是個DFS相關問題, 遍歷整個grid時間為O(mn) ~ O(500*500)
所以可以遍歷起點"1"然後進行DFS

預期框架可能大概像是:

dfs(r, c, need, didTurn, curDirection): the longest length at (r,c) with next step should be `need` (2 or 0), current direction is `curDirection` and `didTurn` indicate if we turn 90 deg clockwise before

```py
m, n = len(grid), len(grid[0])

res = 0
for r in range(m):
    for c in range(n):
        if grid[r][c] == 1:
            for curDirection in direction:
                res = max(res, dfs(r, c, 2, False, curDirection)+1)
return res
```

那依這個思緒, 看起來就單純的dfs搜索, 試著搜索並維護狀態
最後再補上cache即可

```py
# direction state mapping (90 deg clockwise)
direction = {
    (1,-1): (-1,-1),
    (-1,-1): (-1,1),
    (-1,1): (1,1),
    (1,1): (1,-1),
}

@lru_cache(None)
def dfs(r, c, need, didTurn, curDirection):
    """
    need = 2 | 0
    next need = 2 if current is 0
                = 0 if current is 2
                = 2-need
    """
    step = 0

    # keep moving forward
    row, col = r+curDirection[0], c+curDirection[1]
    if 0 <= row < m and 0 <= col < n and grid[row][col] == need:
        step = max(step, dfs(row, col, 2-need, didTurn, curDirection) + 1)

    if not didTurn: # try turning 90 deg clockwise
        nextDirection = direction[curDirection]
        row, col = r+nextDirection[0], c+nextDirection[1]
        if 0 <= row < m and 0 <= col < n and grid[row][col] == need:
            step = max(step, dfs(row, col, 2-need, True, nextDirection) + 1)
    return res
```