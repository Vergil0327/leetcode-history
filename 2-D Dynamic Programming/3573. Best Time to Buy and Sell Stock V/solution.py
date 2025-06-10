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
    
# iterative method
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        bought = [-inf] * k
        res = [0] * (k + 1)
        sold = [0] * k
        for p in prices:
            for kk in range(k, 0, -1):
                res[kk] = max(res[kk], bought[kk - 1] + p, sold[kk - 1] - p)
                bought[kk - 1] = max(bought[kk - 1], res[kk - 1] - p)
                sold[kk - 1] = max(sold[kk - 1], res[kk - 1] + p)
        return max(res)