class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        W = "1"
        n = len(floor)

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1]+(1 if floor[i-1] == W else 0)

        totalWhite = presum[n]

        # dp[i][numCarpets]: the maximum number of while tiles that are still visible
        dp = [[totalWhite] * (numCarpets+1) for _ in range(n)]

        for j in range(1, numCarpets+1):
            dp[0][j] = totalWhite-1 if floor[0] == W else totalWhite
        
        for i in range(1, n):
            for j in range(1, numCarpets+1):
                covered = presum[i+1]-presum[max(0, i-carpetLen+1)]
                dp[i][j] = min(dp[i-1][j], (dp[i-carpetLen][j-1] if i-carpetLen >= 0 else totalWhite) - covered)
        
        return min(dp[n-1])
        