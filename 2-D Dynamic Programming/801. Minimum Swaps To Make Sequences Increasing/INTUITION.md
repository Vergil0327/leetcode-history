# Intuition

最初想的是能不能greedy? 但稍微想一下發現，對於當前的nums1[i], nums2[i]來說

有可能當下不換，但後續換會更少步驟
也可能換了之後，才能達到最佳解
所以這樣一想，就會想到其實就兩種狀態在變化

所以想到可能可以這麼定義dp:

dp[i][didSwap, 0 or 1]: the minimum number of swaps to make nums1[:i] and nums2[:i] strictly increasing which didSwap = 0 means we don't swap nums1[i] with nums2[i], whereas didSwap = 1 means we swap nums1[i] with nums2[i]

但當時後續的狀態轉移就卡住了，但實際上當前的dp[i][0], dp[i][1]只跟dp[i-1][0], dp[i-1][1]有關，所以我們這麼分析:

1. 如果當前的nums1[i], nums2[i]不用換, 那代表
   1. 如果上一輪也沒換，那麼只有當`nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]`時，我們可以從 dp[i-1][0] 轉移到 dp[i][0]
      - dp[i][0] = min(dp[i][0], dp[i-1][0]) if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]
   2. 如果上一輪有換，那麼就是當`nums1[i] > nums2[i-1] and nums2[i] > nums[i-1]`時，我們可以從 dp[i-1][1] 轉移到dp[i][0]
      - dp[i][0] = min(dp[i][0], dp[i-1][1]) if nums1[i] > nums2[i-1] and nums2[i] > nums[i-1]

2. 如果當前nums1[i], nums2[i]需要調換, 那代表
   1. 如果上輪沒換，那就是當`nums2[i] > nums1[i-1] and nums1[i] > nums2[i-1]`時，我們可以從 dp[i-1][0]+1 轉移到dp[i][1]
      - dp[i][1] = min(dp[i][1], dp[i-1][0]+1) if nums2[i] > nums1[i-1] and nums1[i] > nums2[i-1]
   2. 如果上輪有換，那就是當`nums2[i] > nums2[i-1] and nums1[i] > nums1[i-1]`時，我們可以從 dp[i-1][1]+1 轉移到dp[i][1]
      - dp[i][1] = min(dp[i][1], dp[i-1][1]+1) if nums2[i] > nums2[i-1] and nums1[i] > nums1[i-1]

最終答案就是 `min(dp[n-1])`

然後注意一下base case
第一輪的時候可以自由調換，dp[0][0] = 0, dp[0][1] = 1
然後我們從第二輪開始進行狀態轉移