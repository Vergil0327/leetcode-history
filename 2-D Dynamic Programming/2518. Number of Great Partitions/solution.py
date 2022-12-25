class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2*k: return 0
        
        n = len(nums)
        MOD = 1_000_000_007

        # dp[i][j]: total number of subsets in the array with their sum j is smaller than k for nums[:i]
        dp = [[0]*k for _ in range(n+1)]

        # base case
        for j in range(k):
            dp[0][j] = 1 # one empty subset
        # dp[i][0] = 0 where i from 1 to n

        nums = [0] + nums # shfit index to 1-based. be consistent with dp
        for i in range(1, n+1):
            for j in range(k): # find sum from 0 to k-1
                dp[i][j] = dp[i-1][j]
                if j-nums[i] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i]]
        
        invalid = dp[n][k-1] # sum is k-1 which is smaller than k
        return (pow(2, n) - 2 * invalid) % MOD

# Brute Force
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        SUM = sum(nums)
        MOD = 1_000_000_007
        
        @lru_cache(None)
        def dfs(i, total):
            if i == n: return 0
            
            great = 1 if total+nums[i] >= k and (SUM-total-nums[i]) >= k else 0
            
            great += dfs(i+1, total)
            great += dfs(i+1, total+nums[i])
            return great % MOD
        return dfs(0, 0)