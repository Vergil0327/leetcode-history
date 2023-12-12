mod = 10**9 + 7

@cache
def fact(x):
    if x == 0: return 1
    return x * fact(x-1)%mod

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:

        groups = [sick[0], n-1-sick[-1]] # 兩側non-enclosed group的大小
        for i in range(1, len(sick)):
            l, r = sick[i-1], sick[i]
            if (size := r-l-1) > 0:
                groups.append(size)

        res = fact(sum(groups))
        for i, sz in enumerate(groups):
            res *= pow(fact(sz), -1, mod)
            res %= mod

            if i >= 2: # 兩側組內排列只有一種順序
                res *= pow(2, sz-1, mod)
                res %= mod
        return res