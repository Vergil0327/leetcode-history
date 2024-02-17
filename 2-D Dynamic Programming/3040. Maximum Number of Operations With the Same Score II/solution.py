class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(l, r, score):
            if l >= r: return 0
            
            res = 0
            if l+1 <= r and (score == 0 or score == nums[l]+nums[l+1]):
                res = max(res, dfs(l+2, r, nums[l]+nums[l+1])+1)
            if r-2 >= l and (score == 0 or score == nums[r]+nums[r-1]):
                res = max(res, dfs(l, r-2, nums[r]+nums[r-1])+1)
            if l < r and (score == 0 or score == nums[l]+nums[r]):
                res = max(res, dfs(l+1, r-1, nums[l]+nums[r])+1)
            return res
        return dfs(0, len(nums)-1, 0)
