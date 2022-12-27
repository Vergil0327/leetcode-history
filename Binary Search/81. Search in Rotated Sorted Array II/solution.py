class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        while len(nums)>1 and nums[0] == nums[-1]:
            nums.pop()
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target: return True

            if (nums[mid] >= nums[0]) == (target >= nums[0]): # target and mid in the same sorted intervals -> normal binary search
                if target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            elif target >= nums[0]: # target in the left portion
                r = mid-1
            else: # target in the right portion
                l = mid+1
        
        return False