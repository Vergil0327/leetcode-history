# Intuition

實際上這題是知名的[Z-function algorithm](https://cp-algorithms.com/string/z-function.html), 可以用O(n)時間解
但太技術性所以沒特別研究

from description, the total scores is:

```
iterate length from 1 to n:
    score += longestCommonLength(prefix, suffix)
```

```
s = X X X X X X [X X X X X X]
                 j         i
```

for `def longestCommonLength`, we can use binary search to find longest common length

```py
l, r = 0, length
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```

but how to check `mid` length common prefix in O(1)?

```
s = X X X X X X X X X X X X
                j         i
```

think **prefix sum** and **rolling hash**.

if we use N-system rolling hash
`rolling hash of s[j:i] = (prefix rolling hsah of s[:i]) - (prefix rolling hash of s[:j-1] * N^len(s[j:i]))`

since only 26 English character, N = 26

```py
class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)

        prefixRollingHash = [0] # 1-indexed
        N = 26
        for i in range(n):
            ch = ord(s[i])-ord("a")
            prefixRollingHash.append(prefixRollingHash[-1] * N + ch)

        def getRollingHash(i, length):
            return prefixRollingHash[i+length] - prefixRollingHash[i] * pow(N, length)

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
```

but this will get MLE/TLE, therefore, we should use modulo and avoid hash collision.

we use `mod = 1e9+7`

=> `(prefixRollingHash[i+length] - prefixRollingHash[i] * pow(N, length, mod) + mod)%mod`

and we can precompute pow(N, length, mod):
`powmod = [pow(N, i, mod) for i in range(n+1)]`
and replace `pow(N, length, mod)` with `powmod[length]`

time: O(nlogn)