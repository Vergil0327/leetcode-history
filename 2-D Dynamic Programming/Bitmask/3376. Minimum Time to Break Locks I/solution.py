
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        # perms = permutations(strength)

        # res = inf
        # for arr in perms:
        #     t = egy = 0
        #     x = 1
        #     for num in arr:
        #         times = ceil(num/x)
        #         egy += x * times
        #         t += times

        #         egy = 0
        #         x += K
        #     res = min(res, t)
        # return res

        n = len(strength)
        
        @cache
        def dfs(x, state):
            if state.bit_count() == n: return 0

            res = inf
            for i in range(n):
                if (state>>i)&1: continue
                res = min(res, dfs(x+K, state | (1<<i)) + ceil(strength[i]/x))
            return res

        return dfs(1, 0)
