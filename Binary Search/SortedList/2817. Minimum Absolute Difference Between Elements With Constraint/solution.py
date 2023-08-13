from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sl = SortedList()
        for i in range(x, n):
            sl.add(nums[i])
        res = inf
        for i, num in enumerate(nums):
            r = sl.bisect_right(num)
            l = r-1
            if r < len(sl):
                res = min(res, abs(sl[r]-num))
            if l >= 0:
                res = min(res, abs(sl[l]-num))
            if i+x < n:
                sl.remove(nums[i+x])
        return res