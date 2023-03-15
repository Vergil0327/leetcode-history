class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], K: int) -> int:
        n = len(nums)
        
        # dp[i][j]: the minimum total space wasted if you can resize the array[:i] with j times resize operations
        dp = [[inf]*(K+1) for _ in range(n)]

        maxSize = accuSum = 0
        for i in range(n):
            maxSize = max(maxSize, nums[i])
            accuSum += nums[i]
            dp[i][0] = maxSize*(i+1) - accuSum
            
        # for i in range(n):
        for i in range(1, n):
            for k in range(1, min(i, K)+1):
                maxSize = -inf
                accuSum = 0
                # for j in range(i, -1, -1): # the previous time we resize
                for j in range(i, 0, -1): # the previous time we resize
                    maxSize = max(maxSize, nums[j])
                    accuSum += nums[j]
                    # dp[i][k] = min(dp[i][k], dp[j-1][k-1] + maxSize*(i-j+1) - sum(nums[j:i+1]))
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + maxSize*(i-j+1) - accuSum)
        return min(dp[n-1])
