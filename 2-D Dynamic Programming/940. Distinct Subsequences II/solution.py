class Solution:
    def distinctSubseqII(self, s: str) -> int:
        M = 1_000_000_007

        n = len(s)
        dp = [[0]*26 for _ in range(n)]
        for i in range(n):
            ch = ord(s[i]) - ord("a")
            for c in range(26):
                if c != ch:
                    dp[i][c] = dp[i-1][c]
                    continue

                if i>0:
                    dp[i][c] = sum(dp[i-1]) + 1
                    dp[i][c] %= M
                else:
                    dp[i][c] = 1
        return sum(dp[n-1])%M
    
# 1-D DP
# 由於dp[i]只跟dp[i-1]有關, 我們可以只用一個數組來節省空間
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        M = 1_000_000_007

        n = len(s)

        dp = [0] * 26
        for i in range(n):
            dp[ord(s[i]) - ord("a")] = (sum(dp) + 1)%M
        return sum(dp)%M