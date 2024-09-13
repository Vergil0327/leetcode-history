class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        if m < n:
            def findMaxIndex(col):
                idx = mx = -1
                for i in range(m):
                    if mat[i][col] > mx:
                        mx = mat[i][col]
                        idx = i
                return idx

            l, r = 0, n-1
            while l <= r:
                mid = l + (r-l)//2
                
                mxRowIdx = findMaxIndex(mid)
                left, right = mat[mxRowIdx][mid-1] if mid-1 >= 0 else -1, mat[mxRowIdx][mid+1] if mid+1 < n else -1

                if mat[mxRowIdx][mid] > left and mat[mxRowIdx][mid] > right:
                    return [mxRowIdx, mid]
                elif mat[mxRowIdx][mid] < left:
                    r = mid-1
                else:
                    l = mid+1
        else:
            def findMaxIndex(row):
                idx = mx = -1
                for i in range(n):
                    if mat[row][i] > mx:
                        mx = mat[row][i]
                        idx = i
                return idx

            l, r = 0, m-1
            while l <= r:
                mid = l + (r-l)//2

                mxColIdx = findMaxIndex(mid)
                top = mat[mid-1][mxColIdx] if mid-1 >= 0 else -1
                bot = mat[mid+1][mxColIdx] if mid+1 < m else -1

                if mat[mid][mxColIdx] > top and mat[mid][mxColIdx] > bot:
                    return [mid, mxColIdx]
                elif mat[mid][mxColIdx] < top:
                    r = mid-1
                else:
                    l = mid+1
        return [-1, -1]