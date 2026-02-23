from fractions import Fraction 
from collections import defaultdict

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        dp = defaultdict(int)
        dp[Fraction(1,1)] = 1
        for x in nums:
            newDp = defaultdict(int)
            for val, cnt in dp.items():
                newDp[val*x] += cnt
                newDp[val/x] += cnt
                newDp[val] += cnt
            dp = newDp
        return dp[Fraction(k,1)]