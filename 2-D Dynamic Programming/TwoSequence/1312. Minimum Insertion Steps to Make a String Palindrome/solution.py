class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n+1):
            for l in range(n-length+1): # l+length-1 = r < n
                r = l+length-1
                if s[l] == s[r]:
                    dp[l][r] = max(dp[l][r], dp[l+1][r-1]+2)
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])

        return n-dp[0][n-1]

# dp[l][r]: the maximum insertion to make `s` as a palindrome
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        dp = [[0]*n for _ in range(n)]

        # for length=1
        # for i in range(n):
        #     dp[i][i] = 0

        for length in range(2, n+1):
            for l in range(n-length+1): # l+length-1 = r < n
                r = l+length-1
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1]
                else:
                    dp[l][r] = min(dp[l+1][r]+1, dp[l][r-1]+1)

        return dp[0][n-1]

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        t = s[::-1]

        # 我們dp用1-indexed
        dp = [[inf] * (n+1) for _ in range(n+1)]

        # 字串也配合狀態轉移改成1-indexed
        s = "#" + s
        t = "#" + t

        # base case
        dp[0][0] = 0
        for i in range(1, n+1):
            dp[0][i] = i # s為"", 跟t[:i]的SCS的最短長度為 i
            dp[i][0] = i # s[:i], 跟t=""的SCS長度為i

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[n][n] - n