class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        
        @cache
        def dfs(i, sign, total, prod, picked):
            if i >= len(nums):
                if picked and total == k and prod <= limit:
                    return prod
                return -inf
            prod1 = dfs(i+1, sign, total, prod, picked)
            prod2 = dfs(i+1, sign*-1, total+nums[i]*sign, min(limit+1, prod*nums[i]), True)
            return max(prod1, prod2)
        res = dfs(0, 1, 0, 1, False)
        dfs.cache_clear()
        return res if res > -inf else -1