class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 1e9+7
        
        n = len(s)
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        if s[0] == "*":
            dp[1] *= 9
        if n == 1: return dp[1]

        for i in range(2, n+1):
            if s[i-1] == "*":
                dp[i] += dp[i-1]*9
            elif s[i-1] != "0":
                dp[i] += dp[i-1]*1
                
            if i>1:
                if s[i-2] == "*" and s[i-1] == "*":
                    dp[i] += dp[i-2]*15
                elif s[i-2] == "*" and s[i-1] not in {"7", "8", "9"}:
                    dp[i] += dp[i-2]*2
                elif s[i-2] == "*":
                    dp[i] += dp[i-2]
                elif s[i-2] == "2" and s[i-1] == "*":
                    dp[i] += dp[i-2]*6
                elif s[i-2] == "2" and s[i-1] not in {"7", "8", "9"}:
                    dp[i] += dp[i-2]
                elif s[i-2] == "1" and s[i-1] == "*":
                    dp[i] += dp[i-2]*9
                elif s[i-2] == "1":
                    dp[i] += dp[i-2]
                    
            dp[i] = int(dp[i] % MOD)

        return dp[n]
"""
Video Explanation: https://www.youtube.com/watch?v=fUB-_KggU9w

Analysis

definition: dp[i] = the number of ways to decode s[:i]

    initial value of dp[i] is 0
    [XXXXXX]: represent already solved subproblem, dp[i-1]

    dp[i] += dp[i-1]*1 if valid, s[i] == 0-9, else 0
    [XXXXXX] 1
    [XXXXXX] 2
    dp[i-1]  s[i]
    
    dp[i] += dp[i-1]*9 since * represent 1-9, each way becomes 9 possible way
    [XXXXXX] *

    dp[i] += dp[i-2] * 1 if valid else 0
    [XXXXX] [1, 0-9]
    [XXXXX] [2, 0-6]
    [XXXXX] [3, ] invalid
    
    dp[i] += dp[i-2]*9
    [XXXXX] [1, *]
    
    dp[i] += dp[i-2]*6
    [XXXXX] [2, *]
    
    dp[i] += dp[i-2]*0
    [XXXXX] [3, *]
    
    dp[i] += dp[i-2] * 2 because * can be both 1 and 2
    [XXXXX] [*, 0-6] valid for 10~16 & 20~26
	
	    dp[i] += dp[i-2] * 1 because * can only be 1
    [XXXXX] [*, 7-9] valid for 17~19
    
    dp[i] += dp[i-2] * 15
    [XXXXX] [*, *] 11~19 & 21~26
"""