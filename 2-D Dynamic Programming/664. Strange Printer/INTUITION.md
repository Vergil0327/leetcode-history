# top-down

## Intuition

至少得打印第一個字符，再來就考慮可以一路打印到哪個字符
如果第`k`個字符跟首位字符相等, 亦即s[l:r]這區間裡s[l] == s[k]，我們都考慮看看是不是可以同步印完，然後在遞歸地考慮s[l+1:k-1]和s[k+1:r]
全部DFS搜索一遍後取最小值即可

核心程式碼為:

```
def dfs(l, r):
    res = dfs(l+1, r) + 1
    for k in range(l+1, r+1):
        if s[k] == s[l]:
            res = min(res, dfs(l, k-1) + dfs(k+1, r))
```

**邊界條件**
左端點必須小於右端點, 因此 `if l > r: return 0`

## Complexity

- time complexity

$$O(n^3)$$

(n-k)*(k-n) -> O(n^2) intervals -> O(n^2) subproblems
and we take O(n) for searching `k` in each subproblem

- space complexity

$$O(n^2)$$