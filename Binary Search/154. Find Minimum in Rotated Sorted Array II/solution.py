class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums)>1 and nums[0] == nums[-1]:
            nums.pop()

        minVal = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            minVal = min(minVal, nums[mid])

            if nums[0] <= nums[mid]: # left portion
                l = mid+1
            else:
                r = mid-1
        return minVal