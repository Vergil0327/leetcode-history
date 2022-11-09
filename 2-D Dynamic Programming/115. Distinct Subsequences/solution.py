# Explanation: https://www.youtube.com/watch?v=-Q6XfyMiYUc

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # use dfs to explore all the possibility
        # i is index at s and j is index at t, keep comparing s[i:] and t[j:]
        @functools.lru_cache(None)
        def dfs(i, j):
            if j == n: return 1 # found matched
            if i == m: return 0
            
            num = dfs(i+1, j) # skip current character and compare rest of s and t
            if s[i] == t[j]: # take current character if valid and keep comparing rest of s and t
                num += dfs(i+1, j+1)
            return num
        
        return dfs(0, 0)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[i][j]: number of distinct subsequences of s[:i] which equals to t[:j]
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Base Case
        # dp[0][j] = 0, j from 0 to n # s = "", t = "XXXX"
        for i in range(1, m+1): # s = "XXXXX", t = ""
            dp[i][0] = 1
        dp[0][0] = 1 # s = "", t = ""

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[m][n]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[i][j]: number of distinct subsequences of s[:i] which equals to t[:j]
        # dp = [[0] * (n+1) for _ in range(m+1)]
        dp = [0] * (n+1)
        prev = [0] * (n+1)

        # Base Case
        # dp[0][j] = 0, j from 0 to n # s = "", t = "XXXX"
        # for i in range(1, m+1): # s = "XXXXX", t = ""
        #     dp[i][0] = 1
        # dp[0][0] = 1 # s = "", t = ""
        dp[0] = prev[0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                # dp[i][j] = dp[i-1][j]
                dp[j] = prev[j]
                if s[i-1] == t[j-1]:
                    # dp[i][j] += dp[i-1][j-1]
                    dp[j] += prev[j-1]
            dp, prev = prev, dp
        return prev[n]