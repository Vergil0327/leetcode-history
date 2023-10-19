class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix),len(matrix[0])
        presum_mat = [[0]*n for _ in range(m)]

        for i in range(m):
            tot = 0
            for j in range(n):
                tot += matrix[i][j]
                presum_mat[i][j] = (presum_mat[i-1][j] if i-1>=0 else 0) + tot

        res = 0
        for top in range(m):
            for bot in range(top, m):
                seen = {0: 1}
                for j in range(n):
                    cur = presum_mat[bot][j]-(presum_mat[top-1][j] if top-1>=0 else 0)

                    if cur-target in seen:
                        res += seen[cur-target]
                    seen[cur] = seen.get(cur, 0) + 1
        return res
