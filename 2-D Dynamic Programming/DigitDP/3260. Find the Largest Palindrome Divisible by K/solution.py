class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        kmod = [1] * n
        for i in range(1, n):
            kmod[i] = kmod[i-1]*10 % k

        res = [9] * n

        @cache
        def dfs(i, mod):
            if i == (n+1)//2:
                return mod == 0

            for d in range(9, -1, -1):
                res[i] = res[~i] = d
                coeff = sum(kmod[j] for j in {i, n-1-i})
                nxt_mod = (mod + coeff * d) % k
                if dfs(i+1, nxt_mod): return True
            return False
        dfs(0, 0)

        return "".join(map(str, res))
