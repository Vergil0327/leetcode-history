from random import randint

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(set(nums)) == 1: return nums

        def partition(nums, l, r):
            if l == r: return l
            
            # random pick pivot and put to right-most position
            pivotIdx = randint(l, r)
            nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]
            
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]
            return p
        
        def quicksort(nums, l, r):
            if l < r:
                p = partition(nums, l, r)
                quicksort(nums, l, p-1)
                quicksort(nums, p+1, r)
            return
        
        quicksort(nums, 0, len(nums)-1)
        return nums