class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, hashValue: int) -> str:
        def val(ch):
            return ord(ch)-ord("a")+1

        n = len(s)
        vals = [val(s[i]) for i in range(n)]
        pks = [pow(p, i, m) for i in range(k)]


        rollingHash = 0
        res = ""
        for i in range(n-1,n-k-1, -1):
            rollingHash += vals[i] * pks[k-(n-1-i)-1]
            rollingHash %= m

        if rollingHash == hashValue:
            res = s[n-k:]

        for i in range(n-k-1, -1, -1):
            rollingHash -= vals[i+k] * pks[k-1]
            rollingHash *= p
            rollingHash += vals[i]
            rollingHash = (rollingHash+m)%m
            if rollingHash == hashValue:
                res = s[i:i+k]
        return res
