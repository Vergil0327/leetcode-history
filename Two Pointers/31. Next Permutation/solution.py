class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # step 1:find position we need to increase
        i = n-1
        while i >= 1 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i == 0: # [3,2,1] -> [1,2,3]
            nums.sort()
            return

        # step 2
        i -= 1 # swap position
        j = n-1 # index of wanted swap value
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

        # step 3
        nums[i+1:] = sorted(nums[i+1:])
