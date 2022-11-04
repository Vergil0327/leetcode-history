class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def mergesort(l, r):
            nonlocal count
            if l == r: return
            
            mid = l + (r-l)//2
            mergesort(l, mid)
            mergesort(mid+1, r)
            
            j = mid+1
            for i in range(l, mid+1):
                while j < r+1 and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid+1)
                
            nums[l:r+1] = sorted(nums[l:r+1])
            
        mergesort(0, len(nums)-1)
        return count