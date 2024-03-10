class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        memo = [[[inf, inf] for _ in range(k+1)] for _ in range(n+1)]
        def dfs(i, k, appending):
            if k == 0: return 0
            if i == n:
                if k == 1 and appending: return 0
                return -inf

            if memo[i][k][appending] < inf: return memo[i][k][appending]

            memo[i][k][appending] = dfs(i+1, k, 1) + nums[i]*k*(1 if k%2 == 1 else -1)
            if appending:
                memo[i][k][appending] = max(memo[i][k][appending], dfs(i, k-1, 0))
            else:
                memo[i][k][appending] = max(memo[i][k][appending], dfs(i+1, k, 0))

            return memo[i][k][appending]
        return dfs(0, k, 0)
            
