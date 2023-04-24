class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[[0]*26 for _ in range(n)] for _ in range(n)]

        # length = 2
        for i in range(n-1):
            k = ord(s[i])-ord("a")
            if s[i] == s[i+1]:
                dp[i][i+1][k] = 2

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                p, q = ord(s[i])-ord("a"), ord(s[j])-ord("a")
                if s[i] == s[j]:
                    for k in range(26):
                        if p != k:
                            dp[i][j][p] = max(dp[i][j][p], dp[i+1][j-1][k]+2)

                    for k in range(26):
                        if p != k:
                            dp[i][j][k] = dp[i+1][j-1][k]
                else:
                    dp[i][j][p] = dp[i][j-1][p]
                    dp[i][j][q] = dp[i+1][j][q]
                    for k in range(26):
                        if k != p and k != q:
                            dp[i][j][k] = dp[i+1][j-1][k]
        return max(dp[0][n-1])
