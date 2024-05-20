class Solution:
    def waysToReachStair(self, k: int) -> int:
        op1, op2 = 1, 2

        #k <= 10^9
        mx = ceil(log2(10**9))
        power2 = [1] * (mx+1)
        for i in range(mx+1):
            power2[i] = pow(2, i)

        @cache
        def dfs(i, op, jump):
            if i > k+1: return 0 # no way to turn back

            res = 1 if i == k else 0 # keep exploring possible ways even when we already reach k position

            if op == op2: # op1 can't consecutive
                res += dfs(i-1, op1, jump)
            res += dfs(i+power2[jump], op2, jump+1)

            return res

        return dfs(1, op2, 0)

def waysToReachStair(self, k: int) -> int:
        mx = ceil(log2(10**9)) # k <= 10^9
        return sum(comb(jump + 1, (1<<jump) - k) for jump in range(mx) if 1<<jump >= k)