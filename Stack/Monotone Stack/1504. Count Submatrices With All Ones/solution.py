# O(M*M*N)
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        res = 0
        for i in range(m):
            height = [0] * n
            for j in range(i, m):
                for k in range(n):
                    if mat[j][k] == 0:
                        height[k] = 0
                    else:
                        height[k] += 1

                # 計算0到n這段有多少高度為h的合法矩形
                h = j-i+1
                cnt = width = 0
                for k in range(n):
                    if height[k] != h:
                        width = 0
                    else:
                        width += 1
                    cnt += width
                res += cnt
        return res
    
# O(MN)
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        def histogram(arr):
            n = len(arr)
            counter = [0]*n
            stack = []

            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()

                if stack:
                    idx = stack[-1]
                    counter[i] = counter[idx]
                    counter[i] += arr[i] * (i-idx)
                else:
                    counter[i] = arr[i] * (i+1) # 0-indexed
                stack.append(i)
            return sum(counter)

        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            res += histogram(heights)
        return res