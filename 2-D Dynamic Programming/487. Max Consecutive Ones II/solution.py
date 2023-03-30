from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i][0]: maximum consecutive ones when iteration ends at i without flip
        # dp[i][1]: maximum consecutive ones when iteration ends at i with flip   
        dp = [[0,0] for _ in range(n)]

        # handle i=0 independently to get rid of out-of-bounds error
        dp[0][0] = 1 if nums[0] == 1 else 0
        dp[0][1] = 1

        res = 0
        for i in range(1, n):
            if nums[i] == 0:
                dp[i][1] = dp[i-1][0] + 1
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + 1
            res = max(res, dp[i][1])
        
        return res
    
# space optimization
class SpaceOpimizedSolution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        res = flip = noflip = 0
        for i in range(n):
            if nums[i] == 0:
                flip = noflip + 1
                noflip = 0
            else:
                noflip += 1
                flip += 1
            res = max(res, flip)
        return res
