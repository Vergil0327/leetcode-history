from functools import lru_cache
from typing import List
from math import inf, ceil

# top-down
class SolutionTopDown:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        # use bitmask to represent defeat state
        # 0010 means we only defeat 1st monster with power[1]
        @lru_cache(None)
        def dfs(defeatState):
            count = bin(defeatState).count("1")
            if count == len(power): return 0

            res = inf
            for i in range(n):
                if (defeatState>>i)&1 == 1: continue

                daysNeed = ceil(power[i] / (1+count))
                res = min(res, dfs(defeatState | (1<<i)) + daysNeed) # choose i-th monster to defeat
            return res
        return dfs(0)

class SolutionBottomUp:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        
        maxState = 1<<n
        dp = [inf]*(maxState)
        dp[0] = 0 # base case

        for state in range(maxState):
            gain = state.bit_count()
            for i in range(n):
                if (state>>i)&1 == 0: continue
                daysNeed = ceil(power[i]/(1+(gain-1))) # remember to minus current 1 from `gain`
                dp[state] = min(dp[state], dp[state-(1<<i)] + daysNeed)
        return dp[maxState-1]