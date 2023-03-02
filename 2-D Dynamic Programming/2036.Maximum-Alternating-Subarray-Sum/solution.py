from typing import List



class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-float('inf')]*2 for _ in range(n+1)]
        dp[0][1] = -float('inf')
        dp[0][0] = 0

        res = -float('inf')
        for i in range(1, n+1):
            dp[i][1] = max(nums[i-1], dp[i-1][0] + nums[i-1])
            dp[i][0] = dp[i-1][1] - nums[i-1]
            res = max(res, max(dp[i][1], dp[i][0]))
        return res

        

"""
以 example1 為例

由於我們必須記錄目前加上的nums[i]前面是正號還是負號,我們用額外的dp[i][0]跟dp[i][1]表示
dp[i][0] 代表第i位是負號
dp[i][1] 代表第i位是正號

這樣我們就能進行狀態轉移, 第i-1位必定是alternating sign:
dp[i][1] = max(nums[i], dp[i-1][0] + nums[i])
dp[i][0] = max(-nums[i], dp[i-1][1] - nums[i])

由於每個nums[i]都可以作為subarray的開頭, 所以我們取max
-> 因為如果nums[i]以先前的subarray和還大, 那我們沒必要取之前的dp[i]作為結果

但由於這題的alternating subarray必須是正號開頭
所以其實dp[i][0]不可能有-nums[i]作為開頭的subarray
因此dp[i][0] 只可能是 dp[i-1][1] - nums[i]

把所有的可能在這兩者中取max就是結果
"""
# Input: nums = [3,-1,1,2]
# Output: 5
# Explanation: 
# The subarray [3,-1,1] has the largest alternating subarray sum.
# The alternating subarray sum is 3 - (-1) + 1 = 5.

# dp[i][0 or 1]:
# dp[i][1] -> nums[i] is positive
# dp[i][0] -> nums[i] is negative
# dp[1][1] = max(3, dp[0][0] + 3) = 0+3 = 3
# dp[1][0] = max(-3, dp[0][1] - 3) = -inf-3 = 3

# dp[2][1] = max(4, dp[1][0] + -1) = -inf-1 = 4
# dp[2][0] = max(-4, dp[1][1] - (-1)) = 3 - (-1) = 4

# dp[3][1] = max(1, dp[2][0] + 1) = 1, 5 = 5
# dp[3][0] = max(-1, dp[2][1] - 1) = 1, 3 = 3

# dp[4][1] = max(2, dp[3][0] + 2) = 2, 5
# dp[4][0] = max(-2, dp[3][1] - 2) = 2, 3
