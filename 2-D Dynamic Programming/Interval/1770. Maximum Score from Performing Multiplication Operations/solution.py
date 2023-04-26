class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        M = len(multipliers)
        @lru_cache(None)
        def dfs(m, l, r):
            if m >= M: return 0
            return max(nums[l]*multipliers[m] + dfs(m+1, l+1, r), nums[r]*multipliers[m] + dfs(m+1, l, r-1))
        return dfs(0, 0, len(nums)-1)

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        M = len(multipliers)

        # 由於 l,r 受限於m, l取m個的話那r肯定不變, 依舊m-1
        # 所以我們cache (m, l)即可
        cache = {} # cache[(m,l)] = maximum score
        def dfs(m, l, r):
            if m >= M: return 0
            if (m,l) in cache: return cache[(m,l)]
            cache[(m,l)] = max(nums[l]*multipliers[m] + dfs(m+1, l+1, r), nums[r]*multipliers[m] + dfs(m+1, l, r-1))
            return cache[(m,l)]
        return dfs(0, 0, len(nums)-1)

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        # dp[i][j]: the maximum score for nums[:i] and nums[j:]. i.e. pick first i elements and last j elements
        # X X X X _ _ _ _ _ _ _ X X X X X X
        #       i               j

        dp = [[-inf]*(m+1) for _ in range(m+1)]
        nums = [0] + nums # to 1-indexed

        # base case
        dp[0][0] = 0
        
        res = -inf
        for length in range(1, m+1): # total take length elements from both sides
            for i in range(length+1):
                j = length-i
                dp[i][j] = max(
                    dp[i][j],
                    (dp[i-1][j]+nums[i]*multipliers[i+j-1] if i-1>=0 else -inf),
                    (dp[i][j-1]+nums[n-j+1]*multipliers[i+j-1] if j-1 >= 0 else -inf))
                if length == m:
                    res = max(res, dp[i][j])
        return res