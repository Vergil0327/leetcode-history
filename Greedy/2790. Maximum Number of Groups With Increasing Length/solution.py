class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        n = len(usageLimits)
        usageLimits.sort()
        
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + usageLimits[i-1]
            
        targetGroups = 1
        for i in range(1, n+1):
            require = (1+targetGroups)*targetGroups//2
            if presum[i] >= require:
                targetGroups += 1

        return targetGroups-1
