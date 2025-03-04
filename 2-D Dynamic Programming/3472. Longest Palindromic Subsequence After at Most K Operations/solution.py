class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(n)]
        def dfs(l, r, k):
            if l==r: return 1
            if l > r: return 0
            if dp[l][r][k] != -1: return dp[l][r][k]

            # skip s[l]
            dp[l][r][k] = dfs(l+1, r, k)
            
            # skip s[r]
            dp[l][r][k] = max(dp[l][r][k], dfs(l, r-1, k))

            # two skip above make all possible (s[l],s[r]) combinations
            # then, we try match them under k operations
            # match s[l], s[r]

            x = ord(s[l])-ord("a")
            y = ord(s[r])-ord("a")
            # ex. x=a, y=z, two directions:
            # 0-25 = -25 = 1
            # 25-0 = 25
            op1 = x-y if x-y >= 0 else x-y+26
            op2 = y-x if y-x >= 0 else y-x+26
            if k >= min(op1, op2):
                dp[l][r][k] = max(dp[l][r][k], dfs(l+1, r-1, k-min(op1, op2))+2)
            return dp[l][r][k]
        return dfs(0, n-1, k)