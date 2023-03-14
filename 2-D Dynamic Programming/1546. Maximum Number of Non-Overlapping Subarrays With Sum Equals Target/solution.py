class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        dp = [0] * (n+1)
        seen = {0: -1}
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            # presum[i]-presum[j-1] == target
            sumj = presum[i]-target
            if sumj in seen:
                dp[i] = max(dp[i], dp[seen[sumj]] + 1)
            
            seen[presum[i]] = i

        return max(dp)

# TLE
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for j in range(1, i+1):
                if presum[i]-presum[j-1] == target:
                    dp[i] = max(dp[i], dp[j-1] + 1)

        return max(dp)
