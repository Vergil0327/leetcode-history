class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(n+1):
            i = bisect.bisect_left(nums, x)
            if n-i == x: return x
        return -1
