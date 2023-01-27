class Solution:
    def strangePrinter(self, s):
        memo = {}
        def dfs(l, r):
            if l > r: return 0
            if (l, r) not in memo:
                res = dfs(l+1, r) + 1
                for k in range(l+1, r+1):
                    if s[k] == s[l]:
                        res = min(res, dfs(l, k-1) + dfs(k+1, r))
                memo[(l, r)] = res
            return memo[(l, r)]

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[inf] * n for _ in range(n)]

        # base case: length = 1
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n+1):
            for i in range(n-length+1): # j = i+length-1 < n
                j = i + length -1
                # k 代表打印的最後一個字符，從i一路印到k
                for k in range(i, j+1):
                    if s[k] == s[i]:
                        # [X] XXXXXXXX, 右端點不可以小於左端點，如果小於，代表至少要打印第k的字符
                        left = dp[i][k-1] if k-1 >= i else 1
                        # XXXXXXXXX [], 左端點不可以大於右端點，如果大於，代表右邊沒有字符需要印
                        right = dp[k+1][j] if k < j else 0

                        dp[i][j] = min(dp[i][j], left + right)
        
        return dp[0][n-1]