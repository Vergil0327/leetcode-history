class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        
        dp = [[0]*51 for _ in range(n)]
        for num1 in range(51):
            num2 = nums[0] - num1
            if num2 >= 0:
                dp[0][num1] = 1

        for i in range(1, n):
            # arr1
            for num1 in range(51):
                num2 = nums[i]-num1
                if num2 < 0: continue

                for prev_num1 in range(num1+1):
                    pre_num2 = nums[i-1]-prev_num1
                    if num2 > pre_num2 or pre_num2 < 0: continue
                    dp[i][num1] += dp[i-1][prev_num1]
                    dp[i][num1] %= mod
        return sum(dp[n-1]) % mod
