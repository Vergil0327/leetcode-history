# dp[l][r]: the maximum length of palindrome which exists in s[l:r]
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        dp = [[0]*n for _ in range(n)]

        # for length=1 to prevent key-out-of-bound error
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