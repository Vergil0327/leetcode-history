class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]: the number of ways to decode s[:i]
        # numDecodings(s) = numDecodings(s[0:-1]) + numDecodings(s[0:-2])
        # => dp[i] = dp[i-1] + dp[i-2] if s[i-1]s[i] are valid
        n = len(s)
        
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            # number of decodings considering single character "X"
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
            
            # num of decodings considering two characters "XY"
            if i>1:
                if s[i-2] == "1" or (s[i-2] == "2" and s[i-1] in "0123456"):
                    dp[i] += dp[i-2]
        return dp[n]

# Space Optimized
# since our dp[i] only depends on dp[i-1] and dp[i-2]
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]: the number of ways to decode s[:i]  
        # dp[i] = dp[i-1] + dp[i-2]
        n = len(s)
        
        dp = [0] * (n+1)
        dp[0] = 1
        
        dp1, dp2 = 1, 0 if s[0] == "0" else 1
        if n==1: return dp2
        
        for i in range(2, n+1):
            dp = 0
            # number of decodings considering single character "X"
            if s[i-1] != "0":
                dp = dp2
            else:
                dp = 0
            
            # num of decodings considering two characters "XY"
            if i>1:
                if s[i-2] == "1" or (s[i-2] == "2" and s[i-1] in "0123456"):
                    dp += dp1
            dp1, dp2 = dp2, dp
        return dp

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        # s[i:]
        @functools.lru_cache(None)
        def dfs(i):
            if i == n: return 1
            
            # keep comparing character by character
            result = dfs(i+1) if s[i] != "0" else 0
            
            if i < n-1:
                if s[i] == "1" or (s[i] == "2" and s[i+1] not in {"7", "8", "9"}):
                    result += dfs(i+2) # keep comparing two characters with next two characters
            return result
        return dfs(0)