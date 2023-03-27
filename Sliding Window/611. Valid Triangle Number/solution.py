class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # triangle: any two side length > 3rd side length
        nums.sort()
        res = 0
        for k in range(len(nums)-1, 1, -1):
            l, r = 0, k-1
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    res += r-l
                    r -= 1
                else:
                    l += 1
            
        return res
