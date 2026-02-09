from sortedcontainers import SortedList
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = res = 0
        sl = SortedList()
        while r < n:
            num = nums[r]
            sl.add(num)
            r += 1

            # cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1) <= k
            # X {X X X X} X X
            while l < r and (sl[-1] - sl[0]) * len(sl) > k:
                sl.remove(nums[l])
                l += 1

            res += r-l
        return res
