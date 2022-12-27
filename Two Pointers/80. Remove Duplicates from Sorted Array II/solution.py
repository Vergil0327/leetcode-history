# l valid position
# cnt count of nums[l]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, 0
        cnt = 0
        while r < n:
            if nums[r] != nums[l]:
                cnt = 0
                l += 1
                nums[l] = nums[r]
            elif l < r and cnt < 2:
                l += 1
                nums[l] = nums[r]

            cnt += 1
            r += 1
            
        return l+1