# Intuition

一開始只想得到Brute Force:
```py
def maximumGain(self, s: str, x: int, y: int) -> int:
    @lru_cache(None)
    def dfs(s):
        m = len(s)
        points = 0
        for i in range(1, m):
            # ba
            if s[i] == "a" and s[i-1] == "b":
                points = max(points, dfs(s[:i-1] + s[i+1:]) + y)
            # ab
            if s[i] == "b" and s[i-1] == "a":
                points = max(points, dfs(s[:i-1] + s[i+1:]) + x)
        return points

    n = len(s)
    i = res = 0
    while i < n:
        if s[i] != "a" and s[i] != "b":
            i += 1
            continue

        j = i
        while j < n and (s[j] == "a" or s[j] == "b"):
            j += 1

        res += dfs(s[i:j])

        i = j
    return res
```

但這會是個$O(n^2)$的時間複雜度, 肯定會是TLE的
因此可能要想看看有沒有Greedy或是Binary Search Solution

對於"ab"我們可以先取或是後取, 同樣地對於"ba"我們也可以先取或後取
由於看不出明顯的binary search的搜索方法，因此這題很可能是要用Greedy的方式來解

首先我們不關心"a", "b"以外的字母, 以所有非"a", "b"的字母做為分隔
我們都能得到一串只由"a", "b"組成的substring

```
abab -> ba + ab or ab + ab = y+x or x+x
baba -> ab + ba or ba + ba = x+y or y+y
aabb -> ab + ab = x + x
bbaa -> ba + ba = y + y
abaa -> ab or ba = x or y
babb -> ba or ab = y or x
abba -> x + y
baab -> y + x
```

再來從上面觀察可發現, 我們沒有任何substring會導致有兩種可能是 `y+x` or `x+y`
所以我們永遠都只有兩種決策:
1. 先取"ab"再取"ba"
2. 先取"ba"再取"ab"

因此我們就可以用**stack**來優先取"ab"然後再對剩下取"ba"
以及先取"ba"在取"ab"
然後兩者取較大值即可
