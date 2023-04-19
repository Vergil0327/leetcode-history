class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        # size = n%K + n//K
        # while size >= K:
        #     size = size%K + size//K
        # if size != 1: return -1
        if (n-1)%(K-1) != 0: return -1

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + stones[i-1]

        dp = [[[inf] * (K+1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i][1] = 0 # already 1 pile, cost = 0

        for l in range(2, n+1):
            for i in range(n-l+1): # j = i+l-1 < n
                j = i+l-1

                for k in range(2, K+1):
                    if k > l: break
                    for m in range(i, j):
                        if dp[i][m][1] == inf or dp[m+1][j][k-1] == inf: continue
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m+1][j][k-1])
                # dp[i][j][1] = dp[i][j][k] + sum(stones[i:j+1])
                if dp[i][j][K] != inf:
                    dp[i][j][1] = dp[i][j][K] + presum[j+1] - presum[i]
        
        return dp[0][n-1][1]