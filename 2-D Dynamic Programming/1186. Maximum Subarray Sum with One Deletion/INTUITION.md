# Intuition

如果沒有deletion, 那就是知名的Kadane's algorithm
對於到第`i`個元素為止的最大subarray和, 有兩種選擇:
- 累加至arr[i]: dp[i-1][0] + arr[i]
- 如果之前的dp[i-1][0]加上去後變小，那不如不要，只留下arr[i]

所以`dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])`

```py
# dp[i][0]: maximum sum for a non-empty subarray without deletion considering first i elements
dp = [[0] for _ in range(n)]
dp[0][0] = arr[0]

res = arr[0]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
    res = max(res, dp[i][0])
return res
```

那如果可以刪除掉一個數呢?
我們定義:
`dp[i][1]: maximum sum for a non-empty subarray with 1 deletion considering first i elements`

arr = ＸＸＸＸＸＸＸＸＸＸＸ
                       i
對於dp[i][1]來說，如果刪的是第`i`個元素，那麼就是:
`dp[i][1] = dp[i-1][0]` # 在`i-1`前的最大subarray和

如果刪除的是之前的元素，那麼根據定義就是:
`dp[i][1] = dp[i-1][1] + arr[i]` # 在`i-1`前刪除掉一個元素後的最大subarray和，再加上arr[i]

所以dp[i][1]就是在這兩種決策下取最大值:
`dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])`

# Optimized

由於dp[i]只跟dp[i-1]有關，因此我們僅需要用一個變數來取代dp array

```py
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        noDel = arr[0] # dp[i][0]
        withDel = 0 # dp[i][1]

        res = arr[0]
        for i in range(1, n):
            # dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
            # dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])
            noDel, withDel = max(noDel + arr[i], arr[i]), max(noDel, withDel + arr[i])
            res = max(res, max(noDel, withDel))
        return res
```