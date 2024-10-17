class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx_sum = min_sum = res = 0
        for num in nums:
            mx_sum += num
            min_sum += num
            res = max(res, abs(mx_sum), abs(min_sum))

            mx_sum = max(0, mx_sum)
            min_sum = min(0, min_sum)
        return res

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx_sum = min_sum = res = 0
        for num in nums:
            mx_sum = max(0, mx_sum+num)
            min_sum = min(0, min_sum+num)
            res = max(res, abs(mx_sum), abs(min_sum))

        return res