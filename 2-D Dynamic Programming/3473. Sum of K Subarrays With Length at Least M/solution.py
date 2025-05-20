class Solution:
    def maxSum(self, nums: List[int], K: int, m: int) -> int:
        n = len(nums)

        presum = list(accumulate(nums, initial=0))
        @cache
        def dfs(i, k, appending):
            if i >= n:
                return 0 if k == 0 else -inf
            if n-i < k*m: return -inf # can't get k subarrays at least from remain nums[i:]
            
            res = dfs(i+1, k, False)

            if appending:
                res = max(res, dfs(i+1, k, appending) + nums[i])

            if k>0 and i+m <= n:
                res = max(res, dfs(i+m, k-1, True) + presum[i+m]-presum[i])
            return res
        
        dfs.cache_clear()
        return dfs(0, K, False)