# Intuition

對3取餘數僅可能有`0,1,2`

如果當前nums[i]%3 == 0 可以接在 sum%3==0的後面
如果當前nums[i]%3 == 1 可以接在 sum%3==2的後面
如果當前nums[i]%3 == 2 可以接在 sum%3==1的後面

所以我們可以這麼定義dp:

`dp[i][mod]: maximum possible sum considering array[:i] where the current sum modulo 3 is equal to mod.`

所以如果取nums[i]的話, j = nums[i]%3
那麼dp[i][mod] = dp[i-1][(3+mod-j)%3] + nums[i]

如果不取nums[i]的話, dp[i][mod] = dp[i-1][mod]

那就兩種決策取最大的possible sum: dp[i][mod] = max(dp[i-1][mod], dp[i-1][(3+mod-j)%3]+nums[i])

這樣最終答案就是dp[-1][0]

初始條件的話, 因為要取`max`, 所以初始值我們可以設-inf

那麼dp[0][0] 就等於 0 -> 0個元素且sum%3餘0的possible sum, 那就是0