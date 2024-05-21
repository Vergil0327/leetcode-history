class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        s = "#" + s # to 1-indexed
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1

        mod = 10**9 + 7
        for i in range(1, n+1):
            for j in range(i+1):
                if s[i] == "I":
                    for prev in range(j):
                        dp[i][j] += dp[i-1][prev]
                else:
                    for prev in range(j, i):
                        dp[i][j] += dp[i-1][prev]
                dp[i][j] %= mod

        return sum(dp[n]) % mod