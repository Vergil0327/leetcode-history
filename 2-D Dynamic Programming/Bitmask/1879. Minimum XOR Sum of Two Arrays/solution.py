class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @cache
        def dfs(i, state):
            if i >= n: return 0
            
            res = inf
            for j in range(n):
                if (state>>j)&1 == 1: continue
                res = min(res, dfs(i+1, state|(1<<j)) + (nums1[i]^nums2[j]))
            return res
            
        return dfs(0, 0)
