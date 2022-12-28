# Bottom-Up
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(profit)

        # dp[i][members][proft]: from first i crimes, how many of schemes s.t. we just use members and earn profits
        dp = [[[0] * (n+1) for _ in range(minProfit+1)] for _ in range(m+1)]
        dp[0][0][0] = 1
        
        for i in range(m):
            for p in range(minProfit+1):
                for g in range(n+1):
                    dp[i+1][p][g] += dp[i][p][g]
                    if g+group[i] <= n:
                        dp[i+1][min(p+profit[i], minProfit)][g+group[i]] += dp[i][p][g]
                    dp[i+1][p][g] %= MOD
        
        total = sum(dp[m][minProfit])
        total %= MOD
        return total

    # def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    #     MOD = 10**9 + 7
    #     m = len(profit)

    #     @lru_cache(None)
    #     def dfs(i, members, money):
    #         if i == m: return 0
    #         if members > n: return 0

    #         schemes = 0
    #         schemes += dfs(i+1, members, money)
    #         schemes += dfs(i+1, members+group[i], money + profit[i]) + (1 if members+group[i] <= n and money+profit[i] >= minProfit else 0)

    #         return schemes % MOD

    #     initialMoney = 0
    #     intitalMembers = 0
    #     return dfs(0, intitalMembers, initialMoney) + (1 if initialMoney >= minProfit and intitalMembers <= n else 0)

# Top-Down
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(i, members, money):
            if i == len(profit): return 0
            if members > n: return 0

            schemes = 0
            schemes += dfs(i+1, members+group[i], money + profit[i]) + (1 if members+group[i] <= n and money+profit[i] >= minProfit else 0)
            schemes += dfs(i+1, members, money)

            return schemes % MOD

        initialMoney = 0
        intitalMembers = 0
        return dfs(0, intitalMembers, initialMoney) + (1 if initialMoney >= minProfit and intitalMembers <= n else 0)