
# time: O(n)
# space: O(n)
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [nums[0]]*n
        for i in range(1, n):
            presum[i] = presum[i-1] + nums[i]
            
        sufsum = [0]*n
        for i in range(n-2, -1, -1): # ! exclude i itself
            sufsum[i] = sufsum[i+1] + nums[i+1]
        
        minDiff = float("inf")
        res = -1
        for i in range(n):
            a = presum[i]//(i+1)
            b = sufsum[i]//(n-i-1) if n-i-1>0 else 0 # ! be careful of zero division
            diff = abs(a-b)
            if diff < minDiff:
                minDiff = diff
                res = i
        return res

# time: O(n)
# space: O(1), only 4 variables
class OptimizedSolution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        total = sum(nums)
        currPresum = 0
        
        minDiff = float("inf")
        res = -1
        for i in range(n):
            currPresum += nums[i]
            currSufsum = total - currPresum

            a = currPresum//(i+1)
            b = currSufsum//(n-i-1) if n-i-1>0 else 0
            diff = abs(a-b)
            if diff < minDiff:
                minDiff = diff
                res = i
        return res