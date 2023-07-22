# Intuition

see example 1.

每次可以移動到8個位置, 如果第一回合後下個位置是合法的位置, 那該位置的機率就是1/8
再下次如果又成功, 那就是(1/8) * (1/8)
最後把所有在k回合後還成功留在棋盤上的機率加總起來就會是最終還留在位置的機率

首先想到是可以用DFS/BFS, 然後會有k rounds
DFS的話就是top-down方式開始遞歸直到k=0
base case就是到k=0時還留在棋盤, 所以機率返回1, 其餘越界的就返回0
並且我們可以對計算過的位置做memorization => {(row, col, k): prob}

bottom-up方式也是一樣
每一輪遍歷當前每個合法位置(機率不為0)都可以跳到下個合法位置, 這時下個合法位置的機率就是`當前位置 * 1/8`
然後下一輪再遍歷每個合法位置, 這邊是用現在狀態更新未來狀態, 所以`dp[row][col][K-1] += dp[r][c][K] * 1/8`
```py
if dp[r][c][K] != 0:
    for dr, dc in dirs:
        row, col = r+dr, c+dc
        if row < 0 or row >= n or col < 0 or col >= n:
            continue
        dp[row][col][K-1] += dp[r][c][K] * 1/8
```

這邊可以遍歷整個棋盤找出合法位置(機率dp[r][c][K]不為0), 然後更新dp
也可以用BFS配合visited hashset去找出下一輪的合法位置並移除duplicate
=> 因為下輪位置的dp state已經更新過, 我們僅需要知道下輪的位置然後繼續更新下下輪的dp, 如果不移除duplicate的話dp state會被錯誤更新

```py
while K:
    for r in range(n):
        for c in range(n):
            if dp[r][c][K] != 0:
                for dr, dc in dirs:
                    # update dp[row][col][K-1]
    K -= 1
```

```py
queue = set([(ROW, COLUMN)])
while K:
    nxtQueue = set() # next valid position
    for r, c in queue:
        for dr, dc in dirs:
            # update dp[row][col][K-1]
    K -= 1
    queue = nxtQueue
```