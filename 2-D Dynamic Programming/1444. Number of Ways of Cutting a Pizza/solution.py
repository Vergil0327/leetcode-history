class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        MOD = int(1e9+7)
        ROWS, COLS = len(pizza), len(pizza[0])

        squareSum = [[0] * (COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            for c in range(COLS):
                squareSum[r+1][c+1] = squareSum[r+1][c] + squareSum[r][c+1] + (1 if pizza[r][c] == "A" else 0) - squareSum[r][c]

        def hasApple(r1, c1, r2, c2):
            return 1 if squareSum[r2+1][c2+1] - squareSum[r2+1][c1] - squareSum[r1][c2+1] + squareSum[r1][c1] > 0 else 0

        cache = {}
        def dfs(r, c, k):
            if k == 0: return hasApple(r, c, ROWS-1, COLS-1)

            key = (r,c,k)
            if key in cache: return cache[key]

            res = 0
            for row in range(r, ROWS-1):
                res += hasApple(r, c, row, COLS-1) * dfs(row+1, c, k-1)
                res %= MOD

            for col in range(c, COLS-1):
                res += hasApple(r, c, ROWS-1, col) * dfs(r, col+1, k-1)
                res %= MOD

            cache[key] = res % MOD
            return cache[key]

        return dfs(0, 0, K-1)

# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/solutions/2677389/python3-space-optimized-bottom-up-dp-o-k-r-c-r-c-time-o-r-c-space/
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        
        # first, need way to query if a section contains an apple given a top left (r1, c1) and bottom right (r2, c2)
        # we can do this in constant time by keeping track of the number of apples above and to the left of any given cell
        apples = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            apples_left = 0
            for col in range(cols):
                if pizza[row][col] == 'A':
                    apples_left += 1
                apples[row][col] = apples[row-1][col] + apples_left
              
        # query if there is an apple in this rectangle using the prefix sums
        def has_apple(r1, c1, r2 = rows-1, c2 = cols-1) -> bool:
            if r1 > r2 or c1 > c2:
                return False
            tot = apples[r2][c2]
            left_sub = apples[r2][c1-1] if c1 > 0 else 0
            up_sub = apples[r1-1][c2] if r1 > 0 else 0
            upleft_sub = apples[r1-1][c1-1] if r1 > 0 < c1 else 0
            in_rect = tot - left_sub - up_sub + upleft_sub
            return in_rect > 0
        
        # memory optimized dp, keep track of only one matrix of rows x cols
        # bc we only need to access the values at the previous number of cuts
        dp = [[1 if has_apple(r, c) else 0 for c in range(cols + 1)] for r in range(rows + 1)]
        
        for cuts in range(1, k):
            new_dp = [[0] * (cols + 1) for _ in range(rows + 1)]
            for row in range(rows-1, -1, -1):
                for col in range(cols-1, -1, -1):
                    
                    for r2 in range(row, rows):
                        if has_apple(row, col, r2):
                            new_dp[row][col] += dp[r2+1][col]
                            
                    for c2 in range(col, cols):
                        if has_apple(row, col, rows-1, c2):
                            new_dp[row][col] += dp[row][c2+1]
            dp = new_dp
                            
        return dp[0][0] % (10**9 + 7)