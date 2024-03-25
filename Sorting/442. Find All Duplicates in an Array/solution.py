class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)

        j = n-1
        for i in range(n):
            if nums[i] == i+1: continue

            while j >= 0 and nums[i] != i+1:
                idx = nums[i]-1
                if idx < i or nums[i] == nums[idx]: # duplicate
                    nums[i], nums[j] = nums[j], nums[i]

                    # move j to next unsorting element
                    j -= 1
                    while j >= 0 and nums[j] == j+1:
                        j -= 1
                else:
                    nums[i], nums[idx] = nums[idx], nums[i]
        return [nums[i] for i in range(n) if nums[i] != i+1]
