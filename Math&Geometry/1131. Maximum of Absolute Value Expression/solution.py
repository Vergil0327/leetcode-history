class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        arrs = [[] for _ in range(8)]
        for i, (A,B)  in enumerate(zip(arr1, arr2)):
            arrs[0].append(A+B+i)
            arrs[1].append(A-B+i)
            arrs[2].append(-A+B+i)
            arrs[3].append(-A-B+i)
            arrs[4].append(A+B-i)
            arrs[5].append(A-B-i)
            arrs[6].append(-A+B-i)
            arrs[7].append(-A-B-i)

        res = 0
        for arr in arrs:
            arr.sort()
            res = max(res, arr[-1]-arr[0])
        return res

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        arr = [(arr1[i], arr2[i], i) for i in range(n)]
        res = 0
        for sign in range(1<<3): # 000, 001, 010, 100, ... 1 means positive and 0 means negative
            mx, mn = -inf, inf
            for i in range(n):
                val = 0
                for j in range(3):
                    if (sign>>j)&1:
                        val += arr[i][j]
                    else:
                        val += -arr[i][j]

                mx = max(mx, val)
                mn = min(mn, val)
            res = max(res, mx-mn)
        return res