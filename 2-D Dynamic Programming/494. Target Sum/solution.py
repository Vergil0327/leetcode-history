# each number we can choose add "+" or "-"
# keep tracking our total sum
# if total sum equals to target, it means we found 1 way to make sum to target
# sum up all the possible choices
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, total):
            if i == n:
                if total == target:
                    return 1 # one possible way
                return 0

            # ways of (add "+") + ways of (add "-")
            return dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
        return dfs(0, 0)

# DP solution
# turn problem into 0/1 knapsack problem
class Solution:
    """
    A: contains num which is added "+" sign
    B: contains num which is added "-" sign

    sum(A) - sum(B) = target
    sum(A) = target + sum(B)
    sum(A) + sum(A) = target + sum(B) + sum(A)
    2 * sum(A) = target + sum(nums)
    sum(A) = (target + sum(nums)) / 2
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][j]: use first i nums to make j sum
        n = len(nums)
        total = sum(nums)

        if (target+total)%2 != 0 or total < abs(target): return 0

        targetSum = (target+total)//2
        dp = [[0] * (targetSum+1) for _ in range(n+1)]

        # base case
        dp[0][0] = 1 # one way to make 0 sum for using first i num

        for i in range(1, n+1):
            for j in range(targetSum+1):
                if j-nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                    continue

                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        return dp[n][targetSum]
