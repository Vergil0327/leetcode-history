# Intuition

days = [1,4,6,7,8,20], costs = [2,7,15]
days = X X X X X X X X X [X]
                          i
days = X X X X X X X X [X X]
                        j i
days = X X X X X X X [X X X]
                      j   i
days = X X X X X X [X X X X]
                    j     i

觀察Example可發現, 每當我們考慮days[i]時
我們可以往前追溯看我們可以用哪一種ticket來往前cover最划算

定義 dp[i]: the minimum number of dollars you need to travel every day in the given list of days[:i].

我們可以透過`days[i]-days[j]+1`這出遊的天數橫跨幾天
由於題目沒有說costs是有序的，所以我們每個都試，然後找最划算的

只要 `days[i]-days[j]+1 <= 30` 小於等於30天，那就每種票價都試試，然後找最划算的
```py
for k in range(3):
    if days[i]-days[j]+1 <= [1, 7, 30][k]:
        dp[i] = min(dp[i], dp[j-1] + costs[k])
```

如果大於30天，那沒有任何票價可以cover, 可以直接break

`if days[i]-days[j]+1 > 30: break`

所以大致框架如下，最後返回的就是dp[n-1], 考慮全部的days list所得到的最小成本

```py
ticketType = [1, 7, 30] # [1-day pass, 7-day, 30-day]
for i in range(n):
    for j in range(i, -1, -1):
        if days[i] - days[j]+1 > ticketType[-1]: break
        for k in range(3):
            if days[i] - days[j]+1 <= ticketType[k]:
                dp[i] = min(dp[i], dp[j-1] + costs[k])
return dp[n-1]
```

**Base Case & Edge Case**

然後檢查每個dp的下標可發現, 當我們遍歷[0,n-1]這區間時`dp[j-1]`可能越界, j=0 0> j-1 = -1
所以我們全部換成**1-indexed**
那這樣我們遍歷的合法區間變為: `[1,n]`

```py
dp = [inf] * (n+1) # 1-indexed
days = [days[0]] + days # 1-indexed
for i in range(1, n+1): # [1,n]
    for j in range(i, 0, -1): # [n,1]
        # ...
return dp[n]
```

然後Baes Case: dp[0] = 0
0天出遊，那成本花費就是0