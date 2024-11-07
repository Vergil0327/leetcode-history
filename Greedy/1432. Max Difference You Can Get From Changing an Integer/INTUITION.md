# Intuition

這題比較考驗思維能力

- 找出max比較簡單, 高位往低位遍歷, 找到第一個不是"9"的digit, 全替換成"9"即可
- 找出min的話要分幾個情況, 但大方向就是高位往低位, 找到第一個將digit換成`"0"`或`"1"`的合法情況
  1. 如果`s[0]` > "1", 那就把所有`s[0]` digit換成`"1"`
  2. 如果`s[0]`已經是"1", 那就從第二位數開始, 找到第一個不為`"0"`的digit替換成`"0"`, **並且**該digit不可以跟`s[0]`一樣, 不然會產生leading zero

## More Simple Solution

直接暴力生產出最佳解:

```py
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        mx, mn = -inf, inf
        for d1 in "0123456789":
            for d2 in "019":
                nxt = s.replace(d1, d2)
                if nxt[0] == "0" or int(nxt) == 0: continue

                mx = max(mx, int(nxt))
                mn = min(mn, int(nxt))
        return mx - mn
```

# Complexity

time: O(n)
space: O(n)