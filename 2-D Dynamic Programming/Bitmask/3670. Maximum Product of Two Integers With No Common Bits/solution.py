class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = max(nums)
        k = mx.bit_length()
        MX_STATE = 1<<k
        
        dp = [0] * MX_STATE
        for num in nums:
            dp[num] = num

        for b in range(k):
            for state in range(1, MX_STATE):
                if state & (1<<b):
                    substate = state^(1<<b)
                    if dp[substate] > dp[state]:
                        dp[state] = dp[substate]
        res = 0
        for num in nums:
            res = max(res, num * dp[(MX_STATE-1)^num])
        return res