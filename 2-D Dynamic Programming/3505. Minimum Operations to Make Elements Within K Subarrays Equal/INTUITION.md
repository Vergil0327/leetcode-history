# Intuition

For a subarray of size `x`, it is always optimal to make all the equal to the median element of the sorted subarray.
make median be `upper[0]`, then we can slide window to find minimum operations for every subarray of size `x` at position `i`
    
and the `needed operations = abs(sum_upper - median * upper.size) + abs(sum_lower - median * lower.size)`

we'll know minimum operations for every position after sliding window preprocess, vals[i] = needed operations for subarray starting at position `i` (0-indexed)

then we can use dp to find minimum operations for exactly k subarrays

define dp[i][k]: the minimum operations for first i elements and exactly k subarrays
    
base case: 0 operations for choosing 0 subarray

```py
for i in range(n+1):
    dp[i][0] = 0
```

then we iterate every possible size of subarray from 1 to n, update `dp[i][j] = min(dp[i-1][j], dp[i-x][j-1] + vals[i-x])` where
1. dp[i-1][j] for not choosing current subarray ending at i
2. dp[i-x][j-1] + vals[i-x] for choosing current subarray ending at i

```
X X X X X X X X {X X X X X}
             i-x         i
```

therefore, we can write code:

```py
for i in range(1, n+1): 
    for j in range(1, k+1): 
        if i >= j*x: # total elements need to be greater than j*x
            dp[i][j] = min(dp[i-1][j], vals[i-x] + dp[i-x][j-1])
```

then answer should be `dp[n][k]` for choosing all n elements with exactly k subarrays