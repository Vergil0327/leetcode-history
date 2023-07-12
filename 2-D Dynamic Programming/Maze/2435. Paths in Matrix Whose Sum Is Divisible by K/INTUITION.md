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

# Other Solution - bottom-up

定義dp[i][j][m]: the ways to reach (i, j) when sum%k = m

對於走到當前grid[i][j]來說, 他的可能餘數為`0 <= m < k`:
所以我們遍歷所有可能的餘數`m`, 兩個方向的所有可能數相加:
```py
for m in range(k):
    dp[i][j][(m + grid[i][j])%k] = dp[i-1][j][m] + dp[i][j-1][m]
```

**base case**

起始狀態為一種方法數
dp[0][0][grid[0][0]%k] = 1