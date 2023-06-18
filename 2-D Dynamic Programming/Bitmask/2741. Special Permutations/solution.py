class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10**9+7
        
        n = len(nums)
        
        valid = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if nums[i]%nums[j] == 0:
                    valid[i][j] = True
                    valid[j][i] = True
                
        # dp[bitmask][prev]
        totalStates =(1<<n)-1
        @lru_cache(None)
        def dfs(bitmask, prev):
            if bitmask == totalStates: return 1

            res = 0
            for i in range(n):
                if (bitmask>>i)&1: continue
                if prev == -1 or valid[i][prev]:
                    res += dfs(bitmask | (1<<i), i)
            return res
        return dfs(0, -1)%mod
        