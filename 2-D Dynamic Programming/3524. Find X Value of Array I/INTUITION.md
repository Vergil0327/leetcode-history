# Intuition

```
* * * {*} * * *
* * {* *} * * *
* {* * *} * * *
{* * * *} * * *
 j     i
```

res[product(nums[j:i])%k] += 1

1. 首先乘積會很大, 直覺想到一定跟餘數有關
2. 1 <= k <= 5: k數值不大, 可以遍歷

所以我們可以遍歷所有可能餘數`r`, 那很自然能想到下面這關係式:
當前的餘數`x`等於所有可能的餘數`r`乘上`nums[i]`再對`k`取餘:

```py
for r in range(k):
    x = (r * nums[i]) % k
    dp[x] += dp[r]
```

然後我們再從只看nums[i]到看整個nums[:i], 所以我們定義:
dp[i][r]: the number of subarrays ended at i whose product modulo k is r

那麼狀態變化的思路就清晰了:

```py
n = len(nums)

nums = [0] + nums
dp = [[0]*k for _ in range(n+1)]
for i in range(1, n+1):
    # only nums[i] itself
    dp[i][nums[i]%k] += 1

    for r in range(k):
        x = (r*nums[i])%k
        dp[i][x] += dp[i-1][r]
```

注意這邊base case: `dp[0][r] = 0 for r i range(k)`
這是因為0-size的subarray並不符合定義

那既然得知結束於每個位置`i`的subarray裡, 有dp[i][r]個合法subarray, 全部在遍歷一遍加總即可得到最終答案

```py
res = [0] * k
for i in range(1, n+1):
    for r in range(k):
        res[r] += dp[i][r]
return res
```

time: O(nk)
space: O(nk)