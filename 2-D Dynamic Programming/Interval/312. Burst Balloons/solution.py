# I don't think python has tail-recursion optimization...but
# after removing if l > r: return 0, it reduce runtime from 5000 ms to 3000 ms strangely

# https://www.youtube.com/watch?v=VFskby7lUbw
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(l, r):
            return max([arr[l-1]*arr[i]*arr[r+1] + dfs(l, i-1) + dfs(i+1, r) for i in range(l, r+1)] or [0])
        return dfs(1, len(arr)-2)

class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(l, r):
            maxPoints = 0
            for i in range(l, r+1):
                maxPoints = max(maxPoints, nums[l-1] * nums[i] * nums[r+1] + dfs(l, i-1) + dfs(i+1, r))
            return maxPoints

        return dfs(1, n-2)

# detailed version but TLE
# use too many temp. variable or redundant computation to avoid TLE
class SolutionTLE:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(l, r):
            maxPoints = 0
            for i in range(l, r+1):
                points = arr[l-1]*arr[i]*arr[r+1]
                points += dfs(l, i-1) + dfs(i+1, r)
                maxPoints = max(maxPoints, points)
            return maxPoints
        return dfs(1, len(arr)-2)

# https://www.youtube.com/watch?v=BBdHB2jjNUA
class Solution(object):
    def maxCoins(self, nums):
        n = len(nums)
        nums = [1] + nums + [1]

        # dp[i][j]: maximum coins within nums[i:j]
        # compute small interval first, therefore, outer loop is length and length from low to high
        dp = [[0] * (n+2) for _ in range(n+2)]

        for length in range(1, n+1):
            # [1] [3,1,5,8] [1]
            #  i             j
            # j = i-length+1 <= n, why "<=" ?  because we append [1] in the beginning
            for i in range(1, n-length+2): # i from 1 to i+n. nums[0] and nums[-1] is appended [1].
                j = i+length-1
                # the balloon we can choose
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j])
        return dp[1][n]

# https://www.youtube.com/watch?v=VFskby7lUbw
class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dfs(l, r):
            maxPoints = 0
            for i in range(l, r+1):
                maxPoints = max(maxPoints, nums[l-1] * nums[i] * nums[r+1] + dfs(l, i-1) + dfs(i+1, r))
            return maxPoints

        return dfs(1, n-2)
