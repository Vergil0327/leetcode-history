# bottom-up: O(amount * len(coins))
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float("inf")
        dp = [inf] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                val = dp[i-coin]+1 if i-coin >= 0 else inf
                dp[i] = min(dp[i], val)

        return -1 if dp[amount] == inf else dp[amount]

# top-down
class SolutionFaster:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float("inf")
        
        memo = [-inf] * (amount+1)
        def dfs(amount):
            if amount == 0: return 0
            if amount < 0: return -1
            
            if memo[amount] != -inf:
                return memo[amount]
            
            total = inf
            for coin in coins:
                times = dfs(amount-coin)
                if times != -1:
                    total = min(total, times+1)
                    
            memo[amount] = total if total != inf else -1
            return memo[amount]
            
        return dfs(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float("inf")
        
        @functools.lru_cache(None)
        def dfs(amount):
            if amount == 0: return 0
            if amount < 0: return -1
            
            total = inf
            for coin in coins:
                times = dfs(amount-coin)
                if times != -1:
                    total = min(total, times+1)

            return total if total != inf else -1
            
        return dfs(amount)