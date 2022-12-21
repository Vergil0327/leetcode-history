class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)

        # build dp
        # dp[i][ch] = dp[state][character] = next transfer state
        # default value: 0 which means back to state 0 (to index 0 of needle)
        dp = [[0] * 256 for _ in range(m+1)]
        
        # base case
        dp[0][ord(needle[0])] = 1

        # prev longest prefix state
        prevLPS = 0
        for i in range(1, m): # i == 0 is base case
            for ch in range(256): # ASCii Code: 0-255
                if ch == ord(needle[i]):
                    # transfer state forward
                    dp[i][ch] = i+1
                else:
                    dp[i][ch] = dp[prevLPS][ch]
            # update prevLPS
            # next time if we meet needle[i] character, we'll know where prevLPS should go
            prevLPS = dp[prevLPS][ord(needle[i])]

        # search
        j = 0
        for i in range(n):
            j = dp[j][ord(haystack[i])]
            if j == m:
                return i-m+1 # first index, haystack[i-m+1:i+1] == needle
        return -1
