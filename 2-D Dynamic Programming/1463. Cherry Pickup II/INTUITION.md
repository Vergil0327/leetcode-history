# Top-down DP

## Intuition

想法很簡單，每一ROW選兩個位置，每個機器有三個選擇(COL-1, COL, COL+1)可選，當選到同個位置時別重複計算

```
cherry = grid[r][c1]
if c2 != c1: cherry += grid[r][c2]
```

如此一來我們的decision tree就出來了
接下來只要遞歸遍歷所有選擇，從合法選項裡選最大的即可
```
maxCherry = 0
for i in range(-1, 2):
    for j in range(-1, 2):
        maxCherry = max(maxCherry, dfs(r+1, c1+i, c2+j))
```

## Complexity

- time complexity

$$O(ROWS * (3*COLS)^2)$$
equals
$$O(ROWS * COLS^2)$$

since our DFS function have three variables as input, which have ROWS, COLS, and COLS possible values respectively. In the worst case, we have to calculate them all once, so that would cost $O(ROWS⋅COLS⋅COLS)$ = $O(ROWS*COLS^2)$. Also, since we save the results after calculating, we would not have repeated calculation.

- space complexity

$$O(ROWS*COLS*COLS)$$

since our DFS function have three variables as input, and they have ROWS, COLS, and COLS possible values respectively. We need a map with size of $O(ROWS*COLS^2)$ to store the results.

# Bottom-up DP

## Intuition

same concept as top-down dp

**definition**
define dp[row][col1][col2] to represent: for given `row`, the maximum number of cherries collection using robot1 at `col1` and robot2 at `col2`

**base case**
in the beginning, robot1 at grid[0][0] and robot2 at grid[0][COLS-1]
dp[0][0][COLS-1] = grid[0][0] + grid[0][COLS-1]

**state transfer**
dp[row][col1][col2] = dp[row-1][col_i][col_j] + grid[row][col1] + (grid[row][col2] if col1 != col2 else 0),
where col_i = col1 + 1 or 0 or -1 and col_j = col1 + 1 or 0 or -1