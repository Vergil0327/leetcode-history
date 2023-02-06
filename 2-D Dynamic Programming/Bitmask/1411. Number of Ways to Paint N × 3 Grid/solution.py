class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = int(1e9+7)

        def valid(color1, color2, color3):
            return color1 != color2 and color2 != color3
    
        # dp[row][(0/1/2, 0/1/2, 0/1/2)], use 0, 1, 2 as red, yellow and green
        # dp[i][color_state]: the ways to paint first i rows by painting this color_state
        dp = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(n)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if valid(i, j, k):
                        dp[0][i][j][k] = 1

        for i in range(1, n):
            for c1 in range(3):
                for c2 in range(3):
                    for c3 in range(3):
                        if not valid(c1, c2, c3): continue

                        for prev1 in range(3):
                            if prev1 == c1: continue
                            for prev2 in range(3):
                                if prev2 == c2: continue
                                for prev3 in range(3):
                                    if not valid(prev1, prev2, prev3): continue
                                    if prev3 == c3: continue
                                    dp[i][c1][c2][c3] = (dp[i][c1][c2][c3] + dp[i-1][prev1][prev2][prev3]) % MOD
        total = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    total = (total + dp[n-1][i][j][k])%MOD
        return total