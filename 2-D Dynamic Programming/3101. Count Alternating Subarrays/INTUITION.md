# Intuition

直覺想到的是類似LIS的dynamic programming

我們定義:
dp[i][0]: 前i個元素當中, 以0作結尾的subarray的個數 
dp[i][1]: 前i個元素當中, 以1作結尾的subarray的個數

那狀態轉移也很簡單:

dp[i][0] += dp[i-1][1]
dp[i][1] += dp[i-1][0]

base case:

```py
for i in range(n):
    dp[i][nums[i]] = 1
```

由於subarray可能終止在任何一個位置
所以最終答案就是將所有的dp[i]加總起來