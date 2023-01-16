class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n) for _ in range(n)]
        for r1,c1,r2,c2 in queries:
            for r in range(r1, r2+1):
                mat[r][c1] += 1
                if c2+1 < n:
                    mat[r][c2+1] -= 1
                    
        for r in range(n):
            for c in range(n):
                if c > 0:
                    mat[r][c] += mat[r][c-1]
        return mat

# Optimized - 2D difference array

# method 1
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff2D = [[0] * (n+1) for _ in range(n+1)]
        # Principle of inclusion and exclusion 排容原理
        for r1, c1, r2, c2 in queries:
            diff2D[r1][c1] += 1     # top-left
            diff2D[r1][c2+1] -= 1   # right-portion
            diff2D[r2+1][c1] -= 1   # bottom-portion
            diff2D[r2+1][c2+1] += 1 # bottom-right

        # method 1, sweepline on rows then sweepline on cols
        for i in range(1, n+1):
            for j in range(n+1):
                diff2D[i][j] = diff2D[i][j] + diff2D[i-1][j]
        for i in range(n+1):
            for j in range(1, n+1):
                diff2D[i][j] = diff2D[i][j] + diff2D[i][j-1]
        
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = diff2D[i][j] # method 1
        return res

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff2D = [[0] * (n+1) for _ in range(n+1)]
        # Principle of inclusion and exclusion 排容原理
        for r1, c1, r2, c2 in queries:
            diff2D[r1][c1] += 1     # top-left
            diff2D[r1][c2+1] -= 1   # right-portion
            diff2D[r2+1][c1] -= 1   # bottom-portion
            diff2D[r2+1][c2+1] += 1 # bottom-right

        result = [[0] * (n+1) for _ in range(n+1)]

        # method 2
        result[0][0] = diff2D[0][0]
        for i in range(n):
            for j in range(n):
                top = result[i-1][j] if i-1 >=0 else 0
                left = result[i][j-1] if j-1 >= 0 else 0
                topleft = result[i-1][j-1] if i-1 >=0 and j-1 >=0 else 0
                result[i][j] = top + left - topleft + diff2D[i][j]
        
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = result[i][j] # method 2
        return res