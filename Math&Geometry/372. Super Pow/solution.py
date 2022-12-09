MOD = 1337
class Solution:
    # (a*b)%k = (a%k)(b%k)%k
    def powmod(self, a, power):
        a %= MOD

        res = 1
        for _ in range(power):
            res *= a
            res %= MOD
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        if not b: return 1

        last = b.pop()
        x = self.powmod(a, last)
        y = self.powmod(self.superPow(a, b), 10)
        return (x * y) % MOD

MOD = 1337
class BetterSolution:
    # (a*b)%k = (a%k)(b%k)%k
    def powmod(self, a, power):
        if power == 0: return 1
        
        a %= MOD
        if power&1: # power is odd
            return (a * self.powmod(a, power-1)) % MOD
        else: # power is even
            x = self.powmod(a, power//2)
            return (x * x) % MOD

    def superPow(self, a: int, b: List[int]) -> int:
        if not b: return 1

        last = b.pop()
        x = self.powmod(a, last)
        y = self.powmod(self.superPow(a, b), 10)
        return (x * y) % MOD