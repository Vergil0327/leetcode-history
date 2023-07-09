# Intuition


我們要找一段non-decreasing subarray

`[... X] Y`

如果Y要接在後面, Y 必須 >= X
Y可以是nums1[i]或nums2[i]
由於最長subarray有可能是以nums1[i]結尾或是以nums2[i]結尾
所以兩個都得試過然後取最大的

我們定義dp:
dp[i][0]: the maximum length of non-decreasing subarray ended at nums1[i]
dp[i][1]: the maximum length of non-decreasing subarray ended at nums2[i]

那麼狀態轉移則為:

1. 如果nums1[i] >= nums1[i-1] => dp[i][0] = dp[i-1][0] + 1
2. 如果nums1[i] >= nums2[i-1] => dp[i][0] = dp[i-1][1] + 1
3. 如果nums2[i] >= nums1[i-1] => dp[i][1] = dp[i-1][0] + 1
4. 如果nums2[i] >= nums2[i-1] => dp[i][1] = dp[i-1][1] + 1

由於dp[i][0]跟dp[i][1]都有兩種前驅狀態，我們取max()
那麼我們就能實時更新res = max(res, max(dp[i][0], dp[i][1]))

**base case**

`dp[i][0] = dp[i][1] = 1 where i from 0 to n-1`