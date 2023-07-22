# Intuition

起初想到的brute force為:
```py
def numberOfWays(self, N: int, x: int) -> int:
    M = 10**9 + 7
        
    @lru_cache(None)
    def dfs(n, start):
        if n == 0: return 1
        if n < 0: return 0
        if start**x > n: return 0
        
        res = 0
        for i in range(start, N+1):
            res += dfs(n - i**x, i+1)
            res %= M
        return res
    
    res = 0
    for i in range(1, N+1):
        res += dfs(N - i**x, i+1)
        res %= M
    return res
```

就遍歷全部可能然後看能不能讓總和拼成`n`, 但這樣會TLE

後來發現, 其實是從num from 1 to num**x <= n這段區間挑任意subset使得subset裡的$num^x$總和為n
所以我們其實可以用take-or-skip的策略, 然後方法數會是加法原理

首先num從1開始, 對於每個num我們可以選擇取或不取:
1. 取num的話, current_sum += num ** x
2. 不取的話, current_sum 不變

所以top-down recursion可以很直覺寫成下面這種形式

至於**base case**則為:
- 如果_sum == n, 代表我們找到一個合法的subset所以方法數返回1
- 如果num ** x > n 或是 _sum > n, 那麼都是不合法的解, 返回0

```py
def numberOfWays(self, n: int, x: int) -> int:
    M = 10**9 + 7
        
    @lru_cache(None)
    def dfs(_sum, num):
        if _sum == n: return 1
        if num ** x > n: return 0
        if _sum > n: return 0
        
        res = 0
        res = (res + dfs(_sum + num**x, num+1))%M
        res = (res + dfs(_sum, num+1))%M
        return res
        
    return dfs(0, 1)
```

但這樣的話會因為MLE而死在最後的test case

所以後來改成不使用lru_cache, 而是直接開二維array數組後就通過了

# Other Solution

bottom-up的方式的話, 定義`dp[sum]: the number of ways to make sum`
一樣num從1開始直到 `num ** x <= n`

那這樣dp[sum]就可以從dp[sum - num ** x]的方法數轉移過來, 所以是:

```py
dp[sum] += dp[sum - num**x]
dp[sum] %= mod
```

從後往前遍歷的話, 可以只用一維數組來省記憶體空間
因為dp[sum]確定後就不會再被後續狀態更新而影響到

```py
def numberOfWays(self, n: int, x: int) -> int:
    dp = [0] * (n+1)
    dp[0] = 1
    
    num = 1
    mod = 10**9 + 7
    while (v := pow(num, x)) <= n:
        for _sum in range(n, v - 1, -1):
            dp[_sum] = (dp[_sum] + dp[_sum - v]) % mod
        num += 1
    return dp[n]
```