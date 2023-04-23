from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl = SortedList()
        n = len(nums)
        l = r = 0
        res = []
        while r < n:
            sl.add(nums[r])
            r += 1
            
            while l < r and r-l>k:
                sl.remove(nums[l])
                l += 1
            if r-l == k and x-1 < len(sl):
                if sl[x-1] < 0:
                    res.append(sl[x-1])
                elif sl[x-1] >= 0:
                    res.append(0)
        return res