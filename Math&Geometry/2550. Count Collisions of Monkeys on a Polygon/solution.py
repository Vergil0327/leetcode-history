class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = int(1e9+7)
        
        @lru_cache(None)
        def powmod(x, y, MOD):
            if y == 0: return 1
            if y%2 == 0:
                res = powmod(x, y//2, MOD) * powmod(x, y//2, MOD)
                res %= MOD
            else:
                res = x * powmod(x, (y-1)//2, MOD) * powmod(x, (y-1)//2, MOD)
                res %= MOD
            return res
        return (powmod(2, n, MOD)-2+MOD)%MOD

class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = int(1e9+7)
        return (pow(2, n, MOD)-2+MOD)%MOD