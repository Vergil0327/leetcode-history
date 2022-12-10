# Observation
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

# Top-Down + Memorization
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        
        @functools.lru_cache(None)
        def dfs(piles):
            if not piles: return 0

            bob1 = dfs(tuple(piles[1:]))
            takeFirstAlice = piles[0] + sum(piles[1:])- bob1
            
            bob2 = dfs(tuple(piles[:-1]))
            takeLastAlice = piles[-1] + sum(piles[:-1])-bob2
            return max(takeFirstAlice, takeLastAlice)
            
        return dfs(tuple(piles)) > total//2

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        # dp[i][j]: alice's greatest piles from piles[i] to piles[j]
        dp = [[0] * n for _ in range(n)]

        # base case: for every i=j, dp[i][j] = piles[i]
        for i in range(n):
            dp[i][i] = piles[i]

        # [1,2]
        # n = 2, i=0, length=1
        # chooseFirst = piles[0] - dp[0+1][0+1] dp[1][1]
        # chooseLast = piles[1] - dp[0][0+1-1] dp[0][0]
        # dp[0][1] = max(chooseFirst, chooseLast)
        for length in range(1, n):
            for i in range(0, n-length):
                chooseFirst = piles[i] - dp[i+1][i+length]
                chooseLast = piles[i+length] - dp[i][i+length-1]
                dp[i][i+length] = max(chooseFirst, chooseLast)
        return dp[0][n-1] > 0