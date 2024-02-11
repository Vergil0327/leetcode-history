# KMP
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        
        # KMP preprocess
        # dp[i]: longest common prefix-suffix length of s[0:i)
        dp = [0]*n
        # dp[0] = 0

        for i in range(1, n):
            j = dp[i-1]
            while j >= 1 and s[j] != s[i]:
                j = dp[j-1]
            dp[i] = j + int(s[i] == s[j])
        
        length = dp[n-1]
        return s[:length]
