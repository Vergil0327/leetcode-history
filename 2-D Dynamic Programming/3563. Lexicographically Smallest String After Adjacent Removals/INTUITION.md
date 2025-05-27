# Intuition

主幹:

- 用top-down dp (DFS + memorization)去找出全局lexicographically smallest string

```py
@cache
def dfs(i):
    # Answer for S[i:]
    if i >= n: return ""

    ans = s[i] + dfs(i + 1)
    for j in range(i + 1, n, 2):
        if empty(i, j):
            ans = min(ans, dfs(j + 1))
    return ans

return dfs(0)
```

其中的`empty`又是另一個dp, 用來確認s[i:j] (both inclusive)是否可以被移除, 分三種情況:

1. base case: 當左端點大於右端點, 代表全部被移除
2. 如果s[l]跟s[r]可被移除, 那就近一步看s[l+1:r-1]這段
3. 找中間點`k`, 判斷s[l:k]跟s[k+1:r]能否分別被移除

```py
def empty(l, r):
    # Can S[l..r] be removed completely?
    if l > r:
        return True
    if abs(char[l] - char[r]) in [1, ord("z")-ord("a")] and empty(l + 1, r - 1):
        return True
    return any(empty(l, k) and empty(k + 1, r) for k in range(l + 1, r, 2))
```


time: 
- empty: O(n^2)
- dfs: O(n) * O(empty) = O(n^3)