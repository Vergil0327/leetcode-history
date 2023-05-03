# Intuition

## top-down dp

我們找出從`start`出發, 在總共有`fuel`這麼多的燃料下能抵達`finish`多少次
很直覺的想到能用DFS來探索所有路徑次數

我們標記當前的位置以及剩餘燃料, 每次遞歸都找出下一個能抵達的位置
只要當前位置是finish, 那就代表方法數+1
把所有方法數加總即為答案

## bottom-up

核心代碼如下, 重點是我們的狀態轉移依賴於高油量的時候
因此必須`fuel`從大到小建立dp table
再來就遍歷當前城市及下個城市進行狀態轉移即可

```py
dp = [[0]*(fuel+1) for _ in range(n)]
dp[start][fuel] = 1

for f in range(fuel, -1, -1):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            
            cost = abs(locations[i] - locations[j])
            if f+cost <= fuel:
                dp[i][f] += dp[j][f+cost]
                dp[i][f] %= mod
```

# Complexity

- time complexity
$$O(n^2 * f)$$

- space complexity
$$O(nf)$$

# Other Solution


這解法必須前提是locations是依序排列的
對於每個城市, 我們算出他被經過多少次以及停留多少次
這樣我們對於`city`來說, 他的狀態僅來自於左右相鄰城市`city-1`和`city+1`
然後再多一個有限狀態`state`來區分往左經過, 往右經過以及停留

```py
n = len(locations)
startPos = locations[start]
finishPos = locations[finish]
locations.sort()

startIdx = endIdx = -1
for i in range(n):
    if locations[i] == startPos:
        startIdx = i
    if locations[i] == finishPos:
        endIdx = i
```

```py
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7

        dp = [[[0]*3 for _ in range(n)]for _ in range(fuel+1)]
        dp[fuel][startIdx][0] = 1

        for f in range(fuel, -1, -1):
            for city in range(n):
                # dp[f][city][state], state=0 -> stay at city; state=1 -> moving right; state=2 -> moving left
                if city > 0 and f+(cost := abs(locations[city] - locations[city-1])) <= fuel:
                    # 以及停留在city = 向左經過city-1 及 停留在city-1 的方法數都能抵達city
                    dp[f][city][0] += dp[f+cost][city-1][1] + dp[f+cost][city-1][0]
                    dp[f][city][0] %= mod
                    dp[f][city][1] += dp[f+cost][city-1][1] + dp[f+cost][city-1][0]
                    dp[f][city][1] %= mod
                if city < n-1 and f+(cost := abs(locations[city] - locations[city+1])) <= fuel:
                    dp[f][city][0] += dp[f+cost][city+1][2] + dp[f+cost][city+1][0]
                    dp[f][city][0] %= mod
                    dp[f][city][2] += dp[f+cost][city+1][2] + dp[f+cost][city+1][0]
                    dp[f][city][2] %= mod
        
        res = 0
        for f in range(fuel+1):
            res = (res + dp[f][endIdx][0])%mod
        
        return res
```