"""
it's hard to build string from "" and count how many valid string which low <= length <= high

reverse thinking:
    if we can reduce length by zero/step or one/step to 0 successfully, it should be valid length
    
therefore, we can iterate from low to high (both inclusive) and count how many different good strings we can construct
"""

class SolutionTopDown:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007
        
        @functools.lru_cache(None)
        def dfs(length):
            if length == 0:
                return 1
            if length < 0:
                return 0
            
            count1 = dfs(length-zero)
            count2 = dfs(length-one)
            return (count1 + count2) % MOD
        
        cnt = 0
        for length in range(low, high+1):
            cnt += dfs(length)
        return cnt % MOD


"""
definition: dp[i]: the number of good string with i length long
we can also build good string from empty string and sum up the number of good string satisfying the conditions
"""
class SolutionBottomUp:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007
        
        # dp[i]: the number of good string with i length long
        # good string is constructed from empty string

        dp = [0] * (high+1)
        dp[0] = 1 # empty string is good string
        
        total = 0
        for i in range(1, high+1):
            dp[i] = 0
            if i-zero >= 0:
                dp[i] += dp[i-zero]
            if i-one >= 0:
                dp[i] += dp[i-one]
            dp[i] %= MOD
            if i >= low:
                total = (total + dp[i]) % MOD
            
        return total