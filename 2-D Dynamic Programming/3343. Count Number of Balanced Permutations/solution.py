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

# 2 <= num.length <= 80
m = n = 81
comb = [[0]*n for _ in range(m)]

for i in range(m):
    comb[i][i] = comb[i][0] = 1
    for j in range(1, i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

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
                res += comb[odd][cnt] * comb[even][evenCnt] * dfs(digit+1, odd-cnt, even - evenCnt, balance + digit * (cnt - evenCnt))
                res %= mod
            return res
        return dfs(0, n-n//2, n//2, 0)