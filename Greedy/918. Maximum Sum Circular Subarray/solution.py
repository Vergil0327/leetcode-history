class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0
        MAX = currMax = -inf
        MIN = currMin = inf
        for num in nums:
            currMax = max(currMax+num, num)
            MAX = max(MAX, currMax)
            currMin = min(currMin+num, num)
            MIN = min(MIN, currMin)

            total += num
        return max(MAX, total-MIN) if MAX > 0 else MAX