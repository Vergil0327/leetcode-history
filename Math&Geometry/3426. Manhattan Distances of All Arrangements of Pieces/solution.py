class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        base = comb(m * n - 2, k - 2) % mod
        res = 0
        for d in range(1, n):
            res += d * (n - d) * m * m
        for d in range(1, m):
            res += d * (m - d) * n * n
        return res * base % mod
