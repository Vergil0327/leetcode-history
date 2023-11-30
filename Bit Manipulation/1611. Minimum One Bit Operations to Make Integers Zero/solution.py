class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        dp = [1]
        k = 1
        while pow(2, k) <= n:
            dp.append(pow(2, k) + dp[-1])
            k += 1

        res = 0
        while n:
            lsb = n & -n

            k = int(log2(lsb))
            res = dp[k] - res

            n -= lsb
        return res

