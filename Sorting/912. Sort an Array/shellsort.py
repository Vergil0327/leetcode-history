# Pseudo Code
# shellSort(array, size)
        #   for interval i <- size/2n down to 1
        #     for each interval "i" in array
        #         sort all the elements at interval "i"
        # end shellSort

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
            while gap > 0:
                # repeat insertion sort with different gaps 
                # Code exactly similar to insertion sort, only difference is that in case of insertion sort there is only `gap == 1`
                # but here gap start from n/2 and keep reducing untill it becomes 0.
                for i in range(gap, n):
                    current = nums[i]
                    j = i - gap
                    while j >= 0 and nums[j] > current:
                        nums[j+gap] = nums[j]
                        j -= gap
                    nums[j+gap] = current
                gap //= 2
            return nums
        return shellsort(nums, len(nums))