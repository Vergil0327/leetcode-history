# shell sort is optimized insertion sort: https://www.programiz.com/dsa/shell-sort
# time complexity
# Best	O(nlog n)
# Worst	O(n^2)
# Average	O(nlog n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        
        def shellsort(nums, n):
            # start with a big gap, then reduce the gap
            gap = n//2
            while gap >= 1:
                # repeat insertion sort with different gaps 
                # Code exactly similar to insertion sort, only difference is that in case of insertion sort there is only `gap == 1`
                # but here gap start from n/2 and keep reducing untill it becomes 0.
                for i in range(gap, n):
                    key = nums[i]
                    j = i - gap
                    while j >= 0 and nums[j] > key:
                        nums[j+gap] = nums[j]
                        j -= gap
                    nums[j+gap] = key
                gap //= 2
        
        shellsort(nums, len(nums))
        return nums