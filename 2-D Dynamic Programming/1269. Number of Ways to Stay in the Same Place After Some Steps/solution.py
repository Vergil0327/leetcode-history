class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = arrLen
        mod = 10**9 + 7

        dp = [[0]*(min(steps//2+1, n)+1) for _ in range(steps+1)]
        dp[0][0] = 1

        for i in range (1, steps+1):
            for pos in range(min(steps//2+1, n)):
                dp[i][pos] = ((dp[i-1][pos-1] if pos-1 >= 0 else 0) + 
                              dp[i-1][pos] + 
                              (dp[i-1][pos+1] if pos+1 < n else 0))
                dp[i][pos] %= mod
        
        return dp[steps][0]

class Solution_TLE:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = arrLen
        mod = 10**9 + 7

        dp = [[0]*n for _ in range(steps+1)]
        dp[0][0] = 1

        for i in range (1, steps+1):
            for pos in range(n):
                dp[i][pos] = ((dp[i-1][pos-1] if pos-1 >= 0 else 0) + 
                              dp[i-1][pos] + 
                              (dp[i-1][pos+1] if pos+1 < n else 0))
                dp[i][pos] %= mod
        
        return dp[steps][0]