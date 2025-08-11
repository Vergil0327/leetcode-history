from functools import reduce
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        karr = []
        for i in range(n):
            if nums[i] == i: continue
            j = nums[i]
            karr.append(nums[i]&nums[j])

        INITIAL = (1<<32)-1
        res = reduce(lambda x,y: x&y, karr, INITIAL)
        return res if res < INITIAL else 0