class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7

        # 有一個 111...111, 全1
        num1 = (1<<p)-1

        # 最低位是0
        # 個數有 2^(p-1) - 1個
        num2 = num1-1

        # return num1 * pow(num2, (1<<(p-1)) - 1, mod) % mod # python standard library: math.pow
        return num1 * self.powmod(num2, (1<<(p-1)) - 1, mod) % mod

    def powmod(self, base, power, M):
        if power == 0: return 1

        # 3^4 = (3^2)^2 = (3*3)^2
        # 3^5 = 3^4 * 3 = (3*3)^2 * 3
        num = self.powmod(base, power//2, M)
        return num * num % M if power%2 == 0 else num * num * base % M
