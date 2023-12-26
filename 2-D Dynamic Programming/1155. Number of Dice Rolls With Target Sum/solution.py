class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for t in range(1, target+1):
                for j in range(1, k+1):
                    if t-j >= 0:
                        dp[i][t] += dp[i-1][t-j]
                        dp[i][t] %= 1000000007
        return dp[n][target]

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[[0]*(k+1) for _ in range(target+1)] for _ in range(n)]
        for j in range(1, k+1):
            if j <= target:
                dp[0][j][j] = 1
        for i in range(1, n):
            for t in range(1, target+1):
                for j in range(1, k+1):
                    if t-j >= 0:
                        for k in range(1, k+1):
                            dp[i][t][j] += dp[i-1][t-j][k]
                            dp[i][t][j] %= 1000000007
        return sum(dp[n-1][target])%1000000007