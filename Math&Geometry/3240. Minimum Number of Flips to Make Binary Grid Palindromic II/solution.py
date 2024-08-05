class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        step = 0
        for i in range(m//2):
            for j in range(n//2):
                # palindrome => 4 points should be equal
                a = grid[i][j]
                b = grid[i][n-1-j]
                c = grid[m-1-i][j]
                d = grid[m-1-i][n-1-j]

                one_cnt = a+b+c+d
                step += min(one_cnt, 4-one_cnt) # (全轉成0, 全轉成1)

        ones = diff_pair = 0
        if n%2 == 1:
            for i in range(m//2):
                a, b = grid[i][n//2], grid[m-1-i][n//2]
                ones += a+b
                diff_pair += int(a != b)

        if m%2 == 1:
            for j in range(n//2):
                a, b = grid[m//2][j], grid[m//2][n-1-j]
                ones += a+b
                diff_pair += int(a != b)

        if m%2 and n%2:
            step += grid[m//2][n//2]

        if diff_pair == 0 and ones%4 > 0:
            step += 2

        return step+diff_pair
        