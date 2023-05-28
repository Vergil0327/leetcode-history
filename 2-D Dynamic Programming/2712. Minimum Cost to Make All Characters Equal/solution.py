class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        dp = [[inf]*2 for _ in range(n+2)]
        dp[0][0] = dp[0][1] = 0
        
        dp2 = [[inf]*2 for _ in range(n+2)]
        dp2[n+1][0] = dp2[n+1][1] = 0
        
        s = "#" + s
        
        for i in range(1, n+1):
            if s[i] == "0":
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][0]+i
            else:
                dp[i][1] = dp[i-1][1]
                dp[i][0] = dp[i-1][1]+i
        
        for i in range(n, 0, -1):
            if s[i] == "0":
                dp2[i][0] = dp2[i+1][0]
                dp2[i][1] = dp2[i+1][0]+n+1-i
            else:
                dp2[i][1] = dp2[i+1][1]
                dp2[i][0] = dp2[i+1][1]+n-i+1

        res = inf
        for i in range(1, n+1):
            res = min(res, dp[i][0] + dp2[i][0])
            res = min(res, dp[i][1] + dp2[i][1])
        
        return res
