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

        for i in range(1, n):

            for num1 in range(nums[i]+1):
                num2 = nums[i]-num1
                if num2 < 0: break

                for prev_num1 in range(min(nums[i-1]-num2, num1)+1):
                    dp[i][num1] += dp[i-1][prev_num1]
                    dp[i][num1] %= mod

        return sum(dp[n-1]) % mod
