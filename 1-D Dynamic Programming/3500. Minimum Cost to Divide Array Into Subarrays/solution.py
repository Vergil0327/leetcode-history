class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        presum_num = list(accumulate(nums))
        presum_cost = list(accumulate(cost, initial=0)) # 1-indexed

        dp = [inf] * (n+1)
        dp[n] = 0 # base case
        for l in range(n-1, -1, -1):
            for r in range(l, n):
                dp[l] = min(dp[l], dp[r+1] + presum_num[r] * (presum_cost[r+1] - presum_cost[l]) + k * (presum_cost[-1] - presum_cost[l]))
        
        return dp[0]

class Solution:
    def minimumCost(self, nums: List[int], costs: List[int], k: int) -> int:
        presum_num = list(accumulate(nums, initial=0))
        presum_cost = list(accumulate(costs, initial=0))
        n = len(nums)

        @cache
        def dp(i):
            if i == n:
                return 0

            res = inf
            for j in range(i, n):
                cand = presum_num[j + 1] * (presum_cost[j + 1] - presum_cost[i]) + k * (presum_cost[-1] - presum_cost[i])
                cand += dp(j + 1)
                res = min(res, cand)

            return res

        return dp(0)