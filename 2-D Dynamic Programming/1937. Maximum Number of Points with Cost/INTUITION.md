# Intuition

dp[r][c]: the maximum points considering first r rows and ended at c rows

then we can get state transfer fn intuitively:
```
dp[r][c] = maximum(dp[r-1][c1]-abs(c1-c) or dp[r-1][c2]-abs(c2-c) or dp[r-1][c3]-abs(c3-c)) + points[r][c]
         = max(dp[r-1][x]-abs(c-x) for x in range(n)) + points[r][c]
```

be careful of edge case `i=0`, thus:
```py
for c in range(n):
    dp[0][c] = points[0][c]

for r in range(1, m):
    for c in range(n):
        dp[r][c] = max(dp[r-1][x]-abs(c-x) for x in range(n)) + points[r][c]
return max(dp[m-1])
```

but time complexity is $$O(n^3)$$

if we strip off `abs()`, we got:

```py
for r in range(1, m):
    for c in range(n):
        # case 1
        dp[r][c] = max(dp[r-1][x]+x for x in range(n) if x <= c) - c + points[r][c]
        
        # case 2
        dp[r][c] = max(dp[r-1][x]-x for x in range(n) if x > c) + c  + points[r][c]
```

- case 1: we want maximum of dp[r-1][x]+x for every 0 <= x <= j -> rolling max where x from 0 to c

```py
# Case 1
rollingMax = -inf
for c in range(n):
    rollingMax = max(rollingMax, dp[r-1][c]+c)
    dp[r][c] = max(dp[r][c], rollingMax - c + points[r][c])
```

- case 2: we want maximum of dp[r-1][x]-x for every j >= x < n -> rolling max where x from n-1 to c

```py
# Case 2
rollingMax = -inf
for c in range(n-1, -1, -1):
    rollingMax = max(rollingMax, dp[r-1][c]-c)
    dp[r][c] = max(dp[r][c], rollingMax + c  + points[r][c])
```