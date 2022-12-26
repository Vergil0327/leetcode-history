# Intuition

**definition**

`dp[i][j]: the number of possible unique paths that robot can take to reach bottom-right`

**base case**

dp = [[0] * (n+1) for _ in range(m+1)]
1-based index: `dp[1][1]=1`

**state transfer**

if we encounter obstacle, it means there is no way we can go further.
thus, `dp[i][j] = 0 if grid[i][j] == 1`