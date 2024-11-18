class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0
        presum = list(accumulate(nums, initial=0))
        for i in range(n):
            if nums[i] == 0:
                left, right = presum[i], presum[n]-presum[i]
                if left == right:
                    res += 2
                elif abs(left-right) == 1:
                    res += 1
        return res

# space-optimized
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        res = left = 0
        right = sum(nums)
        for i in range(n):
            right -= nums[i]
            
            if nums[i] == 0:
                if left == right:
                    res += 2
                elif abs(left-right) == 1:
                    res += 1

            left += nums[i]
        return res
