class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        M = 10**9 + 7
        num = 1
        while num**x < n:
            num += 1
        
        dp = [[-1]*(num+1) for _ in range(n+1)]
        def dfs(_sum, num):
            if _sum == n: return 1
            if num ** x > n: return 0
            if _sum > n: return 0
            if dp[_sum][num] != -1: return dp[_sum][num]
            
            res = 0
            res = (res + dfs(_sum + num**x, num+1))%M
            res = (res + dfs(_sum, num+1))%M

            dp[_sum][num] = res
            return res
            
        return dfs(0, 1)
    
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        
        num = 1
        mod = 10**9 + 7
        while (v := pow(num, x)) <= n:
            for _sum in range(n, v - 1, -1):
                dp[_sum] = (dp[_sum] + dp[_sum - v]) % mod
            num += 1
        return dp[n]