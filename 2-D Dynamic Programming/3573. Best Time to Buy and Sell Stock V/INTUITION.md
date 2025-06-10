# Intuition

一開始直覺先寫出simulation:

```py
class Solution:
    def maximumProfit(self, prices: List[int], K: int) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, k):
            if i >= n:
                return 0 if k >= 0 else -inf

            res = dfs(i+1, k)

            for j in range(i+1, n):
                res = max(res, dfs(j+1, k-1) - prices[i] + prices[j])
                res = max(res, dfs(j+1, k-1) + prices[i] - prices[j])
            return res
        return dfs(0, K)
```

後來想到, 如果要更進一步優化, 那試著take-or-skip方式來挑選我們要的prices[i]
但這樣就需要紀錄當前處於哪種狀態 `tx_type`:

```py
class Solution:
    def maximumProfit(self, prices: List[int], K: int) -> int:
        n = len(prices)

        # tx_type=0 no tx
        # tx_type=1 sell
        # tx_type=2 short sell
        @lru_cache(None)
        def dfs(i, k, tx_type):
            if i >= n:
                return 0 if k >= 0 and tx_type == 0 else -inf

            res = dfs(i+1, k, tx_type)
            if k > 0:
                if tx_type == 0:
                    res = max(res, dfs(i+1, k, 1) - prices[i])
                    res = max(res, dfs(i+1, k, 2) + prices[i])
                else:
                    if tx_type == 1:
                        res = max(res, dfs(i+1, k-1, 0) + prices[i])
                    if tx_type == 2:
                        res = max(res, dfs(i+1, k-1, 0) - prices[i])
            return res
        dfs.cache_clear()
        return dfs(0, K, 0)    
```

但由於直接用`@lru_cache`會Memory Limit Exceed(MLE)
所以直覺想到用三維矩陣進一步節省空間

```py
class Solution:
    def maximumProfit(self, prices: List[int], K: int) -> int:
        n = len(prices)

        # tx_type=0 no tx
        # tx_type=1 sell
        # tx_type=2 short sell
        memo = [[[None]*3 for _ in range(K+1)] for _ in range(n)]

        def dfs(i, k, tx_type):
            if i >= n:
                return 0 if k >= 0 and tx_type == 0 else -inf

            if memo[i][k][tx_type] is None:
                memo[i][k][tx_type] = dfs(i+1, k, tx_type)
                if k > 0:
                    if tx_type == 0:
                        memo[i][k][tx_type] = max(memo[i][k][tx_type], dfs(i+1, k, 1) - prices[i])
                        memo[i][k][tx_type] = max(memo[i][k][tx_type], dfs(i+1, k, 2) + prices[i])
                    else:
                        if tx_type == 1:
                            memo[i][k][tx_type] = max(memo[i][k][tx_type], dfs(i+1, k-1, 0) + prices[i])
                        if tx_type == 2:
                            memo[i][k][tx_type] = max(memo[i][k][tx_type], dfs(i+1, k-1, 0) - prices[i])
            return memo[i][k][tx_type]

        return dfs(0, K, 0)
```
