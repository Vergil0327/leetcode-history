class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[1] * n for _ in range(n)]

        for r in range(n):
            for l in range(r-1, -1, -1):
                if s[r] == s[l]:
                    if l+1 > r-1:
                        dp[l][r] = max(dp[l][r], 2)
                    else:
                        dp[l][r] = max(dp[l][r], dp[l+1][r-1] + 2)
                else:
                    dp[l][r] = max(dp[l][r-1], dp[l+1][r])
                
        return dp[0][n-1]
    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [1] * n
        prevdp = [1] * n

        for r in range(n):
            dp[r] = 1
            for l in range(r-1, -1, -1):
                if s[r] == s[l]:
                    if s[r] == s[l]:
                        if l+1 > r-1:
                            # dp[l][r] = max(dp[l][r], 2)
                            dp[l] = max(dp[l], 2)
                        else:
                            # dp[l][r] = max(dp[l][r], dp[l+1][r-1] + 2)
                            dp[l] = max(dp[l], prevdp[l+1] + 2)
                else:
                    # dp[l][r] = max(dp[l][r-1], dp[l+1][r])
                    dp[l] = max(prevdp[l], dp[l+1])
            dp, prevdp = prevdp, dp

        return prevdp[0]