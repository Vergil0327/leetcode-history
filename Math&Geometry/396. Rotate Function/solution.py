class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        rotateSum = sum([v * i for i, v in enumerate(nums)])
        
        res = -inf
        while nums: # right rotate
            last = nums.pop()
            rotateSum = rotateSum + total - last * n
            res = max(res, rotateSum)
        return res

        # right rotate
        # nextTotal = total + (sum-nums[n-1]) - nums[n-1] * (n-1)
        #           = total + sum - nums[n-1] * n
        # 4,3,2,6
        # 6,4,3,2
        # 2,6,4,3
        # 3,2,6,4
        # 4*0 + 3*1 + 2*2 + 6*3
        # 6*0 + 4*1 + 3*2 + 2*3
        # 2*0 + 6*1 + 4*2 + 3*3
        # 3*0 + 2*1 + 6*2 + 4*3
