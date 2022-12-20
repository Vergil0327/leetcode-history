# Top-Down DP
class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def dfs(characters, copy):
            if characters == n: return 0
            if characters > n: return inf
            # copy + paste: we can't achieve minimum operations by just copy & copy
            # must copy combined with 1 paste
            steps1 = dfs(characters+characters, characters) + 2

            # only paste with we've already copy 1 character at least
            steps2 = inf
            if copy > 0:
                steps2 = dfs(characters+copy, copy) + 1
            return min(steps1, steps2)

        return dfs(1, 0)

# Bottom-Up
class Solution:
    def minSteps(self, n: int) -> int:
        # dp[i]: the minimum operations to achieve i character
        dp = [inf] * (n+1)
        
        # base case: 1 character on the screen in the beginning
        dp[1] = 0

        for i in range(2, n+1):
            dp[i] = i # copy 1 character & paste, paste, ...
            for copy in range(1, i+1):
                if i%copy == 0:
                    times = i//copy
                    dp[i] = min(dp[i], dp[copy]+times)
        return dp[n]

# Bottom-Up + Greedy
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [inf] * (n+1)
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = i # copy 1 & paste, paste, ...
            for copy in range(i-1, 1, -1): # be greedy
                if i%copy == 0:
                    times = i//copy
                    dp[i] = min(dp[i], dp[copy]+times)
                    break
        return dp[n]
