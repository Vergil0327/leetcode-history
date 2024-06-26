class Solution:
    def minScoreTriangulation(self, arr: List[int]) -> int:
        n = len(arr)
        
        dp = [[inf] * n for _ in range(n)]

        # length = 1
        for i in range(n):
            dp[i][i] = 0
        # length = 2
        for i in range(n-1):
            dp[i][i+1] = 0

        for length in range(3, n+1):
            for i in range(n-length+1): # j = i+length-1 < n
                j = i+length-1
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j])

        return dp[0][n-1]
