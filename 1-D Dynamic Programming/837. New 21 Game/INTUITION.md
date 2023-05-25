# Intuition

### Brute Force

直覺上可以用top-down方式遞歸來模擬情境
把所有最後分數<= n的機率加總起來

但這樣會超時, 代表有很多多餘的計算

```py
class Solution_TLE:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @lru_cache(None)
        def dfs(curr):
            res = 0
            if curr < k:
                for pt in range(1, maxPts+1):
                    res += dfs(curr+pt) * 1/maxPts
            else:
                return 1 if curr <= n else 0
            return res
        return dfs(0)
```

延續top-down的想法, 我們的dp定義為

define `dp[pt]`: the probability from 0 to pt

```
dp[pt] = sum{dp[max(0, pt-maxPts)]*1/maxPts, ..., dp[pt-3]*1/maxPts, dp[pt-2]*1/maxPts, dp[pt-1]*1/maxPts}
       = sum{dp[max(0, pt-maxPts)], ..., dp[pt-3], dp[pt-2], dp[pt-1]} * 1/maxPts
       = sum{last maxPts results} / maxPts
```

**our target is to find dp[n]**

所以比起每次遍歷, 我們其實只要維護一個長度為`maxPts`的dp prefix sum (sliding window)

所以狀態轉移框架可以這麼寫

對於抵達`i`points來說, 他是從前maxPts個狀態 * 1/maxPts而來, 所以

- dp[i] = presumDP/maxPts

**base case**

i = 1時, 會需要`presumDP = 1`
這也代表`dp[0] = 1`

然後再更新presumDP
- 如果`i`points仍小於`k`, 那對於下一輪來說, 仍是合法的狀態
  - if i < k: presumDP + dp[i]
  - if i >= k: 那這時已經不能再抽卡了, res += dp[i]. 這跟top-down一模一樣
- 如果`i-maxPts >= 0`, 那對於下一個狀態來說 dp[i-maxPts]已經不合法所以必須扣除
  - if i-maxPts >= 0, presumDP -= dp[i-maxPts]