class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def lessThanEqual(threshold):
            plus = 0
            for i in range(len(nums)-1, 0, -1):
                if nums[i] <= threshold:
                    plus -= threshold - nums[i]
                    if plus < 0: plus = 0
                else:
                    plus += nums[i] - threshold
            return nums[0]+plus <= threshold

        l, r = nums[0], max(nums)
        while l < r:
            mid = l + (r-l)//2
            if lessThanEqual(mid): # less than or equal
                r = mid
            else:
                l = mid+1
        return l
