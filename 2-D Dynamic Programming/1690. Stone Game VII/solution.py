class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        presum = [0]*(n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + stones[i-1]

        # dp[i][j]: the maximum difference when playing in stones[i:j]
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        # base: length = 1
        # for i in range(n):
        #     j = i # j = i+length-1 = i+1-1
        #     dp[i][j] = 0

        # base: length = 2
        for i in range(n-1): # j = i+2-1 < n
            j = i+1
            dp[i][i+1] = max(stones[i], stones[j])

        for length in range(3, n+1):
            for i in range(0, n-length+1+1): # j = i+length-1 < n => i < n-length+1
                j = i+length-1
                
                # be careful of that j+1 can be out-of-bound, we take max() with n
                presum1 = presum[min(j+1, n)]-presum[i+1] # remove left
                presum2 = presum[j]-presum[i] # remove right
                dp[i][j] = max(presum1-dp[i+1][j], presum2-dp[i][j-1])

        return dp[0][n-1]

class Solution_TLE:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        # dp[i][j]: the maximum difference when playing in stones[i:j]
        dp = [[0] * 1005 for _ in range(1005)]
        
        # base: length = 1
        for i in range(n):
            j = i # j = i+length-1 = i+1-1
            dp[i][j] = 0
        # base: length = 2
        for i in range(n-1): # j = i+2-1 < n
            j = i+1
            dp[i][i+1] = max(stones[i], stones[j])

        for length in range(3, n+1):
            for i in range(0, n-length+1+1): # j = i+length-1 < n => i < n-length+1
                j = i+length-1
                dp[i][j] = max(sum(stones[i+1:j+1])-dp[i+1][j], sum(stones[i:j-1+1])-dp[i][j-1])

        return dp[0][n-1]
