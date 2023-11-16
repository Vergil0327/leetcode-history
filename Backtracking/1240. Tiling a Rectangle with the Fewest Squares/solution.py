class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m: return 1

        res = m*n
        def dfs(height, used_blocks):
            nonlocal res
            if all(h == n for h in height):
                res = min(res, used_blocks)
                return

            if used_blocks >= res: return

            min_height = min(height)
            idx = height.index(min_height)
            
            r = idx+1
            while r < m and height[r] == min_height:
                r += 1

            max_possible_square = min(r-idx, n-min_height)
            for i in range(max_possible_square, 0, -1):
                new_height = height.copy()
                for j in range(i):
                    new_height[idx+j] += i
                dfs(new_height, used_blocks+1)
        dfs([0]*m, 0)
        return res
