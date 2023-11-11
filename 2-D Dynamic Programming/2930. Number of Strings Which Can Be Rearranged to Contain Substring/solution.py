class Solution:
    def stringCount(self, n: int) -> int:
        mod = 10**9 + 7
        if n < 4: return 0
        if n == 4: return 12
        
        L, E, T = ord("l")-ord("a"), ord("e")-ord("a"), ord("t")-ord("a")
        dp = [[[[0]*2 for _ in range(3)]for _ in range(2)] for _ in range (n+1)]
        dp[0][0][0][0] = 1
        for i in range(n):
            for l in range(2):
                for e in range(3):
                    for t in range(2):
                        dp[i+1][min(1, l+1)][e][t] += dp[i][l][e][t]
                        dp[i+1][min(1, l+1)][e][t] %= mod
                        
                        dp[i+1][l][min(2, e+1)][t] += dp[i][l][e][t]
                        dp[i+1][l][min(2, e+1)][t] %= mod
                        
                        dp[i+1][l][e][min(1, t+1)] += dp[i][l][e][t]
                        dp[i+1][l][e][min(1, t+1)] %= mod
                        
                        dp[i+1][l][e][t] += dp[i][l][e][t] * 23
                        dp[i+1][l][e][t] %= mod
                        
                        # for ch in range(26):
                        #     if ch == L:
                        #         dp[i+1][min(1, l+1)][e][t] += dp[i][l][e][t]
                        #         dp[i+1][min(1, l+1)][e][t] %= mod
                        #     elif ch == E:
                        #         dp[i+1][l][min(2, e+1)][t] += dp[i][l][e][t]
                        #         dp[i+1][l][min(2, e+1)][t] %= mod
                        #     elif ch == T:
                        #         dp[i+1][l][e][min(1, t+1)] += dp[i][l][e][t]
                        #         dp[i+1][l][e][min(1, t+1)] %= mod
                        #     else:
                        #         dp[i+1][l][e][t] += dp[i][l][e][t]
                        #         dp[i+1][l][e][t] %= mod
        return dp[n][1][2][1]%mod