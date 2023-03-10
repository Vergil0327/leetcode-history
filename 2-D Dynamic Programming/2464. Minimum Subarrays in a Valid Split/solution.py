from math import gcd
from typing import List

class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] : the minimum number of subarrays that we can obtain valid splits in nums[:i]
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for j in range(i, 0, -1):
                if gcd(nums[i-1], nums[j-1]) > 1:
                    dp[i] = min(dp[i], dp[j-1]+1)

        return dp[n] if dp[n]!= float('inf') else -1

# X X X [X X I] 
# [2,6 | 3,4,3]

# X X [X X X I] 
# [2 | 6,3,4,3]
