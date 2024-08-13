# Intuition

3250. Find the Count of Monotonic Pairs I 的 follow-up

原3250題的解法, 時間上O(n * max(nums[i]]) * max(nums[i]])) ~ O(2000 * 1000 * 1000) 會超時
從數據上來看, 時間複雜度上僅能允許`O(n * max(nums[i]))`

遍歷`i`跟`num1`感覺是無法避免, 所以很直覺地會想說該如何優化第三層循環那部分:

```py
for i in range(1, n):

    for num1 in range(nums[i]+1):
        num2 = nums[i]-num1
        if num2 < 0: break

        for prev_num1 in range(min(nums[i-1]-num2, num1)+1):
            dp[i][num1] += dp[i-1][prev_num1]
            dp[i][num1] %= mod

return sum(dp[n-1]) % mod
```

從上面關係式子`dp[i][num1] += dp[i-1][prev_num1] for prev_num1 in range(min(nums[i-1]-num2, num1)+1)`可看出
`dp[i][num1]`加上的是一段區間和, 所以感覺我們可以結合**dp + prefix sum**來讓這段O(n)降至O(1)

所以我們額外維護個`presum_dp[i][num]`, 其中presum[i][num]代表i-th round的sum(dp[i][0] + ... + dp[i][num])
整體概念上會像這樣:

```py
presum_dp = [[0]*(mx+1) for _ in range(n)]
presum_dp[0][0] = dp[0][0]
for num in range(1, mx+1):
    presum_dp[0][num] = presum_dp[0][num-1] + dp[0][num]

for i in range(1, n):

    for num1 in range(nums[i]+1):
        num2 = nums[i]-num1
        if num2 < 0: break

        upperbound = min(nums[i-1]-num2, num1)
        # for prev_num1 in range(upperbound+1):
        #     dp[i][num1] += dp[i-1][prev_num1]
        #     dp[i][num1] %= mod

        if upperbound >= 0:
            dp[i][num1] += presum_dp[i-1][upperbound]
            dp[i][num1] %= mod
    
    presum_dp[i][0] = dp[i][0]
    for num in range(1, mx+1):
        presum_dp[i][num] = presum_dp[i][num-1] + dp[i][num]

return sum(dp[n-1]) % mod
```

將這段更新改用presum_dp更新:

```py
for prev_num1 in range(upperbound+1):
    dp[i][num1] += dp[i-1][prev_num1]
    dp[i][num1] %= mod

# 上下相對應

if upperbound >= 0:
    dp[i][num1] += presum_dp[i-1][upperbound]
    dp[i][num1] %= mod
```

然後在更新完dp後, 再以O(max(nums))的時間更新presum_dp

所以整體時間複雜度為: O(n * 2 * max(nums))