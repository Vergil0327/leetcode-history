# Intuition

競賽途中觀察example 2:

```
010101
```

我們很明顯有兩個操作, 當時首先想到的是如果是只能翻轉prefix, 那麼是不是就可以用dp解?

我們定義dp1[i][0,1]為`the minimum operations required for s[:i] to flipped all into 0 or 1.`

那麼狀態轉移我們就看第i個字符是什麼

**我們全部用1-indexed**

- 如果s[i] == "0"
  - 那麼dp[i][0]就只需要看前面s[:i-1]全部翻轉為0的次數, 也就是dp[i-1][0]
    - dp[i][0] = dp[i-1][0]
    
  - 那麼dp[i][1]就看前面s[:i-1]都為0的cost再加上s[:i]全翻轉為1的cost
    - dp[i][1] = dp[i-1][0] + i
  

- 如果s[i] == "1
  - dp[i][0]就看前面s[:i-1]都要為1的翻轉cost再加上這次全部翻轉為0的cost
    - dp[i][0] = dp[i-1][1] + i
  - dp[i][1]就看前面s[:i-1]都為1的cost
    - dp[i][1] = dp[i-1][1]

同理, 我們還有另一個操作是翻轉suffix, 所以一樣我們就從後往前來看:

這時dp2[i][0,1]為:
`the minimum operations required for s[i:] to flipped all into 0 or 1.`

- if s[i] = "0":
  - dp2[i][0]就看s[i+1:]全翻轉為0的cost
    - dp2[i][0] = dp2[i+1][0]
  - dp2[i][1]就看s[i+1:]全翻轉為0的cost, 然後再一次全翻轉為1的cost
    - dp2[i][1] = dp2[i+1][0] + n-i+1
- if s[i] = "1":
    - dp2[i][1] = dp2[i+1][1]
    - dp2[i][0] = dp2[i+1][1] + n-i+1

那兩種操作的最佳操作都有之後, 我們就每個index遍歷一遍, 找出小操作數即可

可能是全翻轉為0或全翻轉為1, 我們取最佳
`最小操作數 = min(dp[i][0]+dp2[i][0], dp[i][1]+dp2[i][1])`


# Other Solution - One Pass Greedy

每當我們需要翻轉(s[i]!=s[i-1]), 我們可以翻prefix也可以翻suffix
我們取最佳的那個來解決`s[i]`使得他跟目前為止的s[:i-1]一致
那當下的`min(i, n-i)`就是s[i]的所需操作數

那解決s[i]之後, 這時整個s[:i]就全部翻轉成一樣的了
我們就在看s[i+1], 持續疊加到最後就會是我們所需的最小操作數了

```py
def minimumCost(self, s: str) -> int:
    res = 0
    n = len(s)
    for i in range(1, n):
        if s[i] != s[i-1]:
            res += min(i, n-i)
    return res
```
