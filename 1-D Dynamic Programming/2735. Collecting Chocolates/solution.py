class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        minNum = nums.copy()
        res = inf
        for rotation in range(n):
            cost = rotation * x
            
            curSum = 0
            for i in range(n):
                minNum[i] = min(minNum[i], nums[(i-rotation+n)%n])
                curSum += minNum[i]
                    
            res = min(res, curSum + cost)
        return res
