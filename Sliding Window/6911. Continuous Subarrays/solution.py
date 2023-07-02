from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        window = SortedList()
        
        res = 0
        n = len(nums)
        l = r = 0
        while r < n:
            num = nums[r]
            window.add(num)
            r += 1
            
            while l < r and window[-1]-window[0] > 2:
                window.remove(nums[l])
                l += 1
            res += len(window)
            
        return res