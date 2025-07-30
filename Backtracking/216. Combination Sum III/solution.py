class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(d, k, n):
            if k == 0 and n == 0:
                return [[]]
            if k <= 0 or n <= 0:
                return None
            
            res = []
            for i in range(d+1, 10):
                arrs = dfs(i, k-1, n-i)
                if arrs is None: continue
                for arr in arrs:
                    arr.append(i)
                res += arrs
            return res
        return dfs(0, k, n)