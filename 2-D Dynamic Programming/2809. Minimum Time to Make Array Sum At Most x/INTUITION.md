# Intuition

比較能直覺想到的是
- 優先讓nums2[i]小的變為零, 這樣他的數字遞增的比較慢
- 每個nums1[i]最多只需要設為0一次, 設第二次就只是在循環一次而已

所以我們可以先對(nums2[i],nums1[i]) pair排序得到`arr = sorted(zip(nums2, nums1))`
再來定義`dp[i][j]: the maximum **reduced** total value when we do j operations for first i elements`
- 什麼都不做, j=0, 全部減少0 => dp[i][j] = dp[i][0] = 0
- 當我們j operations用在arr[i]上, 可以減少dp[i-1][j-1] + arr[i][0]*j + arr[i][1]
- 當我們j operations不用在arr[i]上, 最多可減少dp[i-1][j]
- 兩者取大可得到, 到前i個元素為止, 當前操作數所能減少的最大值為: max(dp[i-1][j], dp[i-1][j-1] + arr[i][0] * j + arr[i][1])

```py
X X X X X X X X X X X nums1[i-1] nums1[i]

dp[i][0] = 0
dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + arr[i][0] * j + arr[i][1])
```

所以根據前面分析, 對於整個n個元素來說, 當操作j operations時可減少dp[n][j] (1-indexed)
當t=0時, 什麼操作都沒做, 此時total value = sum(nums1)
當t=1時, 可以做一次操作, 此時total value = sum(nums1) + sum(nums2)*1 - dp[n][1]
...
當t=n時, total value = sum(nums1) + sum(nums2)*n - dp[n][n]
最多只需要做到t=n, 在以上就是循環而已

也就是一但我們找到`total value = sum(nums1) + sum(nums2)*t - dp[n][t] <= x, where 0 <= t <= n`時, 那就返回t, 沒有合法解則返回-1

# Complexity

- time complexity

$$O(n^2)$$

- space complexity

$$O(n^2)$$
