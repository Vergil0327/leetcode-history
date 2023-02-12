from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        # lower-nums[j] <= nums[i] <= upper - nums[j]
        res = 0
        for num in nums:
            i = sl.bisect_left(lower-num)
            j = sl.bisect_right(upper-num)
            res += j-i
            sl.add(num)
        return res