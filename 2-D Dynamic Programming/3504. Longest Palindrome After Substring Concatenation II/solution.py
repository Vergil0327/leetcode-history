class Solution:
    # leetcode 647
    def checkPalindrome(self, s):
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j]:
                    if length <= 3 or dp[i+1][j-1]:
                        dp[i][j] = True
        return dp

    def longestPalindrome(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        is_palindrome1 = self.checkPalindrome(s)
        is_palindrome2 = self.checkPalindrome(t)

        max_pal_len_s = [1]*m
        for length in range(2, m+1):
            for i in range(m-length+1):
                # check if s[i:i+length] is palindrome
                # if s[i:i+length] == s[i:i+length][::-1]:
                if is_palindrome1[i][i+length-1]:
                    max_pal_len_s[i] = length
        
        max_pal_len_t = [1]*n
        for length in range(2, n+1):
            for j in range(length-1, n):
                i = j-length+1
                # check if t[i:i+length] is palindrome
                # if t[i:j+1] == t[i:j+1][::-1]:
                if is_palindrome2[i][j]:
                    max_pal_len_t[j] = length

        # since dp[i][j] depends on dp[i+1][j-1], we should iterate `i` reversely to update dp[i+1][j-1] first for every dp[i][j]
        dp = [[1]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                if s[i] == t[j]:
                    if i+1<m and j-1>=0:
                        dp[i][j] = max(max_pal_len_s[i], max_pal_len_t[j], 2+dp[i+1][j-1])
                    elif i+1<m:
                        dp[i][j] = max(max_pal_len_s[i], max_pal_len_t[j], 2+max_pal_len_s[i+1])
                    elif j-1>=0:
                        dp[i][j] = max(max_pal_len_s[i], max_pal_len_t[j], 2+max_pal_len_t[j-1])
                    else:
                        dp[i][j] = 2
                    
                else:
                    dp[i][j] = max(max_pal_len_s[i], max_pal_len_t[j])

        return max(dp[i][j] for i in range(m) for j in range(n))