class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append([grid[i][j], i])
        arr.sort(reverse=True)

        size= len(arr)

        @cache
        def dfs(i, row_state):
            if i == size: return 0

            # skip
            res = dfs(i+1, row_state)

            # pick
            num, row = arr[i]
            if (row_state>>row)&1 == 0:
                # 由於我們已經排過序, 所以我們可以直接利用while-loop跳過重複
                j = i
                while j < size and arr[j][0] == num:
                    j += 1

                res = max(res, dfs(j, row_state | (1<<row)) + num)
            return res
        return dfs(0, 0)
