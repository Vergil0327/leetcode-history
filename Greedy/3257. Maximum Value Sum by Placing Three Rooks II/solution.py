class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        best3_in_rows = [nlargest(3, [(board[i][j], i, j) for j in range(n)]) for i in range(m)]
        best3_in_cols = [nlargest(3, [(board[i][j], i, j) for i in range(m)]) for j in range(n)]

        arr = list(set(chain(*best3_in_rows)) & set(chain(*best3_in_cols)))
        arr = nlargest(11, arr)
        
        res = -3 * 10**9 - 1
        for i in range(len(arr)):
            val1, r1, c1 = arr[i]
            for j in range(i+1, len(arr)):
                val2, r2, c2 = arr[j]
                if r2 == r1 or c2 == c1: continue
                for k in range(j+1, len(arr)):
                    val3, r3, c3 = arr[k]
                    if r3 == r1 or r3 == r2 or c3 == c1 or c3 == c2: continue
                    res = max(res, val1+val2+val3)

        return res