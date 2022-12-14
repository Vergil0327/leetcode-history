# Top-Down DP, Recurison + Memorization
class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1]+stones[i-1]
        
        @functools.lru_cache(None)
        def take(i):
            if i >= n: return 0
            score1 = presum[min(i+1,n)]-presum[i]+presum[-1]-presum[i+1]-take(i+1)
            score2 = presum[min(i+2,n)]-presum[i]+presum[-1]-presum[min(i+2,n)]-take(i+2)
            score3 = presum[min(i+3,n)]-presum[i]+presum[-1]-presum[min(i+3,n)]-take(i+3)
            return max(score1, score2, score3)
        
        alice = take(0)
        if alice > presum[-1]-alice:
            return "Alice"
        elif alice < presum[-1]-alice:
            return "Bob"
        else:
            return "Tie"

# Bottom-Up
class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)        
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1]+stones[i-1]

        # dp[i]: maximum score player can get where i piles stones has been taken
        dp = [-inf] * (n+1)
        dp[n] = 0

        for i in range(n-1, -1, -1): # taken n piles to 0
            for k in range(1, 4): # take one, two or three piles of stones
                if i+k > n: break
                score = presum[i+k]-presum[i] + presum[n]-presum[i+k] - dp[i+k]
                dp[i] = max(dp[i], score)

        alice = dp[0]
        if alice > presum[n]-alice:
            return "Alice"
        elif alice < presum[n]-alice:
            return "Bob"
        else:
            return "Tie"
