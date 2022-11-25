# leetcode 912.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        
        def shellsort(nums: List[int], n: int):
            # shellSort(array, size)
            #   for interval i <- size/2n down to 1
            #     for each interval "i" in array
            #         sort all the elements at interval "i"
            # end shellSort
            gap = n//2
            while gap >= 1:
                for i in range(gap, n):
                    key = nums[i]
                    j = i-gap
                    while j >= 0 and nums[j] > key:
                        nums[j+gap] = nums[j]
                        j -= gap
                    nums[j+gap] = key
                    
                gap //= 2
                    
        
        shellsort(nums, len(nums))
        return nums
