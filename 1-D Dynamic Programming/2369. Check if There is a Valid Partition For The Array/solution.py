# Bottom-Up
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n+1)
        dp[0] = True
        nums = [inf] + nums
        for i in range(1, n+1):
            if nums[i] == nums[i-1]:
                dp[i] = dp[i] or dp[i-2]
            if i-3 >= 0 and (nums[i] == nums[i-1] == nums[i-2] or nums[i] == nums[i-1]+1 and nums[i-1] == nums[i-2]+1):
                dp[i] = dp[i] or dp[i-3]
        return dp[n]

# Top-Down
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dfs(i):
            if i == n: return True

            if i+1 < n and nums[i] == nums[i+1]:
                if dfs(i+2): return True
            if i+2<n and (nums[i] == nums[i+1] == nums[i+2] or nums[i] == nums[i+1]-1 and nums[i+1] == nums[i+2]-1):
                if dfs(i+3): return True

            return False

        return dfs(0)
                