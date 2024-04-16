class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        # k <= 10^4, 我們要計算C(numFactors+n-1, n-1)
        # 最小的prime factor = 2, 如果k全部由2組成 => numFactors = log2(10^4) < 14
        # 所以C(k+n-1, n-1) = C(k+n-1, k) <= C(10^4+14-1, 14)
        size = ceil(log2(10000))
        m, n = 10000+size+1, size+1
        comb = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            comb[i][0] = 1
            for j in range(1, min(i, n)+1):
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % mod

        res = []
        for n, k in queries:
            ans = 1
            for i in range(2, int(sqrt(k))+1):
                count = 0
                while k%i==0:
                    count += 1
                    k //= i
                ans = ans * comb[count+n-1][count] % mod
            if k > 1:
                ans = ans * comb[1+n-1][1] % mod
            res.append(ans)
        return res