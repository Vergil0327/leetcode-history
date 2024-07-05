class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7

        dp = [[[[-1, -1] for _ in range(2)] for _ in range(n)] for _ in range(2)]
        
        def dfs(r, c, leftTop, leftBot):
            if r == 2: return dfs(0, c+1, leftTop, leftBot)
            if c == n: return 1

            if dp[r][c][leftTop][leftBot] == -1:
                dp[r][c][leftTop][leftBot] = dfs(r+1, c, 0 if r == 0 else leftTop, 0 if r == 1 else leftBot)
                if r == 0 and not leftTop:
                    dp[r][c][leftTop][leftBot] += dfs(r+1, c, 1, leftBot)
                if r == 1 and not leftBot:
                    dp[r][c][leftTop][leftBot] += dfs(r+1, c, leftTop, 1)
                dp[r][c][leftTop][leftBot] %= mod
            return dp[r][c][leftTop][leftBot]

        return dfs(0, 0, 0, 0)

class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7

        dp = [0] * (n+2)
        dp[0] = dp[1] = 1
        for i in range(2, n+2):
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= mod
        return (dp[-1] * dp[-1]) % mod
