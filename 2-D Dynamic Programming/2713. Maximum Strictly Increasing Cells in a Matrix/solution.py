class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        positions = defaultdict(list)
        for i in range(m):
            for j in range(n):
                positions[mat[i][j]].append((i, j))

        dp = [[0] * n for _ in range(m)]
        rowPath = defaultdict(int)
        colPath = defaultdict(int)

        res = 0
        for key in sorted(positions, key=lambda x:-x): # 由大到小
            for row, col in positions[key]:
                dp[row][col] = max(rowPath[row], colPath[col])+1
                res = max(res, dp[row][col])

            for row, col in positions[key]:
                rowPath[row] = max(rowPath[row], dp[row][col])
                colPath[col] = max(colPath[col], dp[row][col])
        return res