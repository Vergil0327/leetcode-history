# I don't think python has tail-recursion optimization...but
# after removing if l > r: return 0, it reduce runtime from 5000 ms to 3000 ms strangely

# https://www.youtube.com/watch?v=VFskby7lUbw
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(l, r):
            # if l > r: return 0
            return max([arr[l-1]*arr[i]*arr[r+1] + dfs(l, i-1) + dfs(i+1, r) for i in range(l, r+1)] or [0])

        @functools.lru_cache(None)
        def dfsTLE(l, r):
            if l > r: return 0
            return max([arr[l-1]*arr[i]*arr[r+1] + dfs(l, i-1) + dfs(i+1, r) for i in range(l, r+1)] or [0])
        return dfs(1, len(arr)-2)

# https://www.youtube.com/watch?v=BBdHB2jjNUA
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j]: maximum coins you can collect by bursting the balloons[i:j]
        n = len(nums)
        nums = [1] + nums + [1]
        
        dp = [[0] * (n+2) for _ in range(n+2)]
        
        for length in range(1, n+1):
            # for i + length -1 <= n
            for i in range(n-length+2):
                    j = i+length-1
                    for k in range(i, j+1):
                        # dp[i][j]
                        dp[i][j] = max(dp[i][j], nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j])

        return dp[1][n]

# https://www.youtube.com/watch?v=VFskby7lUbw
class SolutionTLE:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(l, r):
            if l > r: return 0
            
            maxPoints = 0
            for i in range(l, r+1):
                points = arr[l-1]*arr[i]*arr[r+1]
                points += dfs(l, i-1) + dfs(i+1, r)
                maxPoints = max(maxPoints, points)
            return maxPoints
        return dfs(1, len(arr)-2)