# Intuition

依據題意, 在遍歷nums的過程中`i`要放進group nums[i]裡, 並且最後依據group1, group2, group3的順序組成res必須是increasing order

這代表nums必須轉成[11111..... 22222.... 3333....], 這樣最後`res`才會是increasing order

所以我們可以用dp來找出最佳解

```
X X X X X X X j' j
                 i
``` 
define dp[i][j]: the minimum operation ended at group j where 1 <= j <= 3 considering nums[:i]

then state transfer should be:

dp[i][j] = dp[i-1][j'] + 1 if j != nums[i] and j must >= j'
dp[i][j] = dp[i-1][j'] + 0 if j == nums[i] and j must >= j'

thus, we iterate i first, then iterate all the possible j', and iterate j from j' to 3 at last

the final answer should be min(dp[n-1]) because optimal solution can end at 1 or 2 or 3.
