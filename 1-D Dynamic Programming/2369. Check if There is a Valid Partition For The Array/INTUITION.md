# Intuition

基本DP題目

**top-down**
decision tree:
- 如果nums[i] == nums[i+1]，那麼我們可以繼續遞歸考慮nums[i+2:]
- 如果`nums[i] == nums[i+1] == nums[i+2]` 或 `nums[i] == nums[i+1]-1 and nums[i+1] == nums[i+2]-1`，那麼繼續遞歸處理nums[i+2:]

**bottom-up**
dp[i]: can we partition nums[:i] to be a good series of subarray

1. 對於nums[i]來說，我們回頭看nums[i-1]跟nums[i]是否相等，如果相等代表這兩個可以分成一個合法的good subarray，我們可以判斷dp[i-2]是不是也能分成合法的good subarray

dp[i] = dp[i-2] if nums[i] == nums[i-1]

2. 同樣地對於nums[i]來說，回頭看nums[i-1], nums[i-2]是否能符合以下任一條件

- `nums[i] == nums[i-1] == nums[i-2]`
- `nums[i] == nums[i-1]+1 and nums[i-1] == nums[i-2]+1`

如果任一條件符合，那麽dp[i] = dp[i-3]

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$