# Intuition

首先要如何求LIS的最長長度這很簡單

nums = X X X X X X X X X
                 j     i

對於第i個元素我們可以往前找到一個合法的j接在後面取最大值

```py
n = len(nums)
dp = [1] * n # the maximum length of LIS ended at i index

for i in range(n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
```

但由於我們要知道的是有多少個這個長度的LIS

所以如果 nums[i] > nums[j]時
如果有 M 個 nums[j] 那加上nums[i]後就會有 M個以nums[i]結尾的LIS
所以:
```py
if nums[j] < nums[i]:
    if dp[j] + 1 > dp[i]:
        count[i] = count[j]
```


如果此時最長長度為dp[i]
那如果有其他長度也為dp[i]的LIS也是我們要的, 所以:
```py
if nums[j] < nums[i]:
    if dp[j] + 1 == dp[i]:
        count[i] += count[j]
```

所以這代表我們不只要更新dp[i]，我們還要用另外一個數組來持續更新我們的count
因此大體架構為:

```py
dp = [1] * n
count = [1] * n

for i in range(n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                count[i] = count[j]
            elif dp[j] + 1 == dp[i]:
                count[i] += count[j]
```

那最後答案就是看有多少個最長長度的LIS

```py
ans = 0
maxLen = max(dp)
for i in range(n):
    if dp[i] == maxLen:
        ans += count[i]
```