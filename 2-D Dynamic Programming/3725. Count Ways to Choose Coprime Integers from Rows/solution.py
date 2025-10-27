from math import gcd


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        mod = 10**9 + 7

        @cache
        def dfs(i, GCD):
            if i >= m: return int(GCD == 1)
            
            res = 0
            for j in range(n):
                res += dfs(i+1, gcd(GCD, mat[i][j]))
                res %= mod
            return res
        
        res = 0
        for j in range(n):
            res += dfs(1, mat[0][j])
            res %= mod
        return res
