# Intuition

我們的目標是讓subset sum of nums1[:i]跟subset sum of nums2[:i]相等就是合法的選擇
比起追蹤兩個變數，我們可以看他的diff就好，定義`diff[i] = nums1[i] - nums2[i]`

這樣的話就只需要一個變數就能知道我們需要的資訊，只要diff=0，那就是合法的選擇

但由於array index不可以負數，所以我們全部平移一個`OFFSET`，`OFFSET`就`sum(nums1), sum(nums2)`間選最大的

再來就考慮前`i`個數，然後遍歷所有sum的可能
__ __ __ __ __ 0 __ __ __ __ __ __ __
            nums1[i]
            nums2[i]

定義dp[i][sum]為 the number of different ranges whose sum is `sum` considering nums1[:i] and nums2[:i]

如果這輪選nums1[i]
dp[i][sum] = dp[i-1][sum-nums1[i]]

如果這輪選nums2[i]
dp[i][sum] = dp[i-1][sum+nums2[i]]

另外，nums1[i]跟nums2[i]都可以是一個新的[l, r]區間
dp[i][nums1[i]] += 1
dp[i][-nums2[i]] += 1

最終答案就是 sum(dp[i][0] for i = 1 to n), 1-indexed

由於array的index不可為負數，
所以我們平移一個`OFFSET`，狀態轉移方程就變成:

```
if -OFFSET <= sum-nums1[i] <= OFFSET:
    dp[i][sum+OFFSET] = dp[i-1][sum-nums1[i]+OFFSET]
if -OFFSET <= sum-nums2[i] <= OFFSET:
    dp[i][sum+OFFSET] = dp[i-1][sum+nums2[i]+OFFSET]

dp[i][nums1[i]+OFFSET] += 1
dp[i][-nums2[i]+OFFSET] += 1
```

因此整個核心框架為:
```py
OFFSET = max(sum(nums1), sum(nums2))
res = 0
for i in range(1, n+1):
    dp[i][nums1[i]+OFFSET] += 1
    dp[i][-nums2[i]+OFFSET] += 1
    for _sum in range(-OFFSET, OFFSET+1):
        dp[i][_sum+OFFSET] = dp[i-1][_sum-nums1[i]+OFFSET]
        dp[i][_sum+OFFSET] = dp[i-1][_sum+nums2[i]+OFFSET]
    res += dp[i][0+OFFSET]
    res %= 1_000_000_007
```

那最終答案就是在每個可能的`i`的所有diff為零的可能數加總起來，並對1e9+7取餘