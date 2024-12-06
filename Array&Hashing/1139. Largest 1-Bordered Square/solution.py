class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows = [list(accumulate(row, initial=0)) for row in grid]
        cols = [[0]*(m+1) for _ in range(n)]

        for j in range(n):
            for i in range(m):
                cols[j][i+1] = cols[j][i] + grid[i][j]
        
        res = longest = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue

                for length in range(min(m, n)+1, longest-1, -1):
                    if j+length-1 >= n: continue
                    if i+length-1 >= m: continue

                    top = rows[i][j+length] - rows[i][j]
                    bot = rows[i+length-1][j+length] - rows[i+length-1][j]

                    left = cols[j][i+length] - cols[j][i]
                    right = cols[j+length-1][i+length] - cols[j+length-1][i]

                    if top == bot == left == right == length:
                        longest = max(longest, length)
                        res = max(res, length*length)
                        break

        return res