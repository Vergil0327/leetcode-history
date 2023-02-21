class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = nums[0], nums[n-1]
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l)//2
            nums[mid]
            equalsLeft, equalsRight = False, False
            if mid+1 < n:
                if nums[mid] == nums[mid+1]:
                    equalsRight = True
            if mid-1 >= 0:
                if nums[mid] == nums[mid-1]:
                    equalsLeft = True
            if not equalsLeft and not equalsRight:
                return nums[mid]

            if equalsLeft:
                numLeft = mid-1
                numRight = r-mid
                if numRight%2 == 0:
                    r = mid-2
                else:
                    l = mid+1
            else:
                numLeft = mid
                numRight = r-(mid+1)
                if numRight%2 == 0:
                    r = mid-1
                else:
                    l = mid+2
        return nums[l]