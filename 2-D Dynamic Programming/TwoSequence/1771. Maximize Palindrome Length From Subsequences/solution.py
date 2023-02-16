class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        words = word1 + word2
        N = len(words)

        # dp[l][r]: the length of longest palindrome with words[l:r]
        dp = [[0] * N for _ in range(N)]

        # handle length=1 independently because of out-of-key error of [r-1] if length=1 and l=0
        for i in range(N):
            dp[i][i] = 1

        res = 0
        for length in range(2, N+1):
            for l in range(N-length+1): # r = l+length-1 < N
                r = l+length-1
                if words[l] == words[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                    if l < len(word1) and r >= len(word1): # check if l in word1 and r in word2
                        res = max(res, dp[l][r])
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        return res
