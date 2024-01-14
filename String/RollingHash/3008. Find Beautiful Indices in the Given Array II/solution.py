class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        key = lambda ch: ord(ch)-ord("a")

        def rollingHash(s, t):
            P = 31
            MOD = 10**9 + 7
            n, m = len(s), len(t)
            if n < m: return []

            RL = pow(P, m-1, MOD)

            hashT = 0
            for i in range(m):
                hashT = (hashT*P + key(t[i]))%MOD

            indices = []
            h = 0
            for i in range(n):
                if i >= m:
                    h = h - key(s[i-m])*RL
                    h = (h + MOD)%MOD
                h = (h * P + key(s[i]))%MOD
                if n-m >= i-m+1 >= 0 and h == hashT:
                    indices.append(i-m+1)
            return indices

        A, B = rollingHash(s, a), rollingHash(s, b)
        A.sort()
        B.sort()

        res = []
        for i in A:
            r = bisect_right(B, i+k)
            l = bisect_left(B, i-k)
            if r-l > 0:
                res.append(i)
        return res        
        