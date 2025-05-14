class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList()

        n = len(nums)
        l = res = 0
        for r in range(n):
            sl.add(nums[r])
            while sl and abs(nums[r]-sl[0]) > 2 or abs(nums[r]-sl[-1]) > 2:
                sl.remove(nums[l])
                l += 1
            res += len(sl)
        return res