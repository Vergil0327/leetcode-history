mod = 10**9 + 7
class Solution:
    @cache
    def rearrangeSticks(self, n: int, k: int) -> int:
        if n == k: return 1
        if n == 0 or k == 0: return 0

        return (self.rearrangeSticks(n-1, k-1) + self.rearrangeSticks(n-1, k) * (n-1)) % mod

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, min(i, k)+1):
                dp[i][j] += dp[i-1][j-1] + (i-1) * dp[i-1][j]
                dp[i][j] %= mod
        return dp[n][k]