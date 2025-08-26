# Intuition

首先先確保robots跟wall在位置上是有序的

```
robot_i                               robot_i+1
  |----left bullet------>
            <----------right bullet-------|
```

再來由於每個robot可以選擇往右或往左擊發, 所以這邊我們定義:

dp[i][0]: Return the maximum number of unique walls that can be destroyed by the robots[:i] and robot[i+1] DON'T fire its bullet to the left
dp[i][1]: Return the maximum number of unique walls that can be destroyed by the robots[:i] and robot[i+1] fires its bullet to the left

那麼base case:

- dp[0][0] = 0
- dp[0][1] = count(l, r) # 首位機器人往左擊發
    - l = arr[0][0]-arr[0][1]
    - r = arr[0][0]-1

note. 注意這邊有個小細節是, 我們排除掉所以跟robot重疊的wall, 因為不管robot往左或往右擊發, 都一定會集中該wall. 而排除掉是因為起初沒排除掉, 在計算上很難考慮有沒有計算或是重複計算到

那麼dp狀態轉移為:

dp[i][0] = max(dp[i-1][0] + prev, dp[i-1][1]) # max(前一位沒往左擊發的狀態 + 前一位往右擊發的擊倒數, 前一位往左擊倒數)
dp[i][1] = max(dp[i-1][0] + prev + current - overcount, dp[i-1][1] + current) # 前一位沒往左擊發的狀態 + 前一位往右擊倒數 + 當前往左擊倒數 - 重複擊倒數, 前一位王左擊倒數 + 當前往右擊倒數

那最終答案就是max(dp[-1]) + 所有跟robot重疊(必定被集中)的牆的數目

但由於也要考慮首位robot往左擊發的狀態, 所以我們定義dp有`n+1`個狀態 (1-indexed)

base case:

```py
dp = [[0,0] for _ in range(n+1)]
dp[0][0] = 0
dp[0][1] = count(arr[0][0]-arr[0][1], arr[0][0]-1)
```

狀態轉移變成:

```py
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0] + left_bullet, dp[i-1][1])
    dp[i][1] = max(dp[i-1][0] + left_bullet + right_bullet - overcount, dp[i-1][1] + right_bullet)
```

### helper function

count(l, r): count the number of walls that can be destroyed within [l,r] range
