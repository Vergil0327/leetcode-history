class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        mod = 1_000_000_007

        # Sum of nums does not exceed 2 * 10^4
        # => we create 10^5 space for dp[i]
        # dp[i]: the number of ways to sum up i
        # dp[0] = 1 => one way for empty set
        dp = [0] * (r+1)
        dp[0] = 1

        count = Counter(nums)

        for num, freq in count.items():
            presum_dp = dp.copy()
            for i in range(r+1):
                if i >= num:
                    presum_dp[i] += presum_dp[i-num]
                    presum_dp[i] %= mod

            for i in range(r+1):
                if num > 0:
                    j = i - (freq+1)*num
                    dp[i] = presum_dp[i] - (presum_dp[j] if j>=0 else 0)
                else:
                     dp[i] *= freq+1
                     dp[i] %= mod
        
        return sum(dp[l:r+1])%mod

