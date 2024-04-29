# Intuition

目的是進一步優化時間複雜度

從top-down solution來看, 能很明顯地看出內部的for-loop可以再進一步優化

```py
def top_down_solution(zero, one, last):
    if zero == 0 and one == 0: return 1

    res = 0
    if last == 0:
        for consecutiveOne in range(1, limit+1):
            if consecutiveOne <= one:
                res += dfs(zero, one-consecutiveOne, 1)
    else:
        for consecutiveZero in range(1, limit+1):
            if consecutiveZero <= zero:
                res += dfs(zero-consecutiveZero, one, 0)
    return res%mod
return top_down_solution(zero, one, 0) + top_down_solution(zero, one, 1)
```

對於`dfs(zero, one-consecutiveOne, 1) for consecutiveOne in range(1, limit+1)`這部分來說
他其實就是一段dp state的sum, 在求這些state的同時, 其實前驅狀態都是已知的
所以再優化方面得往prefix sum去想

top-down solution不好繼續優化, 可能得先轉成bottom-up的方式然後再繼續:

dp[zero][one][last]: number of StableArray considering zero's 0 and one's 1 and last element is last where last is either 0 or 1.

```py
def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    mod = 10**9 + 7
    dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
    dp[0][0][0] = dp[0][0][1] = 1
    for x in range(zero+1):
        for y in range(one+1):
            for consecutive in range(1, limit+1):
                if consecutive <= y:
                    dp[x][y][last] += dp[x][y-consecutive][1-last]
                else:
                    break

            for consecutive in range(1, limit+1):
                if consecutive <= x:
                    dp[x][y][last] += dp[x-consecutive][y][1-last]
                else:
                    break
            dp[x][y][last] %= mod

    return dp[zero][one][0] + dp[zero][one][1]
```

可進一步寫成:

```py
dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
dp[0][0][0] = dp[0][0][1] = 1

for i in range(1, one+1):
    if i <= limit:
        dp[0][i][0] = 1
        
for i in range(1, zero+1):
    if i <= limit:
        dp[i][0][1] = 1

for x in range(1, zero+1):
    for y in range(1, one+1):
        for consecutive in range(1, min(y, limit)+1):
            dp[x][y][0] += dp[x][y-consecutive][1]
            dp[x][y][0] %= mod

        for consecutive in range(1, min(x, limit)+1):
            dp[x][y][1] += dp[x-consecutive][y][0]
            dp[x][y][1] %= mod

return dp[zero][one][0] + dp[zero][one][1]
```

從bottom-up也能明顯看出`for consecutive in range(1, limit+1)`這段for-loop所用到的state都是已知state

```py
dp[x][y][0] = dp[x][0][1] + dp[x][1][1] + ... + dp[x][min(y, limit)][1] = presum_dp[x][y-1][1] - presum_dp[x][y-limit-1][1]
dp[x][y][1] = dp[0][y][0] + dp[1][y][0] + ... + dp[min(x, limit)][y][0] = presum_dp[x-1][y][0] - presum[x-limit-1][y][0]
```

所以如果我們另外用個presum_dp同時把這些記錄下來並持續更新
我們就不用每次都for-loop更新一整個state

所以接下來就是有耐心的定義跟更新presum_dp

首先是初始化presum_dp base case:

```py
presum_dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
for i in range(one+1):
    presum_dp[0][i][0] = dp[0][i][0]
for i in range(zero+1):
    presum_dp[i][0][1] = dp[i][0][1]
```

再來就是將for-loop換成prefix sum的形式, 並在最後利用dp[zero][one][0/1]更新presum_dp

```py
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        dp[0][0][0] = dp[0][0][1] = 1
        for i in range(1, one+1):
            if i <= limit:
                dp[0][i][0] = 1
                
        for i in range(1, zero+1):
            if i <= limit:
                dp[i][0][1] = 1

        presum_dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        for i in range(one+1):
            presum_dp[0][i][0] = dp[0][i][0]
        for i in range(zero+1):
            presum_dp[i][0][1] = dp[i][0][1]

        for x in range(1, zero+1):
            for y in range(1, one+1):
                # for consecutive in range(1, min(y, limit)+1):
                #     dp[x][y][0] += dp[x][y-consecutive][1]
                #     dp[x][y][0] %= mod
                dp[x][y][0] = presum_dp[x][y-1][1] - (presum_dp[x][y-limit-1][1] if y-limit-1 >= 0 else 0)
                dp[x][y][0] = (dp[x][y][0] + mod) % mod

                # for consecutive in range(1, min(x, limit)+1):
                #     dp[x][y][1] += dp[x-consecutive][y][0]
                #     dp[x][y][1] %= mod
                dp[x][y][1] = presum_dp[x-1][y][0] - (presum_dp[x-limit-1][y][0] if x-limit-1 >= 0 else 0)
                dp[x][y][1] = (dp[x][y][1] + mod) % mod

                presum_dp[x][y][0] = (presum_dp[x-1][y][0] + dp[x][y][0]) % mod
                presum_dp[x][y][1] = (presum_dp[x][y-1][1] + dp[x][y][1]) % mod

        return (dp[zero][one][0] + dp[zero][one][1]) % mod
```
