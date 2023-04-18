class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9+7

        @cache
        def dfs(l, r):
            if l > r: return 0
            if l == r: return 1

            res = 0
            for ch in "abcd":
                i, j = l, r
                while i <= r and s[i] != ch:
                    i += 1
                while j >= l and s[j] != ch:
                    j -= 1
                if i == j:
                    res += 1
                elif i < j:
                    res += dfs(i+1, j-1) + 2
            return res%MOD
        return dfs(0, len(s)-1)


# Chat-GPT4 Solution
class Solution:
    def countPalindromicSubsequences(self, s):
        n = len(s)
        mod = 10**9 + 7
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    left, right = i+1, j-1
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1
                    if left > right:
                        dp[i][j] = dp[i+1][j-1] * 2 + 2
                    elif left == right:
                        dp[i][j] = dp[i+1][j-1] * 2 + 1
                    else:
                        dp[i][j] = dp[i+1][j-1] * 2 - dp[left+1][right-1]
                        # dp[left+1][right-1] 跟s[i], s[j]組合成palindromic subseq
                        # 以及跟s[left], s[right]組合的結果是一樣的
                        # 所以我們要扣掉重複的部分
                        # X ... X {dp[l+1][r-1]} X ... X
                        # i     l                r     j
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                dp[i][j] = (dp[i][j] + mod) % mod
        return dp[0][n-1]
