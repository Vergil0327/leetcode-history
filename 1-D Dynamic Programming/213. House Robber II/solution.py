# since nums[0] is adjacent to nums[-1],
# we can see it as two robI problems
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def robI(nums):
            if len(nums) == 1: return nums[0]
            rob1, rob2 = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nxt = max(rob2, nums[i]+rob1)
                rob1, rob2 = rob2, nxt
            return rob2
        
        return max(robI(nums[:-1]), robI(nums[1:]))