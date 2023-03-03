class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # dp[i][lane, 1,2,3]: the minimum side jump at position `i` with lane `j`
        n = len(obstacles)
        dp = [[inf]*4 for _ in range(n)]
        
        dp[0][1] = 1
        dp[0][2] = 0
        dp[0][3] = 1

        for i in range(1, n):
            currMin = inf
            for lane in range(1, 4):
                if lane == obstacles[i]: continue
                dp[i][lane] = dp[i-1][lane]
                currMin = min(currMin, dp[i][lane])

            for lane in range(1, 4):
                if lane == obstacles[i]: continue
                dp[i][lane] = min(dp[i][lane], currMin+1)
        return min(dp[n-1])