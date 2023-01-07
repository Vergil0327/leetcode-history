# Manacher
# maintain P[i], maxRight, maxCenter
# P[i] the longest radius of palindrome centered at i
# maxRight index of longest radious reached
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # [XXXXXXXX ct XXXXXXXX]
        #      j          i  maxR
        t = "#"
        for i in range(len(s)):
            t += s[i]
            t += "#"

        n = len(t)
        maxRight, maxCenter = -1, -1
        P = [0] * n
        maxLen = 0
        for i in range(n):
            r = 0
            if i < maxRight:
                j = 2*maxCenter-i
                r = min(P[j], maxRight-i)
            while i-r >=0 and i+r < n and t[i-r] == t[i+r]:
                r += 1
            
            P[i] = r-1
            # update maxRight, maxCenter
            if i+P[i] > maxRight:
                maxRight = i+P[i]
                maxCenter = i

            if i-P[i] == 0:
                maxLen = max(maxLen, (P[i]*2+1)//2)
        return s[maxLen:][::-1] + s

# KMP
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return s

        pattern = s
        s = s[::-1]

        # KMP Preprocess
        # LPS, longest equal prefix suffix
        n = len(pattern)
        LPS = [0] * n
        LPS[0] = 0
        for i in range(1, n):
            j = LPS[i-1]
            while j > 0 and pattern[j] != pattern[i]:
                j = LPS[j-1]
            LPS[i] = j + (1 if pattern[j] == pattern[i] else 0)

        n = len(s)
        dp = [0] * n
        dp[0] = 1 if pattern[0] == s[0] else 0
        for i in range(1, n):
            j = dp[i-1]
            while j > 0 and pattern[j] != s[i]:
                j = LPS[j-1]
            dp[i] = j + (1 if pattern[j] == s[i] else 0)

        longestSuffixLen = dp[n-1]
        return pattern[longestSuffixLen:][::-1] + pattern