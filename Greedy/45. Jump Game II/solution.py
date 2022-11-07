# https://labuladong.github.io/algo/3/29/102/
class GreedySolution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        step = 0
        farthest = 0
        end = 0
        # The test cases are generated such that you can reach nums[n - 1].
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            # one jump, [i:farthest]
            if end == i:
                step += 1
                end = farthest

        return step

# https://www.youtube.com/watch?v=Ua_Vqtdd61E
class SolutionBFS:
    def jump(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1: return 0
        
        n = len(nums)
        step = 0
        start = end = 0
        while start <= end:
            newEnd = end
            for i in range(start, end+1):
                newEnd = max(newEnd, i+nums[i])
            
                if newEnd >= n-1:
                    return step + 1
            
            step += 1
            start = end+1
            end = newEnd
        return -1

# O(n^2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i >= n-1: return 0
            
            steps = float("inf")
            for j in range(1, min(nums[i]+1, n)):
                if j == n-1: return 1
                steps = min(steps, dfs(i+j))
            return steps+1
            
        return dfs(0)

# O(n^2) Bottom-Up
class SolutionTLE:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, min(nums[i]+1, n)):
                if i+j < n+1:
                    dp[i+j] = min(dp[i+j], dp[i]+1)

        return dp[n-1]