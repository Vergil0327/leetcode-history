# Intuition

依題意, 目標要找出最小cost使得所有length=3的subarray都必須符合max(subarray) >= k

# Let dp[i] be the minimum number of increment operations required to make the subarray consisting of the first i values beautiful, while also having the value at nums[i] >= k.

dp[i] = min(dp[i-1], dp[i-2], dp[i-3]) + max(0, k-nums[i])

```
[X X X ... X   X  X]
          n-2 n-1 n
```

由於第n-2個element也可以cover到第n個element,所以最終答案為:
min(dp[n-2], dp[n-1], dp[n])
