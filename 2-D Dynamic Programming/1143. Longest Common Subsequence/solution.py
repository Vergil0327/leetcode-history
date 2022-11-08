class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2: return len(text1)
        
        m, n = len(text1), len(text2)
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m or j == n:
                return 0
            
            longest = 0
            if text1[i] == text2[j]:
                longest = max(longest, 1 + dfs(i+1, j+1))
            else:
                longest = max(longest, dfs(i+1, j)) # keep comparing current text2 with rest of text1
                longest = max(longest, dfs(i, j+1)) # keep comparing current text1 with rest of text2
            return longest
        return dfs(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2: return len(text1)
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)] # dp[m][n]: the length of longest common subsequence of text1[:m] and text2[:n]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                else:
                    
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]