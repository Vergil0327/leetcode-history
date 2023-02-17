class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)

        dp = [[0] * n for _ in range(n)] # dp[l][r]: the maximum length of a palindrome which exists in s

        # for length = 1, process independently because when length = 1 and l = 0, r = 0 will cause dp[r-1] error
        for l in range(n):
            dp[l][l] = 1

        for length in range(2, n+1):
            for l in range(n-length+1):
                r = l+length-1
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1]+2
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        return n-dp[0][n-1] <= k
