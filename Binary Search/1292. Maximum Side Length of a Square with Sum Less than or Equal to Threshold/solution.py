class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        
        presums = [[0]*(COLS+1) for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(1, COLS+1):
                presums[r][c] = presums[r][c-1] + mat[r][c-1]

        def squareExists(maxLen):
            for r in range(ROWS-maxLen+1):
                for c in range(COLS-maxLen+1):
                    total = 0
                    for i in range(r, r+maxLen):
                        total += presums[i][c+maxLen] - presums[i][c]
                        if total > threshold: break
                    if total <= threshold: return True
            return False

        l, r = 0, min(ROWS, COLS)
        while l < r:
            mid = r - (r-l)//2
            if squareExists(mid):
                l = mid
            else:
                r = mid-1
        return l

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        
        presum2D = [[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(1, ROWS+1):
            for c in range(1, COLS+1):
                presum2D[r][c] = presum2D[r-1][c] + presum2D[r][c-1] - presum2D[r-1][c-1] + mat[r-1][c-1]

        # [[0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 2, 5, 7, 11, 14, 16],
        # [0, 2, 4, 10, 14, 22, 28, 32],
        # [0, 3, 6, 15, 21, 33, 42, 48]]
        def squareExists(maxLen):
            for r in range(ROWS-maxLen+1):
                for c in range(COLS-maxLen+1):
                    SUM = presum2D[r+maxLen][c+maxLen]+presum2D[r][c]-presum2D[r+maxLen][c]-presum2D[r][c+maxLen]
                    if SUM <= threshold: return True
            return False

        l, r = 0, min(ROWS, COLS)
        while l < r:
            mid = r - (r-l)//2
            if squareExists(mid):
                l = mid
            else:
                r = mid-1
        return l