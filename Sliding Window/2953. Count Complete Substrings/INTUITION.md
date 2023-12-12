# Intuition

A*k
A*k+B*k = (AB) * k
A*k+B*k+C*k = (ABC)*k
...
(A...Z)*k

sliding window 找出 k~26k的長度的complete string

所以首先我們遍歷[k,26k]長度, 再用sliding window查看當前有多少個exact k characters

再來看第二個條件:
如果k=3, word=AAAZZZ

```
AAAZZZ
l  r->
```
由於相鄰兩字母A跟Z的字符差距超過**2**, AAAZ這開頭的substring肯定不符合complete string
那麼其實我們可以直接把`l` pointer移動到`r`位置, 然後再重新搜索

所以我們需要記錄每個character的count
if count == k, valid += 1
等到valid == x * k where 1 <= x <= 26, 那就代表我們找到一個complete string

O(26n) 時間複雜度允許, 但leetcode會TLE
```python
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        def key(ch):
            return ord(ch)-ord("a")

        def validifyDiff(a, b):
            x, y = ord(a), ord(b)
            return abs(x-y) <= 2

        precnt = [[0]*26 for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(26):
                precnt[i][j] = precnt[i-1][j] + (1 if key(word[i-1]) == j else 0)

        res = 0
        for x in range(1, 27):
            length = x*k
            if length > n: break

            l = r = valid = 0
            while r < n:
                # cond. 2
                if r-1>=0 and not validifyDiff(word[r], word[r-1]):
                    valid = 0
                    l = r

                # cond. 1
                if precnt[r+1][key(word[r])]-precnt[l][key(word[r])] == k:
                    valid += 1
                r += 1

                while l < r and r-l > length:
                    if precnt[r][key(word[l])]-precnt[l][key(word[l])] == k:
                        valid -= 1
                    l += 1

                if r-l == length and valid == x:
                    res += 1
        return res
```

其實有個更快的解法是優先用條件2來找出可能區間
一旦滿足`abs(ord(w[r]) - ord(w[r-1])) > 2`, 代表[l:r), 跟[r:]這區間可能有complete string
所以我們就持續查看[l:r), 並且查看完移動`l=r`
最後在查看[r:]
```py
n = len(w)
l = res = 0
for r in range(1, n):
    if abs(ord(w[r]) - ord(w[r-1])) > 2:
        res += calc(w[l:r])
        l = r
res += calc(w[l:])
return res
```

而查看方式也是一樣, 遍歷[k, 26k]
維護每個字符的count, 並且關注他們每個字符個數是不是等於`k`個
而這樣的好處就不用每次都從頭進行一次sliding window