# Top-down
# iterate through all the coins and use start index to remove duplicate
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        
        @functools.lru_cache(None)
        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            
            total = 0
            for j in range(i, len(coins)):
                coin = coins[j]

                # since we've sorted coins, we can get rid of coins if thay're impossible to make the amount
                if coin > amount: break
                total += dfs(j, amount-coin)
            return total
        return dfs(0, amount)

# take or skip strategy
# we've also sort coins to remove recursion branch
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        
        @functools.lru_cache(None)
        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins) or coins[i] > amount:
                return 0
            
            # take or skip
            total = 0
            total += dfs(i, amount-coins[i]) + dfs(i+1, amount)
            
            return total
        return dfs(0, amount)


# bottom-up
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j]: the number of combinations that make up j amount by using first i coins

        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1 # one combination to make amount 0
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                dp[i][j] += dp[i-1][j] + (dp[i][j-coins[i-1]] if j-coins[i-1] >= 0 else 0)
        return dp[len(coins)][amount]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[amount][i]: the number of combination by using first i coins to make amount
        n = len(coins)
        dp = [[0] * (n+1) for _ in range(amount+1)]

        for j in range(n+1):
            dp[0][j] = 1

        for i in range(1, amount+1):
            for j in range(1, n+1):
                if i-coins[j-1] < 0:
                    dp[i][j] = dp[i][j-1]
                    continue
                dp[i][j] = dp[i][j-1] + dp[i-coins[j-1]][j]
        
        return dp[amount][n]
