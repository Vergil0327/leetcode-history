class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[i][j]: how full for j-th glass of i-th row
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        row = [poured]
        nextRow = []
        for i in range(query_row+1):
            nextRow = [0]*(i+2)
            for j in range(i+1):
                if row[j] >= 1: # if it's overflow
                    nextRow[j] += (row[j]-1)/2
                    nextRow[j+1] += (row[j]-1)/2
                    row[j] = 1

            row, nextRow = nextRow, row
        return nextRow[query_glass]