from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        res = ""
        length = inf
        
        r = 0
        i = 0 # pointer of t to check if current subarray s[:r] (r inclusive) contains t
        while r < m:
            ch = s[r]
            r += 1
            if ch == t[i]:
                i += 1

            # find minimum window backwards until window just contains t
            if i == n: # window contains t
                i -= 1
                j = r-1
                while i >= 0:
                    if s[j] == t[i]:
                        i -= 1
                    j -= 1
                i = 0 # i == -1 right now -> reset i to 0.
                
                j += 1
                if r-j < length:
                    length = r-j
                    res = s[j:r]
        return res
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        # dp[i][j]: the minimum length of substring in s[0:i] such that t[0:j] is subsequence of this substring
        dp = [[0] * (n+1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j] + 1 # s[i]對組成t[:j]沒有幫助，從s[:i-1]內找t[:j]
        
        length = inf
        pos = -1
        for i in range(m):
            if dp[i][n] < length:
                length = dp[i][n]
                pos = i

        if length == inf:
            return ""
        else:
            return s[pos-length+1:pos+1]
