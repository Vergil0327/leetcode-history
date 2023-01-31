# Intuition

首先最簡單的檢查是，先排除`n < 3`的情況，不可能形成Arithmetic Subarray，所以直接返回0

再來想到的是DP，由於Arithmetic Subarray取決於數值及他們的差，因此先這樣定義DP

```
dp[i][diff]: the number of subarray from nums[0:i] whose difference is diff

for 2 <= i < n:
    dp[i][diff] = dp[i-1][diff] + 1 if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]
```

diff最多可以差到max(nums)-min(nums)，因此我們的二維DP起始為:
`dp = [[0] * (max(nums)-min(nums)+1) for _ in range(n)]`

ex nums = [1,2,3,4]

當 i = 2:
nums[i-1] - nums[i-2] = 2-1 = 1
nums[i] - nums[i-1] = 3-2 = 1
diff相等，所以可以添加一個上去，這時就形成了一個長度為3的Arithmetic Slice
最後所求就是所有可能的長度i以及所有可能的diff個數相加: `sum(map(sum, dp))`

但這時我們發現:

`dp[i][diff] = dp[i-1][diff] + 1`

我們根本就不需要diff這個狀態，我們的狀態轉移對於`i`來說，只取決於`i-1`這個狀態
因此我們只需要用一維DP即可

所以我們可以這樣定義:

`dp[i] = dp[i-1] + 1 if if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]`

最後答案就是所有可能長度的subarray和: `sum(dp)`

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$