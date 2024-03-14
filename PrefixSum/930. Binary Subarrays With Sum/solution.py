class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        # presum[i]-presum[j] = goal
        # presum[j] = presum[i]-goal
        dp = {0:1}
        res = 0
        for i in range(1, n+1):
            presum[i] = presum[i-1]+nums[i-1]

            if presum[i]-goal in dp:
                res += dp[presum[i]-goal]
            dp[presum[i]] = dp.get(presum[i], 0) + 1
        return res




class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        presum = res = 0
        for num in nums:
            presum += num
            # presum - presumj = goal
            res += count[presum-goal]
            count[presum] += 1
        return res
