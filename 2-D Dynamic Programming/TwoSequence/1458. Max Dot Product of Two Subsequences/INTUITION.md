# Intuition

一開始毫無想法，但看起來是個雙序列DP
因為前面選擇玩nums1[i]*nums2[j]後，有**無後效性**
後面的輪次的選擇不會更改前面輪次的選擇
並且後面輪次的選擇會基於前面輪次而繼續找出最佳解

nums1[0:i]跟nums2[0:j]找出的最佳解就是nums1跟nums2的子問題

所以我們先試著照著題目定義

**dp definition**

dp[i][j]: the maximum dot product between non-empty subsequences of nums1[0:i] and nums2[0:j] with the same length

然後我們來看dp[i][j]跟dp[i-1][j], dp[i][j-1], dp[i-1][j-1]有沒有什麼關係

而這樣定義的話，我們改成**1-index**，base case就會是:
由於要取max，所以預設值為-inf

兩個序列都為空時，最大的dot product = 0
`dp[0][0] = 0 `

因為選擇的nums1[:i]跟nums2[:j]必須是相同長度所以不可以一個為空另一個有長度，所以`dp[0][j]`跟`dp[i][0]`也是 `-inf`


再來來看第一個example來看:

nums1 = 2 1 -2 5
nums2 = 3 0 -6
dp[1][1] = dp[0][0] + 2*3 = 0+6
dp[1][1] = max(dp[0][1], 2*3) = max(-inf, 2*3)
dp[1][1] = max(dp[1][0], 2*3) = max(-inf, 2*3)
所以dp[1][1] = 6

然後再看dp[1][2]
dp[1][2] = dp[0][1] + 2*0 = -inf + 2 = -inf
dp[1][2] = max(dp[0][2], 2*0) = max(-inf, 2) = 2
dp[1][2] = max(dp[1][1], 2*0) = max(6, 2) = 6
dp[1][2] = 6

看起來狀態轉移是對的，所以我們更general來看的話就是

對於nums1[i]*nums2[j]:
1. 我們可以是跟前面結果的疊加，也就是 dp[i-1][j-1] + nums1[i]*nums2[j]
2. 但也有可能nums1[i]不跟nums2[j]配對才是最佳，所以我們還要再考慮dp[i-1][j]跟dp[i][j-1]
   - dp[i-1][j]: 考慮nums2[:j]跟nums1[:i-1]，把nums1[i]留到之後配對
   - dp[i][j-1]: 考慮nums2[:j-1]跟nums1[:i]，把nums2[j]留到之後配對
3. 但也有可能nums1[i]*nums2[j]比前面的dot product結果都大，所以我們還要再dp[i-1][j]跟dp[i][j-1]間比較看看

所以dp[i][j]就是在三種情況取最佳
```py
dp[i][j] = max(dp[i][j], dp[i-1][j], nums1[i]*nums2[j])
dp[i][j] = max(dp[i][j], dp[i][j-1], nums1[i]*nums2[j])
dp[i][j] = max(dp[i][j], dp[i-1][j-1]+nums1[i]*nums2[j])
```

## More Concise

```py
dp[i][j] = max(dp[i][j], dp[i-1][j], nums1[i]*nums2[j])
dp[i][j] = max(dp[i][j], dp[i][j-1], nums1[i]*nums2[j])
dp[i][j] = max(dp[i][j], dp[i-1][j-1]+nums1[i]*nums2[j])
```

但實際上上面還能更精簡一點:
1. 考慮nums1[i]跟nums2[j]不配對的情況下取最大:

`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

2. 考慮nums1[i]*nums2[j]兩個配對的情況:

`dp[i][j] = max(dp[i][j], dp[i-1][j-1] + nums1[i]*nums2[j])`

由於nums1跟nums2含有負數，所以dp[i-1][j-1]有可能是負的
所以我們再取個`max(0, )`，也就是考慮nums1[i]*nums2[j]比先前都大的情況

`dp[i][j] = max(dp[i][j], max(0, dp[i-1][j-1] + nums1[i]*nums2[j]))`

所以最後就是這兩行:

```py
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
dp[i][j] = max(dp[i][j], max(0, dp[i-1][j-1] + nums1[i]*nums2[j]))
```

# Complexity

- time complexity
$$O(m*n)$$

- space complexity
$$O(m*n)$$
