class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]

        for h, w, p in prices:
            dp[h][w] = p

        for i in range(1, m+1):
            for j in range(1, n+1):
                for cut in range(1, i):
                    dp[i][j] = max(dp[i][j], dp[i-cut][j] + dp[cut][j])

                for cut in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i][j-cut] + dp[i][cut])

        return dp[m][n]

# top-down dp (dfs + memorization)
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        sell = defaultdict(int)
        for h, w, p in prices:
            sell[h, w] = p

        @cache
        def dfs(height, width):
            if height < 0 or width < 0: return -inf

            # no cut
            price = sell[height, width] if (height, width) in sell else 0
            
            # vertically cut
            for w in range(1, width):
                price = max(price, dfs(height, w) + dfs(height, width-w))
            
            # horizontally cut
            for h in range(1, height):
                price = max(price, dfs(h, width) + dfs(height-h, width))
            return price
        return dfs(m, n)