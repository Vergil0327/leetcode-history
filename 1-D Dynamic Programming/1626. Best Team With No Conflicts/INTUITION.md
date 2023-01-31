# Intuition

考慮兩個亂序條件比較難處理，試著對其中一個條件排序試試

在不考慮年齡情況下，其實要找的就是個分數的LIS
只是在年齡相等情況下，就不限
因此我們對age排序，考慮如果我們選擇第i個人的話，往前找可以接在哪個第`j`個人後面

其中當年齡`ages[j] < ages[i]`時，`scores[j] <= scores[i]`都是符合的
`dp[i] = max(dp[j] + scores[i]) for j < i`

但當年齡相等時則不在此限，同樣
`dp[i] = max(dp[j] + scores[i]) for j < i`

最後在所有可能中找最大的即可

**definition**
dp[i] = maximum sum of increasing subsequence when choose i-th player

# Complexity

- time complexity
$$O(n^2)$$

- space complexity
$$O(n)$$