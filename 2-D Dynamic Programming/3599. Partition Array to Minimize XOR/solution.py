class Solution:
    def minXor(self, nums: List[int], K: int) -> int:
        n = len(nums)

        # prexor = list(accumulate(nums, operator.xor, initial=0))
        prexor = [0]
        for num in nums:
            prexor.append(prexor[-1]^num)

        memo = [[inf]*(K+1) for _ in range(n+1)]
        def dfs(i, k):
            if i >= n:
                return inf if k != 0 else 0
            if k == 1: return prexor[n]^prexor[i]
            if memo[i][k] < inf: return memo[i][k]

            for j in range(i, n-k+1):
                memo[i][k] = min(memo[i][k], max(prexor[j+1]^prexor[i], dfs(j+1, k-1)))
            return memo[i][k]
        
        return dfs(0, K)