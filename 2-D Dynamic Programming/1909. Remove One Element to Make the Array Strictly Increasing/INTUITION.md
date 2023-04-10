# Intuition

一開始是想這麼定義
dp[i][0]: make nums[:i] strictly increasing without deletion
dp[i][1]: make nums[:i] strictly increasing with one deletion

**base case**

dp = [[False, False] for _ in range(n+1)]
dp[0][0] = True

**state transfer**

if nums[i] > nums[i-1]:
    dp[i][0] = dp[i-1][0]

dp[i][1] = dp[i-1][0] or (dp[i-1][1] and nums[i] > previous max nums[i] with deletion)

對於dp[i][1]來說:
1. 刪除nums[i], 那麼就看dp[i-1][0]是不是strictly increasing
2. 之前已經刪除過, 那麼就看 nums[i][1] 和 nums[i] 有沒有大於先前刪除後最大的nums[i]

看這狀態轉移才發現，我們必須知道前一個刪除一次後的最大nums[i]才可進行轉移
所以我們狀態定義得變一下:

dp[i][0]: the maximum value with strictly increasing nums[:i] without deletion
dp[i][1]: the maximum value with strictly increasing nums[:i] with one deletion

我們分別紀錄到`i`為止的有刪除跟沒有刪除時的最大nums[i]

那麼對於dp[i][0]的狀態轉移則為:

1. 如果nums[i] > nums[i-1], 那麼dp[i][0] = nums[i]
2. 如果nums[i] <= nums[i-1], 那麼代表不可能strictly increasing, 我們讓dp[i][0] = inf

至於dp[i][1]的狀態轉移則一樣:
1. 如果我們刪除掉nums[i], 那麼dp[i][1] = dp[i-1][0]
2. 如果我們不打算刪除nums[i], 那們我們就看nums[i]有沒有大於dp[i-1][1]
   1. 如果沒有, 那我們只能刪除nums[i]
   2. 如果有, 那麼我們就nums[i]跟dp[i-1][1]裡取個最小的，以利於後面strictly increasing. 概念有點像是LIS的nlogn解法的patience sort(接龍)概念 (Greedy)

那要注意的一點是, 如果途中dp[i][1]已經是inf, 那代表我們肯定無法使整個nums strictly increasing
這時就直接返回False

如果一路到最後都沒有返回False, 那就看dp[n][0]跟dp[n][1]任一有沒有解
任一策略有解(值非inf)，那代表有可行解

# Other Solution
但從上面分析可發現，其實整個過程很像是LIS的Greedy解法 (patience sort)
所以其實我們可以去找nums的LIS, 然後看LIS的長度有沒有大於等於n-1(至多刪除一個數)
有的話代表有可行解

從這題可延伸:對於遞增序列且跟刪除數有關的話, 可以想一下是不是能跟LIS扯上關係