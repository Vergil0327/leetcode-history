class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = int(1e9+7)

        # dp[i][cnt][last_dice]: the number of distinct sequences that can be obtained with exact i rolls ended with `last_dice` with `cnt` consecutive times
        dp = [[[0]*16 for _ in range(6)] for _ in range(n)]
        for i in range(6):
            dp[0][i][1] = 1

        for i in range(1, n):
            for j in range(6):
                for cnt in range(1, 16):
                    if cnt > rollMax[j]: continue

                    if cnt > 1:
                        dp[i][j][cnt] += dp[i-1][j][cnt-1]
                        dp[i][j][cnt] %= MOD
                    else:
                        for prev in range(6):
                            if prev == j: continue
                            for k in range(1, 16):
                                if k > rollMax[prev]: continue
                                dp[i][j][cnt] += dp[i-1][prev][k]
                        dp[i][j][cnt] %= MOD
               
        total = 0
        for j in range(6):
            for cnt in range(1, 16):
                if cnt > rollMax[j]: continue
                total += dp[n-1][j][cnt]
            total %= MOD
        return total
    
# 不需要用 `if cnt > rollMax[j]: continue`
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = int(1e9+7)

        # dp[i][cnt][last_dice]: the number of distinct sequences that can be obtained with exact i rolls ended with `last_dice` with `cnt` consecutive times
        dp = [[[0]*16 for _ in range(6)] for _ in range(n)]
        for i in range(6):
            dp[0][i][1] = 1

        for i in range(1, n):
            for j in range(6):
                for cnt in range(1, rollMax[j]+1):
                    if cnt > 1:
                        dp[i][j][cnt] += dp[i-1][j][cnt-1]
                        dp[i][j][cnt] %= MOD
                    else:
                        for prev in range(6):
                            if prev == j: continue
                            for k in range(1, rollMax[prev]+1):
                                dp[i][j][cnt] += dp[i-1][prev][k]
                        dp[i][j][cnt] %= MOD
                    
        total = 0
        for j in range(6):
            for cnt in range(1, rollMax[j]+1):
                total += dp[n-1][j][cnt]
            total %= MOD
        return total