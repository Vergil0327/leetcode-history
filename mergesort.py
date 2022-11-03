class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(set(nums)) == 1: return nums
        
        tmp = [0] * len(nums)
        def merge(nums, l, mid, r):
            tmp[l:r+1] = nums[l:r+1].copy()

            i, j = l, mid+1
            for k in range(l, r+1):
                if i == mid+1: # left-half is finished
                    nums[k] = tmp[j]
                    j += 1
                elif j == r+1:
                    nums[k] = tmp[i]
                    i += 1
                elif tmp[i] > tmp[j]:
                    nums[k] = tmp[j]
                    j += 1
                else:
                    nums[k] = tmp[i]
                    i += 1
            
        def mergesort(nums, l, r):
            if l == r: return
                
            mid = l + (r-l)//2
            mergesort(nums, l, mid)
            mergesort(nums, mid+1, r)
            merge(nums, l, mid, r)
            
        mergesort(nums, 0, len(nums)-1)
        return nums