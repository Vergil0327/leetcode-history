
class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        inf = float('inf')
        n = len(nums)
        sl = SortedList()  # sorted list of (value, index)
        inv_count = 0
        res = inf
        for i in range(n):
            if i - k >= 0:
                leftmost = nums[i - k]
                smaller = sl.bisect_left((leftmost, 0))
                inv_count -= smaller
                if (leftmost, i - k) in sl:
                    sl.remove((leftmost, i - k))

            cur = nums[i]
            greater = len(sl) - sl.bisect_right((cur, inf))
            inv_count += greater
            sl.add((cur, i))

            if i >= k - 1:
                res = min(res, inv_count)

        return res