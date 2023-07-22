class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dfs(i, parity):
            if i == n: return 0
            
            if nums[i]%2 == parity:
                return dfs(i+1, parity) + nums[i]
            else:
                return max(dfs(i+1, nums[i]%2) + nums[i] - x, dfs(i+1, parity))
        return dfs(0, nums[0]%2)
    
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)

        dp = [[0,0] for _ in range(n)]
        dp[0][0] = nums[0] if nums[0]%2 == 0 else (nums[0]-x)
        dp[0][1] = nums[0] if nums[0]%2 == 1 else (nums[0]-x)

        for i in range(1, n):
            if nums[i]%2 == 0:
                dp[i][0] = max(dp[i-1][0] + nums[i], dp[i-1][1] + nums[i] - x)
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = max(dp[i-1][1] + nums[i], dp[i-1][0] + nums[i] - x)
        return max(dp[n-1])