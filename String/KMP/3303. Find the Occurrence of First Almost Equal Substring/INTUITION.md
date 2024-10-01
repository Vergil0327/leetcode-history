# Intuition

對於這種string match, 首先想到的就是rolling-hash (Rabin-Karp)

```py
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        base = 26
        mod = 10**11 + 7

        def get_rolling_hash(pattern):
            n = len(pattern)
            nums = [ord(ch)-ord("a") for ch in pattern]

            rolling_hash = 0
            for i in range(n):
                rolling_hash = rolling_hash*base + nums[i]
                rolling_hash = (rolling_hash+mod) % mod
            return rolling_hash
        
        m, n = len(s), len(pattern)
        almost_equal = set()
        for i in range(n):
            for ch in string.ascii_lowercase:
                almost_equal.add(get_rolling_hash(pattern[:i] + ch + pattern[i+1:]))

        rolling_hash = 0
        pow_base_len = pow(base, n, mod)
        for i in range(m):
            num = ord(s[i])-ord("a")
            rolling_hash = rolling_hash*base + num
            if i >= n:
                rolling_hash -= pow_base_len * (ord(s[i-n]) - ord("a"))

            rolling_hash = (rolling_hash+mod) % mod
            if i >= n-1 and rolling_hash in almost_equal:
                return i-n+1

        return -1
```

可惜這題時間上並不允許, 會TLE (654 / 778 testcases passed)

而這題真正要你用的其實是**Z-Function**

由於我們要在s裡找出與pattern **almost-equal**的substring, 所以

我們透過z-function在s裡找出:
- 最長與pattern prefix相符的prefix, 假設長度是p
- 最長與pattern suffix相符的suffix, 假設長度是q

那麼一但找到一個位置`i`使得, `p + 1 + q >= pattern.length`的話, 就代表我們找到**almost equal**
這時返回i即可

### Z-Function

z[i]  is the length of the longest string that is, at the same time, a prefix of  s and a prefix of the suffix of  s  starting at i .

If we compute z-function for p + s, then z[len(p) + i] would be the number of characters from s[i] that match the prefix of p .

We also need to compute z-function for reverse(p) + reverse(s). It would tell us the number of characters matching the suffix of p.