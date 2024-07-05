# Intuition 1

首先比較能直覺想到的是top-down dp:
我們由上往下, 再由左往右放置房子
每次放完都更新當前街道的左側是不是有房子, 後續放置會依據這個決定和不合法
最終總方法數即為答案

```py
def countHousePlacements(self, n: int) -> int:
    mod = 10**9 + 7

    dp = [[[[-1, -1] for _ in range(2)] for _ in range(n)] for _ in range(2)]
    
    def dfs(r, c, leftTop, leftBot):
        if r == 2: return dfs(0, c+1, leftTop, leftBot)
        if c == n: return 1

        if dp[r][c][leftTop][leftBot] == -1:
            dp[r][c][leftTop][leftBot] = dfs(r+1, c, 0 if r == 0 else leftTop, 0 if r == 1 else leftBot)
            if r == 0 and not leftTop:
                dp[r][c][leftTop][leftBot] += dfs(r+1, c, 1, leftBot)
            if r == 1 and not leftBot:
                dp[r][c][leftTop][leftBot] += dfs(r+1, c, leftTop, 1)
            dp[r][c][leftTop][leftBot] %= mod
        return dp[r][c][leftTop][leftBot]

    return dfs(0, 0, 0, 0)
```

# Intuition 2 (Optimized)

但由於兩邊街道不相互干擾, 其實就像是兩排house roubber
當前dp[i]的方法數從dp[i-1]跟dp[i-2]轉移過來, dp[i] = dp[i-1] + dp[i-2]
最終總方法數就是兩邊各自方方數相乘的排列組合: dp[n-1]*dp[n-1]

base case: 由於dp跟i-2有關, 所以我們將整個遍歷範圍往右兩格[2, n+2)
設置base case => dp[0] = dp[1] = 1

那這樣單獨一排街道的方法數為dp[-1], 總方法數就是(dp[-1]*dp[-1])