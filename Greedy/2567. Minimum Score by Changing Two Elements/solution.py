class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-3] - nums[0], nums[-2] - nums[1])

# same idea, different implementation
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        k = n - 3
        ans = inf
        for i in range(n - k):
            ans = min(ans, nums[i+k] - nums[i])
        return ans