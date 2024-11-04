class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        mod = 10**9 + 7

        count = Counter(map(int, num))
        total = sum(k*v for k, v in count.items())
        if total%2 != 0: return 0

        @cache
        def dfs(digit, odd, even, balance):
            if digit >= 10:
                return int(odd == 0 and even == 0 and balance == 0)
            if odd < 0 or even < 0: return 0

            res = 0
            for cnt in range(0, count[digit]+1):
                evenCnt = count[digit]-cnt
                res += comb(odd, cnt) * comb(even, evenCnt) * dfs(digit+1, odd-cnt, even - evenCnt, balance + digit * (cnt - evenCnt))
                res %= mod
            return res
        return dfs(0, n-n//2, n//2, 0)
