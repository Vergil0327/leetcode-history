class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffixSum = [0] * (n+1+100) # avoid suffixSum[i+x] out-of-bound
        for i in range(n-1, -1, -1):
            suffixSum[i] = suffixSum[i+1]+piles[i]

        @functools.lru_cache(None)
        def dfs(i, M):
            if i >= n: return 0
            
            total = 0
            score = 0
            for x in range(1, 2*M+1):
                if i+x-1 >= n: break
                total += piles[i+x-1]
                bob = dfs(i+x, max(M, x))
                alice = total + suffixSum[i+x] - bob
                score = max(score, alice)
            
            return score
            
        return dfs(0, 1)

# max(Alice points) = points - min(Bob points)
class ConciseSolution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def play(i, m):
            points = sum(piles[i:])
            if i + 2 * m >= len(piles):
                return points
            return points - min(play(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return play(0, 1)

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @functools.lru_cache(None)
        def dfs(i, M):
            points = sum(piles[i:])
            if i + 2*M >= n:
                return points
            
            bob = float("inf")
            for m in range(1, 2*M+1):
                bob = min(bob, dfs(i+m, max(m,M)))
            
            return points - bob 
        return dfs(0, 1)

# bottom up
# https://leetcode.com/problems/stone-game-ii/discuss/738142/Python-bottom-up-with-in-code-explanation
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffixSum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffixSum[i] = suffixSum[i+1]+piles[i]
        
        dp = [[0]*(n+1) for i in range(n)] # dp[i][m]: maximum # of stones alice can get for piles[i:]

        for i in range(n-1,-1,-1):
            for m in range(n,0,-1):
                for x in range(1, 2*m+1):
                    points = suffixSum[i] - dp[i+x][max(x,m)] if i+x<n else suffixSum[i]
                    dp[i][m] = max(dp[i][m], points)
        
        return dp[0][1]