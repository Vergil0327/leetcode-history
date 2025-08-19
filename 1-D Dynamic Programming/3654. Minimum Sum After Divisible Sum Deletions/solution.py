from math import inf

class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        dp = [0] + [inf] * k
        presum = 0
        for num in nums:
            presum += num
            remainder = presum % k
            dp[remainder] = min(dp[remainder], presum)
            presum = min(presum, dp[remainder]) # important! update running prefix sum once we found smaller dp[remainder]
        return presum