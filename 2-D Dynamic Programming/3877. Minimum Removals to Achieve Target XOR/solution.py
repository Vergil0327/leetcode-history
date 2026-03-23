class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        if not nums: return target == 0

        n = len(nums)
        @cache
        def dfs(i, xor):
            if i >= n:
                return 0 if xor == target else -float('inf')
            res = dfs(i+1, xor)
            res = max(res, dfs(i+1, xor ^ nums[i]) + 1)

            return res
        
        removal = dfs(0, 0)
        return n - removal if removal > -float('inf') else -1
    
