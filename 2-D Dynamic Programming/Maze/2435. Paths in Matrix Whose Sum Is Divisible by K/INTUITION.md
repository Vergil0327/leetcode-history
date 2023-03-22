# Intuition

由於要相加到最後才知道對k取餘數會不會為零
所以我們dp要記錄走到每個位置的path sum

由於看的是最後餘數，所以沿途我們可以都對k取餘數，這樣數值範圍僅會落在[0:k]
並且k的範圍僅僅`1 <= k <= 50`
所以我們直接dfs + memorization並持續對path_sum取餘數, 然後看最後有多少合法抵達(m-1, n-1)的path數目即可

大致框架為:

- 如果抵達(m-1, n-1)時, (path_sum + grid[m-1][n-1])%k = 0, 代表這是1個合法的path

```py
@lru_cache(None)
def dfs(i, j, path_sum):
    if i >= m or j >= n: return 0
    if i == m-1 and j == n-1:
        return 1 if (path_sum+grid[i][j])%k == 0 else 0

    res = dfs(i+1, j, (path_sum + grid[i][j])%k)
    res %= 1_000_000_007
    res += dfs(i, j+1, (path_sum + grid[i][j])%k)
    res %= 1_000_000_007
    return res
return dfs(0, 0, 0)
```

由於用hashmap做cache會TLE
我們可以直接開個3維array，效率會高一點