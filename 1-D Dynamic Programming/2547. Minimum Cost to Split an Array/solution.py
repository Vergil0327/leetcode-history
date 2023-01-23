# Brute Force - TLE
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i):
            if i == n: return 0

            counter = defaultdict(int)
            res = inf
            for j in range(i, n):
                counter[nums[j]] += 1
                trimmed = sum(cnt for cnt in counter.values() if cnt > 1)
                res = min(res, k + trimmed + dfs(j+1))
            return res
        return dfs(0)

# Top-Down
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i):
            if i == n: return 0

            counter = defaultdict(int)
            trimmed = 0
            res = inf
            for j in range(i, n):
                counter[nums[j]] += 1
                if counter[nums[j]] > 2:
                    trimmed += 1
                elif counter[nums[j]] == 2:
                    trimmed += 2
                res = min(res, k + trimmed + dfs(j+1))
            return res
        return dfs(0)

# Bottom-Up
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # dp[i]: the minimum possible cost of a split of nums[:i]
        dp = [inf] * n

        for i in range(n):
            counter = defaultdict(int)
            scores = 0  
            for j in range(i, -1, -1):
                counter[nums[j]] += 1
                if counter[nums[j]] == 2:
                    scores += 2
                elif counter[nums[j]] > 2:
                    scores += 1
                if j-1 >= 0:
                    dp[i] = min(dp[i], dp[j-1] + scores + k)
                else:
                    dp[i] = min(dp[i], scores + k)
        
        return dp[n-1]