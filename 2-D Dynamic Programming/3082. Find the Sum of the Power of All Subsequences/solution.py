mod = 10**9 + 7
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(i, tot, size):
            if tot == k: return pow(2, n-size, mod)
            if i == n or tot > k: return 0

            x = dfs(i+1, tot, size)
            y = dfs(i+1, tot+nums[i], size+1)
            return (x+y)%mod
        return dfs(0, 0, 0)

    def sumOfPower(self, nums: List[int], k: int) -> int:
        """
        dp[i][_sum] means the number of subsequence of i elements with sum of _sum.
        """
        n = len(nums)
        mod = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for num in nums:
            for _sum in range(k, num - 1, -1):
                for i in range(n, 0, -1):
                    dp[i][_sum] = (dp[i][_sum] + dp[i - 1][_sum - num]) % mod
        return sum(pow(2, n - i, mod) * dp[i][k] for i in range(1, n + 1)) % mod