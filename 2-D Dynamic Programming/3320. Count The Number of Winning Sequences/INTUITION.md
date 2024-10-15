# Intuition

這題要求方法數, 很明顯是個dynamic programming的題目
而且相對應的決策也很明顯

1. 首先得紀錄`i`來判斷我們對應完Alice的決策了沒
2. 再來因為不能連續兩個相同決策, 所以得紀錄上個決策(`F/W/E`)
3. 然後我們要分數要`strictly greater`, 所以在紀錄分數的`diff`

因此定義: dfs(i, prev, diff): the ways to play with alice with `diff` points at i-th round and summon `prev`

那再來就把所有勝利的決策加總起來即可:

```py
mod = 10**9 + 7
def dfs(i, prev, diff):
    if i == len(s): return int(diff > 0)

    if memo[i][ch2idx[prev]][diff] != -1: return memo[i][ch2idx[prev]][diff]

    res = 0
    if s[i] == "F":
        if prev != "F":
            res += dfs(i+1, "F", diff)
        if prev != "E":
            res += dfs(i+1, "E", diff - 1)
        if prev != "W":
            res += dfs(i+1, "W", diff + 1)
    elif s[i] == "W":
        if prev != "F":
            res += dfs(i+1, "F", diff - 1)
        if prev != "E":
            res += dfs(i+1, "E", diff + 1)
        if prev != "W":
            res += dfs(i+1, "W", diff)
    else: # s[i] == "E"
        if prev != "F":
            res += dfs(i+1, "F", diff + 1)
        if prev != "E":
            res += dfs(i+1, "E", diff)
        if prev != "W":
            res += dfs(i+1, "W", diff - 1)
    res %= mod
    memo[i][ch2idx[prev]][diff] = res
    return res
```

time: O(n * 4 * n) 
space: O(n * 4 * n)

> 另外注意, 如果我們python直接對`dfs`使用decorator `@cache` 會TLE, 所以我們額外用個二維list + defaultdict來加速運算時間