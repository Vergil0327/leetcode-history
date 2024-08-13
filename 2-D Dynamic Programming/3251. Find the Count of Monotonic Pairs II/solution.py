class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        mx = max(nums)
        
        dp = [[0]*(mx+1) for _ in range(n)]
        for num1 in range(mx+1):
            num2 = nums[0] - num1
            if num2 >= 0:
                dp[0][num1] = 1
            else:
                break
        presum_dp = [[0]*(mx+1) for _ in range(n)]
        presum_dp[0][0] = dp[0][0]
        for num in range(1, mx+1):
            presum_dp[0][num] = presum_dp[0][num-1] + dp[0][num]

        for i in range(1, n):

            for num1 in range(nums[i]+1):
                num2 = nums[i]-num1
                if num2 < 0: break

                upperbound = min(nums[i-1]-num2, num1)
                # for prev_num1 in range(upperbound+1):
                #     dp[i][num1] += dp[i-1][prev_num1]
                #     dp[i][num1] %= mod

                if upperbound >= 0:
                    dp[i][num1] += presum_dp[i-1][upperbound]
                    dp[i][num1] %= mod
            
            presum_dp[i][0] = dp[i][0]
            for num in range(1, mx+1):
                presum_dp[i][num] = presum_dp[i][num-1] + dp[i][num]

        return sum(dp[n-1]) % mod
