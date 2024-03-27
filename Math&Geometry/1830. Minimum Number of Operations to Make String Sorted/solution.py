class Solution:
    def makeStringSorted(self, s: str) -> int:
        n = len(s)
        mod = 10**9 + 7

        count = Counter(s)

        fac = [1]*(n+1)
        for i in range(2, n+1):
            fac[i] = fac[i-1]*i%mod

        def inv(x):
            s = 1
            while x > 1:
                s = s * (mod - mod//x) % mod
                x = mod%x
            return s

        res = 0
        for i in range(n):
            numSmaller = 0
            for ch in string.ascii_lowercase:
                if ch >= s[i]: break
                numSmaller += count[ch]

            numPermutations = numSmaller * fac[n-i-1]
            # remove duplicate permutations
            for freq in count.values():
                numPermutations = numPermutations * inv(fac[freq]) % mod

            res = (res + numPermutations) % mod
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
        return res


class Solution:
    def makeStringSorted(self, s: str) -> int:
        counter, prod, res, mod = [0]*26, 1, 0, 1000000007
        for i, c in enumerate(s[::-1], 1):
            idx = ord(c)-ord("a")
            counter[idx] += 1
            res = (res+prod*sum(counter[:idx])//counter[idx])%mod
            prod = prod*i//counter[idx]
        return res
    