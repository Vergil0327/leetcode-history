# Intuition

Basic Dynamic Programming

we can define: `dp[i][j]: the minimum path sum until i-th row at triangle[i][j] position`

and each `dp[i][j]` can be transfered from 2 state:
- from `dp[i-1][j]`: j index from previous row
- fro `dp[i-1][j-1]`: j-1 index from previous row

thus, **state transfer fn** should be:

`dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]`

**base case**

`dp[0][0] = 0`

# Complexity

- time complexity

$$O(n^2)$$

- space complexity

$$O(n^2)$$

# Space Optimized

we can observe state transfer deeply and know that `dp[i][j]` only depends on its previous `dp[i-1]` state.
therefore, we can reduce `dp` down to $O(n)$ space

**definition**

```
prevdp = [inf]*(n+1) # store dp[i-1][0...j] state
dp = [inf]*(n+1)     # store dp[i][0...j] state
```

**base case**

prevdp[0] = 0