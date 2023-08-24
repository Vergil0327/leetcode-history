class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)

        prefixRollingHash = [0] # 1-indexed
        N = 26
        mod = 10**9 + 7
        for i in range(n):
            ch = ord(s[i])-ord("a")
            prefixRollingHash.append((prefixRollingHash[-1] * N + ch)%mod)

        powmod = [pow(N, i, mod) for i in range(n+1)]
        def getRollingHash(i, length):
            # return (prefixRollingHash[i+length] - prefixRollingHash[i] * pow(N, length, mod) + mod)%mod
            return (prefixRollingHash[i+length] - prefixRollingHash[i] * powmod[length] + mod)%mod

        def check(mid, prefixStart, suffixStart):
            prefix = getRollingHash(prefixStart, mid)
            suffix = getRollingHash(suffixStart, mid)
            return prefix == suffix

        res = 0
        for length in range(1, n+1):
            # prefix: s[:length]
            # suffix: s[n-length:]
            if s[0] != s[n-length]: continue

            l, r = 0, length
            while l < r:
                mid = r - (r-l)//2
                if check(mid, 0, n-length):
                    l = mid
                else:
                    r = mid-1
            res += l
            
        return res
