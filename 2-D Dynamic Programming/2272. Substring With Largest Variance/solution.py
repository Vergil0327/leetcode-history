class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        characters = list(set(s))

        res = 0
        for ch1 in characters:
            for ch2 in characters:
                if ch1 == ch2: continue # must any 2 characters present in the string

                # dp = [[-inf, -inf] for _ in range(n)]
                # dp[0][0] = 1 if s[0] == ch1 else 0
                # dp[0][1] = -1 if s[0] == ch2 else -inf
                # for i in range(1, n):
                #     if s[i] == ch1:
                #         dp[i][0] = dp[i-1][0]+1
                #         dp[i][1] = dp[i-1][1]+1
                #     elif s[i] == ch2:
                #         dp[i][0] = 0
                #         dp[i][1] = max(dp[i-1][0]-1, dp[i-1][1]-1)
                #     else:
                #         dp[i][0] = dp[i-1][0] + 0
                #         dp[i][1] = dp[i-1][1] + 0
                    
                #     res = max(res, dp[i][1])

                dp0, dp1 = 0, -inf
                for i in range(n):
                    if s[i] == ch1:
                        dp1 = dp1+1
                        dp0 = dp0+1
                    elif s[i] == ch2:
                        dp1 = max(dp0, dp1)-1
                        dp0 = 0
                    res = max(res, dp1)
        return res
