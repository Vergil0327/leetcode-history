class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        MOD = int(1e9+7)

        # dp[i][j]: the maximum sum of numeric characters we can collect when reached (i, j)
        dp = [[-inf] * (n+1) for _ in range(m+1)]
        # path[i][j]: the number of paths to maximum path sum we can get to reach (i, j)
        path = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if board[i-1][j-1] == "X": continue
                if board[i-1][j-1] == "E":
                    dp[i][j] = 0
                    path[i][j] = 1
                    continue
                
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

                if dp[i-1][j] == dp[i][j]:
                    path[i][j] += path[i-1][j]
                    path[i][j] %= MOD
                if dp[i][j-1] == dp[i][j]:
                    path[i][j] += path[i][j-1]
                    path[i][j] %= MOD
                if dp[i-1][j-1] == dp[i][j]:
                    path[i][j] += path[i-1][j-1]
                    path[i][j] %= MOD

                score = int(board[i-1][j-1]) if board[i-1][j-1].isdigit() else 0
                dp[i][j] += score
        
        return [dp[m][n], path[m][n]] if dp[m][n] != -inf else [0,0]