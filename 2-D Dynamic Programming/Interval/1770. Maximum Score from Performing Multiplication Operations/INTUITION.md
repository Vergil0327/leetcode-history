# Intuition

```
X X X X X X
l         r
```

choose nums[l] or nums[r]
- choose nums[l]
  - score += nums[l] * multipliers[j]
  - keep doing in nums[l+1:r]
- choose nums[r]
  - score += nums[r] * multipliers[j]
  - keep doing in nums[l:r-1]

doing exactly m rounds, and we choose maximum score in each round by doing:
`max(nums[l]*multipliers[j] + score(nums[l+1:r]), nums[r] * multipliers[j] + score(nums[l:r-1]))`

thus, we just use topdown dp to simulate and explore optimal solution.

**base case**

since guarentee m <= n, base case is just:
`if j >= m: return 0 where m = len(multipliers)`

# Complexity

- time complexity

$$O(m^2)$$

we can choose m elements from the beginning or from the end

# Other Solution - bottom up

since we need to choose m elements from both sides 

we can define dp[i][j] as:
dp[i][j]: the maximum socre for picking first i elements and last j elements

```
X X X X _ _ _ _ _ _ _ X X X X X X
      i               j
```

thus,
`dp[i][j] = max(dp[i-1][j] + nums[i]*multipliers[i+j-1])`
`dp[i][j] = max(dp[i][j-1] + nums[n-j+1]*multipliers[i+j-1])`
where i, j are 1-indexed

because we want to build dp table from bottom to up, we need to start with small interval.

```py
from length in range(m):
    for i in range(length+1): # pick i elements from beginning
        j = length-i # pick j elements from end

        # only if i > 0, we got score from left. and vice versa, j > 0 to update dp[i][j] from dp[i][j-1]
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + nums[i]*multipliers[i+j-1])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + nums[n-j+1]*multipliers[i+j-1])
```

**Base Case**

remember to think our base case:
both dp[0][1] and dp[1][0] depend on dp[0][0]

dp[0][0] should be `0` since we pick nothing from both sides