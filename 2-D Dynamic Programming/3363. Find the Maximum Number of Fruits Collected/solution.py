class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # (0,0)
        dp1 = sum(fruits[i][i] for i in range(n))

        # (0,n-1)
        dirs2 = [[1,-1],[1,0],[1,1]]
        dp2 = [[0]*n for _ in range(n)]
        dp2[0][n-1] = fruits[0][n-1]
        for r in range(1, n):
            for c in range(r+1, n):
                for dr, dc in dirs2:
                    row, col = r-dr, c-dc
                    if n-1-r < col < n:
                        dp2[r][c] = max(dp2[r][c], dp2[row][col] + fruits[r][c])
        
        # (n-1,0)
        dirs3 = [[-1,1],[0,1],[1,1]]
        dp3 = [[0]*n for _ in range(n)]
        dp3[n-1][0] = fruits[n-1][0]
        for c in range(1, n):
            for r in range(c+1, n):
                for dr, dc in dirs3:
                    row, col = r-dr, c-dc
                    if n-1-c < row < n:
                        dp3[r][c] = max(dp3[r][c], dp3[row][col] + fruits[r][c])

        return dp1 + dp2[n-2][n-1] + dp3[n-1][n-2]
