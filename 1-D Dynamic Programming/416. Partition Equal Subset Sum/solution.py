class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False

        n = len(nums)
        
        @lru_cache(None)
        def dfs(i, diff):
            if i == n:
                if diff == 0: return True
                return False

            # choose for 1st set
            if dfs(i+1, diff+nums[i]): return True

            # not choose for 1st set
            if dfs(i+1, diff-nums[i]): return True

            return False
        return dfs(0, 0)

# Bottom-Up
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False

        target = total//2
        # dp[i]: True/False means can we make i sum for one set
        dp = defaultdict(bool)

        # base case, put nothing in one set and we get 0 sum
        dp[0] = True

        for num in nums:
            nextDP = defaultdict(bool)
            for currSum in dp:
                nextDP[currSum+num] = True
                nextDP[currSum] = True
            dp = nextDP
        return dp[target]

# 0/1 knapsack problem
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False

        target = total//2
        n = len(nums)

        # dp[i][j]: can we use first i num to make sum equal to j.
        dp = [[False] * (total+1) for _ in range(n+1)]

        # base case
        ## we can make sum = 0 for every fisrt i nums
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, total+1):
                if j-nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                    continue
                
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        return dp[n][target]

# 0/1 knapsack problem - space-optimized
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False

        target = total//2
        n = len(nums)

        # dp[i][j]: can we use first i num to make sum equal to j.
        # dp = [[False] * (total+1) for _ in range(n+1)]
        dp = [False] * (total+1)

        # base case
        ## we can make sum = 0 for every fisrt i nums
        # for i in range(n+1):
        #     dp[i][0] = True
        dp[0] = True

        for i in range(1, n+1):
            for j in range(total, 0, -1):
                if j-nums[i-1] < 0:
                    # dp[i][j] = dp[i-1][j]
                    # dp[j] = dp[j]
                    continue
                
                # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                dp[j] = dp[j] or dp[j-nums[i-1]]
        
        # return dp[n][target]
        return dp[target]